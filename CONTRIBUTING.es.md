# 🤝 Contribuyendo a ZENITH AI
### *Arquitectando el Futuro de la Inteligencia en Terminal*

¡Antes que nada, gracias por considerar contribuir a **ZENITH**! 🏔️

ZENITH es un agente autónomo de código abierto diseñado para ingeniería de alto rendimiento. Valoramos el código limpio, el pensamiento arquitectónico profundo y el liderazgo técnico pragmático. Al contribuir, estás ayudando a construir el espacio de trabajo de IA local-first definitivo para desarrolladores.

---

## 🏗️ ¿Por qué contribuir a Zenith?

*   **Innova en la Vanguardia**: Trabaja con **IA Híbrida** de última generación (Ollama + Gemini).
*   **Domina Sistemas de Memoria**: Contribuye al **Nexus Graph**, nuestro sistema de conocimiento consciente de la lógica del código.
*   **Construye Herramientas Premium**: Ayuda a refinar una experiencia CLI que rivaliza con IDEs profesionales.
*   **Comunidad y Crecimiento**: Únete a un proyecto enfocado en estándares de nivel "Staff Engineer".

---

## 🛠️ Configuración de Desarrollo

Para comenzar a desarrollar en Zenith, sigue estos pasos:

1.  **Fork y Clonar**:
    ```bash
    git clone https://github.com/TU_USUARIO/ZENITH-AI-CLI.git
    cd ZENITH-AI-CLI
    ```

2.  **Crear un Entorno Virtual**:
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar en Modo Editable**:
    Esto te permite probar los cambios en el comando `zenith` instantáneamente.
    ```bash
    pip install -e .[all]
    ```

4.  **Configurar el Entorno**:
    Copia la plantilla y añade tus claves (si usas Gemini).
    ```bash
    cp .env.example .env  # Si existe, o créalo manualmente
    ```

---

## 🚀 Flujo de Trabajo de Contribución

### 1. Encuentra un Issue
Busca issues etiquetados como `good-first-issue` o `help-wanted`. Si tienes una idea nueva, **abre un issue primero** para discutir el enfoque arquitectónico.

### 2. Estrategia de Ramas
Usamos un modelo de ramas simple:
*   `feat/...` para nuevas funcionalidades.
*   `fix/...` para corrección de errores.
*   `docs/...` para mejoras en la documentación.

### 3. Estándares de Código
*   **Tipado Estático**: Todas las funciones deben tener Type Hints de Python.
*   **Código Limpio**: Seguimos PEP 8. Usa `black` o `ruff` para el formateo.
*   **Seguridad de Rutas**: Nunca realices operaciones de E/S de archivos sin usar el `path_sanitizer` interno.
*   **Alineación con Nexus**: Asegúrate de que la nueva lógica respete la filosofía de memoria del "Nexus Graph".

---

## 🌈 Áreas de Enfoque

| Área | Descripción |
| :--- | :--- |
| **🧠 Motor Cerebral** | Optimización de prompts y lógica de proveedores de LLM (Gemma, Gemini, Claude). |
| **📁 Nexus Graph** | Mejora de extracción de entidades, mapeo de relaciones y búsqueda vectorial. |
| **🎨 Interfaz CLI** | Mejora del dashboard con `rich` y comandos interactivos. |
| **🛡️ Seguridad** | Auditoría de sanitización de rutas y adición de funciones seguras por defecto. |

---

## ✅ Checklist para Pull Requests

Antes de enviar tu PR, asegúrate de:
- [ ] Tu código está correctamente tipado y formateado.
- [ ] Has probado los cambios usando el CLI `zenith` localmente.
- [ ] El `README.md` o el comando `guide` están actualizados si es necesario.
- [ ] Tus mensajes de commit son descriptivos (usar Conventional Commits es un plus).

---

## 📬 Comunicación
¡Nos encantan las discusiones técnicas profundas! Únete a la conversación en nuestras **GitHub Issues** o en la pestaña de **Discussions**.

**Alcancemos la cima juntos. El Equipo de Zenith.**
