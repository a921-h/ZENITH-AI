#!/bin/bash
# install.sh
set -e

echo -e "\033[0;36m🏔️ ZENITH CLI: Starting installation for Unix-based system...\033[0m"

# 1. Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "\033[0;31m❌ Error: Python3 not found. Please install Python 3.10+\033[0m"
    exit 1
fi

# 2. Create Virtual Environment
echo -e "\033[0;32m📦 Creating virtual environment...\033[0m"
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Dependencies and Package
echo -e "\033[0;32m📚 Installing Zenith CLI package...\033[0m"
pip install --upgrade pip
pip install -e .

# 4. Create ZENITH Model
if command -v ollama &> /dev/null; then
    echo -e "\033[0;32m🧠 Building Zenith Engine in Ollama...\033[0m"
    ollama create zenith -f zenith.modelfile
else
    echo -e "\033[0;33m⚠️ Warning: Ollama not found. Local engine requires Ollama.\033[0m"
fi

echo -e "\n\033[0;36m✨ ZENITH CLI installed successfully!\033[0m"
echo -e "To start, run: \033[0;32mzenith ignite\033[0m"
