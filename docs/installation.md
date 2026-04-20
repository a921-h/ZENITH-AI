# Zenith AI CLI - Installation Guide

Welcome to the Zenith AI CLI installation guide. Zenith is designed to run seamlessly on your local machine, connecting to either local or cloud AI models.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: `3.9` or higher.
- **Git**: For cloning the repository.
- **Ollama** (Optional but Recommended): For running models locally with zero latency and 100% privacy. Download from [ollama.com](https://ollama.com/).
- **Google AI Studio API Key** (Optional): If you plan to use Gemini 1.5 for complex reasoning and large context windows. Get it from [aistudio.google.com](https://aistudio.google.com/).

## Installation Steps

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/a921-h/ZENITH-AI.git
cd ZENITH-AI
```

### 2. Set Up a Virtual Environment (Recommended)
This isolates the dependencies of Zenith from your system Python.
```bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on macOS / Linux:
source venv/bin/activate
```

### 3. Install Zenith
You can install Zenith and all its dependencies using the included script or directly via pip.

**Using the installation script (Installs dependencies and sets up Ollama model):**
- **Windows (PowerShell):** `./install.ps1`
- **macOS/Linux:** `chmod +x install.sh && ./install.sh`

**Manual Installation (Editable mode for development):**
```bash
pip install -e .[all]
```

### 4. Configuration
Create a `.env` file in the root of the project to customize your engine.
```env
# Choose your engine: 'ollama' or 'gemini'
AI_PROVIDER=ollama

# If using Ollama:
MODEL_NAME=zenith

# If using Gemini (Cloud):
GEMINI_API_KEY=your_api_key_here
```

### 5. Verify Installation
Run the following command to ensure Zenith is correctly installed:
```bash
zenith --help
```
You should see the Zenith CLI help menu.

## Next Steps
Now that Zenith is installed, it's time to map your project. Run `zenith ignite` in the root of any codebase to build the Nexus Graph.
