# Zenith AI CLI - Guía de Instalación

Bienvenido a la guía de instalación de Zenith AI CLI. Zenith está diseñado para ejecutarse de forma fluida en tu máquina local, conectándose a modelos de IA tanto locales como en la nube.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python**: `3.9` o superior.
- **Git**: Para clonar el repositorio.
- **Ollama** (Opcional pero Recomendado): Para ejecutar modelos localmente con latencia cero y 100% de privacidad. Descárgalo desde [ollama.com](https://ollama.com/).
- **API Key de Google AI Studio** (Opcional): Si planeas usar Gemini 1.5 para razonamiento complejo y contextos masivos. Obtenla en [aistudio.google.com](https://aistudio.google.com/).

## Pasos de Instalación

### 1. Clonar el Repositorio
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/a921-h/ZENITH-AI.git
cd ZENITH-AI
```

### 2. Configurar un Entorno Virtual (Recomendado)
Esto aísla las dependencias de Zenith del Python de tu sistema.
```bash
python -m venv venv

# Activar en Windows:
.\venv\Scripts\activate

# Activar en macOS / Linux:
source venv/bin/activate
```

### 3. Instalar Zenith
Puedes instalar Zenith y todas sus dependencias usando el script incluido o directamente vía pip.

**Usando el script de instalación (Instala dependencias y configura el modelo Ollama):**
- **Windows (PowerShell):** `./install.ps1`
- **macOS/Linux:** `chmod +x install.sh && ./install.sh`

**Instalación Manual (Modo editable para desarrollo):**
```bash
pip install -e .[all]
```

### 4. Configuración
Crea un archivo `.env` en la raíz del proyecto para personalizar tu motor de IA.
```env
# Elige tu motor: 'ollama' o 'gemini'
AI_PROVIDER=ollama

# Si usas Ollama:
MODEL_NAME=zenith

# Si usas Gemini (Nube):
GEMINI_API_KEY=tu_api_key_aqui
```

### 5. Verificar Instalación
Ejecuta el siguiente comando para asegurarte de que Zenith está instalado correctamente:
```bash
zenith --help
```
Deberías ver el menú de ayuda del CLI de Zenith.

## Próximos Pasos
Ahora que Zenith está instalado, es momento de mapear tu proyecto. Ejecuta `zenith ignite` en la raíz de cualquier base de código para construir el Nexus Graph.
