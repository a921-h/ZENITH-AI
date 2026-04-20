# install.ps1
Write-Host "🏔️ ZENITH CLI: Starting installation for Windows..." -ForegroundColor Cyan

# 1. Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Error: Python not found. Please install Python 3.10+" -ForegroundColor Red
    exit
}

# 2. Check for Ollama
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️ Warning: Ollama not found. Local engine won't work until Ollama is installed." -ForegroundColor Yellow
}

# 3. Create Virtual Environment
Write-Host "📦 Creating virtual environment..." -ForegroundColor Green
python -m venv .venv
& .\.venv\Scripts\Activate.ps1

# 4. Install Dependencies and Package
Write-Host "📚 Installing Zenith CLI package..." -ForegroundColor Green
pip install -e .

# 5. Create ZENITH Model
if (Get-Command ollama -ErrorAction SilentlyContinue) {
    Write-Host "🧠 Building Zenith Engine in Ollama..." -ForegroundColor Green
    ollama create zenith -f zenith.modelfile
}

Write-Host "`n✨ ZENITH CLI installed successfully!" -ForegroundColor Cyan
Write-Host "To start, run: zenith ignite" -ForegroundColor Green
Write-Host "Try: zenith ask hola" -ForegroundColor Green
