# zenith/cli.py
import typer
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.status import Status
from rich.align import Align
from zenith.brain import Brain
from zenith.memory import get_recent_insights, get_knowledge_graph
from typing import List, Optional
from pathlib import Path

app = typer.Typer(help="🏔️ ZENITH AI CLI", no_args_is_help=False)
console = Console()

LOGO = r"""
[bold cyan]
  ______ ______ _   _ _____ _______ _    _ 
 |___  /|  ____| \ | |_   _|__   __| |  | |
    / / | |__  |  \| | | |    | |  | |__| |
   / /  |  __| | . ` | | |    | |  |  __  |
  / /__ | |____| |\  |_| |_   | |  | |  | |
 /_____||______|_| \_|_____|  |_|  |_|  |_|
[/bold cyan]
[dim italic]     The Peak of Autonomous Intelligence[/dim italic]
"""

def welcome():
    """Muestra una pantalla de bienvenida premium."""
    console.clear()
    banner = Panel(
        Align.center(
            Text.from_markup(
                "[bold cyan]🏔️ ZENITH AI CLI[/bold cyan]\n"
                "[dim white]The Peak of Autonomous Intelligence[/dim white]\n\n"
                "[italic green]\"Transformando código en arquitectura de élite\"[/italic green]"
            )
        ),
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(banner)

def interactive_menu():
    """Menú interactivo de inicio."""
    welcome()
    
    table = Table.grid(padding=(0, 1))
    table.add_column(style="cyan", justify="right")
    table.add_column(style="white")
    
    options = [
        ("1", "🔥 Ignite - Escanear proyecto"),
        ("2", "💬 Ask - Consulta técnica"),
        ("3", "🧠 Nexus - Memoria y Grafo"),
        ("4", "🛠️ Refactor - Mejorar código"),
        ("5", "❓ Help - Guía de comandos"),
        ("0", "❌ Exit - Salir")
    ]
    
    menu_panel = Panel(
        Align.center("\n".join([f"[bold cyan]{opt[0]}[/bold cyan]  {opt[1]}" for opt in options])),
        title="[bold white]DASHBOARD PRINCIPAL[/bold white]",
        border_style="blue",
        width=50
    )
    
    console.print(Align.center(menu_panel))
    
    choice = console.input("\n[bold yellow]❯ Selecciona una opción:[/bold yellow] ")
    
    if choice == "1":
        ignite()
    elif choice == "2":
        msg = console.input("[bold cyan]❯ Tu consulta:[/bold cyan] ")
        ask(message=msg)
    elif choice == "3":
        nexus()
    elif choice == "4":
        file = console.input("[bold cyan]❯ Archivo:[/bold cyan] ")
        inst = console.input("[bold cyan]❯ Instrucción:[/bold cyan] ")
        refactor(file_path=file, instruction=inst)
    elif choice == "5":
        guide()
    elif choice == "0":
        console.print("[italic blue]Cerrando conexión con Zenith... Hasta pronto.[/italic blue]")
        return
    else:
        console.print("[bold red]Opción no válida.[/bold red]")
        interactive_menu()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Punto de entrada principal."""
    if ctx.invoked_subcommand is None:
        interactive_menu()

@app.command()
def guide():
    """❓ Muestra la guía detallada de comandos y uso."""
    welcome()
    help_text = """
### 🚀 Comandos Disponibles

| Comando | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `ignite` | Escaneo profundo y aprendizaje de arquitectura | `zenith ignite` |
| `ask` | Consulta técnica con contexto de archivos | `zenith ask "Optimiza esto" -f main.py` |
| `nexus` | Accede a la memoria y grafo de relaciones | `zenith nexus` |
| `refactor`| Aplica cambios seguros al código | `zenith refactor main.py "Extract logic"` |
| `guide` | Esta guía de ayuda | `zenith guide` |

### 💡 Tips Pro
- Usa `--file` o `-f` múltiples veces para inyectar varios archivos.
- El Nexus aprende de tus interacciones: `[LEARN: ...]`.
- Prueba diferentes personas con `-p`: `architect`, `security`, `reviewer`.
    """
    console.print(Panel(Markdown(help_text), title="[bold white]GUÍA DE USUARIO ZENITH[/bold white]", border_style="green"))

def is_safe_path(path: Path) -> bool:
    """Verifica que la ruta esté dentro del directorio del proyecto para evitar escape."""
    try:
        root = Path(".").absolute()
        target = path.absolute()
        return root in target.parents or root == target
    except Exception:
        return False

def get_project_files(root: Path) -> List[Path]:
    """Escanea archivos ignorando directorios comunes."""
    ignore_dirs = {".git", "node_modules", ".venv", "__pycache__", ".pytest_cache", ".vscode"}
    files = []
    for path in root.rglob("*"):
        if any(part in ignore_dirs for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files

@app.command()
def ask(
    message: str = typer.Argument(..., help="Consulta técnica para Zenith"),
    files: Optional[List[str]] = typer.Option(None, "--file", "-f", help="Archivo(s) de contexto"),
    persona: str = typer.Option("staff", "--persona", "-p", help="Persona: staff, security, architect, reviewer")
):
    """💬 Inicia una sesión de consulta con la inteligencia ZENITH."""
    welcome()
    brain = Brain(persona=persona)
    
    combined_context = ""
    if files:
        for file_path in files:
            path = Path(file_path)
            if not is_safe_path(path):
                console.print(f"[bold red]❌ Error de Seguridad:[/bold red] La ruta '{file_path}' está fuera del proyecto.")
                return
            
            if path.exists():
                if path.is_file():
                    try:
                        content = path.read_text(encoding="utf-8")
                        combined_context += f"\n--- CONTEXTO [{file_path}] ---\n{content}\n"
                    except Exception as e:
                        console.print(f"[bold yellow]⚠️ Advertencia:[/bold yellow] No se pudo leer '{file_path}': {e}")
                elif path.is_dir():
                    console.print(f"[dim]📂 Escaneando directorio: {file_path}[/dim]")
                    for subfile in get_project_files(path):
                        try:
                            content = subfile.read_text(encoding="utf-8")
                            combined_context += f"\n--- CONTEXTO [{subfile}] ---\n{content}\n"
                        except Exception:
                            pass
            else:
                console.print(f"[bold red]❌ Error:[/bold red] Ruta '{file_path}' no encontrada.")
                return

    with console.status("[bold cyan]Sincronizando con Zenith Engine...", spinner="aesthetic"):
        response = brain.generate_response(message, context=combined_context)
    
    console.print(Panel(
        Markdown(response),
        title=f"[bold white]📡 RESPUESTA DEL SISTEMA[/bold white]",
        subtitle=f"[dim]Persona: {persona} | Contexto: {', '.join(files) if files else 'Global'}[/dim]",
        border_style="cyan",
        padding=(1, 2)
    ))

@app.command()
def nexus():
    """🧠 Accede a la memoria colectiva y aprendizajes de Zenith."""
    welcome()
    insights = get_recent_insights(limit=10)
    
    table = Table(title="[bold magenta]ZENITH NEXUS - Historial de Aprendizaje[/bold magenta]", border_style="magenta")
    table.add_column("ID", style="dim")
    table.add_column("Conocimiento Asimilado", style="white")
    
    if not insights:
        table.add_row("-", "La memoria está vacía. Comienza a preguntar para aprender.")
    else:
        for i, line in enumerate(insights.split("\n")):
            if line.strip():
                table.add_row(str(i+1), line.replace("- ", ""))
            
    console.print(table)

    # Mostrar Grafo de Conocimiento
    graph = get_knowledge_graph()
    if graph:
        graph_table = Table(title="[bold cyan]ZENITH NEXUS - Grafo de Relaciones[/bold cyan]", border_style="cyan")
        graph_table.add_column("Relación", style="white")
        for line in graph.split("\n"):
            if line.strip():
                graph_table.add_row(line.replace("- ", ""))
        console.print(graph_table)

@app.command()
def ignite():
    """🔥 Escaneo profundo del entorno actual."""
    welcome()
    with console.status("[bold green]Escaneando arquitectura del proyecto..."):
        root = Path(".")
        project_files = get_project_files(root)
        
        # Agrupar por extensión para el resumen
        extensions = {}
        for f in project_files:
            ext = f.suffix or "sin extensión"
            extensions[ext] = extensions.get(ext, 0) + 1

        summary = Table(show_header=False, border_style="green")
        summary.add_row("[bold green]Entorno:[/bold green]", str(root.absolute()))
        summary.add_row("[bold green]Total Archivos:[/bold green]", str(len(project_files)))
        
        ext_summary = ", ".join([f"{ext}: {count}" for ext, count in extensions.items()])
        summary.add_row("[bold green]Distribución:[/bold green]", ext_summary[:100] + ("..." if len(ext_summary) > 100 else ""))
        summary.add_row("[bold green]Estado Engine:[/bold green]", "[bold cyan]ONLINE[/bold cyan]")
        
        console.print(Panel(summary, title="[bold green]SISTEMA IGNICIONADO", border_style="green"))
        
        # Escaneo profundo: Enviar estructura al Brain para mapear el Nexus
        console.print("[dim]🚀 Iniciando Análisis de Arquitectura Autónomo...[/dim]")
        brain = Brain(persona="architect")
        structure_desc = "\n".join([str(f) for f in project_files[:50]]) # Limitamos a 50 para el prompt
        if len(project_files) > 50:
            structure_desc += "\n... (y más archivos)"
            
        ignite_msg = f"Analiza la estructura de este proyecto y genera entidades y relaciones para tu Nexus. Archivos: {structure_desc}"
        brain.generate_response(ignite_msg)
        console.print("[bold green]✅ Nexus actualizado con la arquitectura del proyecto.[/bold green]")

@app.command()
def refactor(
    file_path: str = typer.Argument(..., help="Archivo a refactorizar"),
    instruction: str = typer.Argument(..., help="Instrucciones para el refactor"),
    persona: str = typer.Option("staff", "--persona", "-p", help="Persona: staff, security, architect, reviewer")
):
    """🛠️ Aplica cambios automáticos y seguros al código."""
    welcome()
    brain = Brain(persona=persona)
    path = Path(file_path)
    
    if not is_safe_path(path):
        console.print(f"[bold red]❌ Error de Seguridad:[/bold red] Acceso denegado a '{file_path}'. Solo puedes modificar archivos dentro del proyecto.")
        return

    if not path.exists():
        console.print(f"[bold red]❌ Error:[/bold red] Archivo '{file_path}' no encontrado.")
        return

    content = path.read_text(encoding="utf-8")
    
    with console.status(f"[bold cyan]Zenith está rediseñando {file_path}...", spinner="bouncingBar"):
        new_content = brain.generate_refactor(instruction, file_path, content)
    
    if not new_content:
        console.print("[bold red]❌ Error:[/bold red] Zenith no pudo generar el refactor.")
        return

    # Limpiar posibles bloques de markdown que el modelo a veces cuela
    if new_content.startswith("```"):
        lines = new_content.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        new_content = "\n".join(lines).strip()

    # Mostrar Diff
    import difflib
    diff = difflib.unified_diff(
        content.splitlines(),
        new_content.splitlines(),
        fromfile=f"a/{file_path}",
        tofile=f"b/{file_path}",
        lineterm=""
    )
    
    diff_text = "\n".join(diff)
    if not diff_text:
        console.print("[bold yellow]ℹ️ No hay cambios sugeridos.[/bold yellow]")
        return

    console.print(Panel(Markdown(f"```diff\n{diff_text}\n```"), title="[bold yellow]CAMBIOS PROPUESTOS", border_style="yellow"))
    
    confirm = typer.confirm("¿Deseas aplicar estos cambios?")
    if confirm:
        path.write_text(new_content, encoding="utf-8")
        console.print(f"[bold green]✅ {file_path} ha sido actualizado con éxito.[/bold green]")
    else:
        console.print("[bold white]Refactor cancelado por el usuario.[/bold white]")

if __name__ == "__main__":
    app()
