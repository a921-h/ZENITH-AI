# 🤝 Contributing to ZENITH AI
### *Architecting the Future of Terminal Intelligence*

[Leer en Español 🇪🇸](CONTRIBUTING.es.md)

First of all, thank you for considering contributing to **ZENITH**! 🏔️

ZENITH is an open-source autonomous agent built for high-performance engineering. We value clean code, deep architectural thinking, and pragmatic technical leadership. By contributing, you're helping build the premier local-first AI workspace for developers.

---

## 🏗️ Why Contribute to Zenith?

*   **Innovate on the Edge**: Work with cutting-edge **Hybrid AI** (Ollama + Gemini).
*   **Master Memory Systems**: Contribute to the **Nexus Graph**, our unique logic-aware knowledge system.
*   **Build Premium Tooling**: Help refine a CLI experience that rivals professional IDEs.
*   **Community & Growth**: Join a project focused on "Staff Engineer" level standards.

---

## 🛠️ Development Setup

To start developing on Zenith, follow these steps:

1.  **Fork & Clone**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ZENITH-AI-CLI.git
    cd ZENITH-AI-CLI
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install in Editable Mode**:
    This allows you to test changes to the `zenith` command instantly.
    ```bash
    pip install -e .[all]
    ```

4.  **Configure Environment**:
    Copy the template and add your keys (if using Gemini).
    ```bash
    cp .env.example .env  # If example exists, or create one
    ```

---

## 🚀 Contribution Workflow

### 1. Find an Issue
Look for issues labeled `good-first-issue` or `help-wanted`. If you have a new idea, **open an issue first** to discuss the architectural approach.

### 2. Branching Strategy
We use a simple branching model:
*   `feat/...` for new features.
*   `fix/...` for bug fixes.
*   `docs/...` for documentation improvements.

### 3. Coding Standards
*   **Type Safety**: All functions must have Python type hints.
*   **Clean Code**: We follow PEP 8. Use `black` or `ruff` for formatting.
*   **Path Security**: Never perform file I/O without using the internal `path_sanitizer`.
*   **Nexus Alignment**: Ensure new logic respects the "Nexus Graph" memory philosophy.

---

## 🌈 Focus Areas

| Area | Description |
| :--- | :--- |
| **🧠 Brain Engine** | Optimizing prompts and LLM provider logic (Gemma, Gemini, Claude). |
| **📁 Nexus Graph** | Improving entity extraction, relationship mapping, and vector search. |
| **🎨 Terminal UI** | Enhancing the `rich` dashboard and interactive commands. |
| **🛡️ Security** | Auditing path-sanitization and adding secure-by-default features. |

---

## ✅ Pull Request Checklist

Before submitting your PR, ensure:
- [ ] Your code is properly typed and formatted.
- [ ] You have tested the changes using the `zenith` CLI locally.
- [ ] The `README.md` or `guide` command is updated if necessary.
- [ ] Your commit messages are descriptive (following Conventional Commits is a plus).

---

## 📬 Communication
We love technical deep-dives! Join the discussion in our **GitHub Issues** or **Discussions** tab.

**Let's reach the peak together. Zenith Team.**
