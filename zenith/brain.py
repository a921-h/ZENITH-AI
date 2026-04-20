import httpx
import json
import re
import os
import google.generativeai as genai
from dotenv import load_dotenv
from zenith.memory import get_recent_insights, save_insight, init_db, get_knowledge_graph

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "zenith")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama") # 'ollama' o 'gemini'

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

init_db()

PERSONAS = {
    "staff": "Eres un Staff Engineer. Tu enfoque es pragmático, técnico y orientado a resultados de alto nivel.",
    "security": "Eres un Experto en Seguridad (CISO/Pentester). Tu prioridad es encontrar vulnerabilidades y asegurar el código.",
    "architect": "Eres un Arquitecto de Software. Te enfocas en patrones de diseño, escalabilidad y desacoplamiento.",
    "reviewer": "Eres un Code Reviewer meticuloso. Buscas clean code, mejores nombres y legibilidad extrema."
}

class Brain:
    def __init__(self, persona: str = "staff"):
        self.persona_prompt = PERSONAS.get(persona, PERSONAS["staff"])
        self.provider = AI_PROVIDER

    def _process_ai_text(self, ai_text: str):
        """Procesa etiquetas de aprendizaje, entidades y relaciones."""
        # Procesamos el aprendizaje automático
        if "[LEARN:" in ai_text:
            learn_match = re.search(r'\[LEARN: ([^\]]+)\]', ai_text)
            if learn_match:
                save_insight(learn_match.group(1).strip())
                ai_text = ai_text.replace(learn_match.group(0), "")

        # Procesamos Entidades
        entity_matches = re.findall(r'\[ENTITY: ([^|]+)\|([^|]+)\|([^\]]+)\]', ai_text)
        for name, etype, desc in entity_matches:
            from zenith.memory import save_entity
            save_entity(name.strip(), etype.strip(), desc.strip())
            ai_text = ai_text.replace(f"[ENTITY: {name}|{etype}|{desc}]", "")

        # Procesamos Relaciones
        rel_matches = re.findall(r'\[REL: ([^|]+)\|([^|]+)\|([^\]]+)\]', ai_text)
        for src, rel, tgt in rel_matches:
            from zenith.memory import save_relationship
            save_relationship(src.strip(), tgt.strip(), rel.strip())
            ai_text = ai_text.replace(f"[REL: {src}|{rel}|{tgt}]", "")
        
        if any(tag in ai_text for tag in ["[LEARN:", "[ENTITY:", "[REL:"]):
             ai_text += "\n\n*(ZENITH ha asimilado nuevos conocimientos en el Nexus)*"
        
        return ai_text

    def _call_ollama(self, prompt: str):
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
        with httpx.Client(timeout=120.0) as client:
            response = client.post(OLLAMA_URL, json=payload)
            if response.status_code != 200:
                return f"❌ Error de Ollama ({response.status_code})."
            return response.json().get('response', '')

    def _call_gemini(self, prompt: str):
        if not GEMINI_API_KEY:
            return "❌ Error: GEMINI_API_KEY no encontrada en .env"
        try:
            model = genai.GenerativeModel('gemini-1.5-flash') # Usamos flash para velocidad
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error de Gemini: {str(e)}"

    def generate_response(self, message: str, context: str = ""):
        # Recuperamos memoria del pasado
        past_memory = get_recent_insights()
        knowledge_graph = get_knowledge_graph()

        prompt = f"""
        {self.persona_prompt}
        
        MEMORIA RECIENTE:
        {past_memory if past_memory else "Sin aprendizajes previos."}
        
        NEXUS GRAPH (Conocimiento Estructurado):
        {knowledge_graph if knowledge_graph else "Grafo de conocimiento vacío."}
        
        CONTEXTO PROYECTO:
        {context}
        
        USUARIO: {message}
        """
        
        if self.provider == "gemini":
            ai_text = self._call_gemini(prompt)
        else:
            try:
                ai_text = self._call_ollama(prompt)
            except Exception as e:
                return f"❌ Error de Conexión Local: {str(e)}. Asegúrate de que Ollama esté corriendo."

        return self._process_ai_text(ai_text)

    def generate_refactor(self, instruction: str, file_path: str, content: str):
        prompt = f"""
        {self.persona_prompt}
        TAREA: Modifica el siguiente código siguiendo esta instrucción: "{instruction}"
        
        ARCHIVO: {file_path}
        CONTENIDO ORIGINAL:
        ```
        {content}
        ```
        
        INSTRUCCIONES DE SALIDA:
        1. Devuelve SOLO el código completo modificado.
        2. No incluyas explicaciones fuera del bloque de código.
        3. Si necesitas explicar algo, hazlo como comentarios en el código.
        4. No uses bloques de markdown, devuelve el texto plano del código.
        """
        
        if self.provider == "gemini":
            new_content = self._call_gemini(prompt)
        else:
            new_content = self._call_ollama(prompt)
        
        return new_content.strip() if new_content else None
