import os
from git import Repo
from pathlib import Path
import ast
import google.generativeai as genai
import typer
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
import time

load_dotenv()

app = typer.Typer()
console = Console()

api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def get_python_files(repo_path: str):
    try:
        Repo(repo_path)
    except Exception:
        print("Not a valid git repository!")
        return []
    
    path = Path(repo_path)
    return list(path.rglob("*.py"))

def extract_functions_from_file(filepath: Path):
    with open(filepath, 'r', encoding='utf-8') as file:
        source_code = file.read()
    
    tree = ast.parse(source_code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_code = ast.get_source_segment(source_code, node)
            functions.append({
                "name": node.name,
                "code": func_code
            })
    return functions

def summarize_function(func_name: str, func_code:str) -> str:
    prompt = f"""
    You are an expert software engineer. Briefly summarize what this Python function does in 1-2 sentences.
    Fucntion name: {func_name}
    Code: {func_code}"""

    response = model.generate_content(prompt)
    return response.text.strip()

@app.command()

def analyze(repo_path: str = "."):
    console.print(f"[bold green]Analyzing repository:[/bold green] {repo_path}")

    files = get_python_files(repo_path)

    for file in files:
        funcs = extract_functions_from_file(file)
        if not funcs:
            continue

        console.print(f"\n[bold blue] File:[/bold blue] {file.name}")

        for f in funcs:
            summary  = summarize_function(f["name"], f["code"])
            console.print(Panel(summary, title=f["name"], border_style="cyan"))
            time.sleep(4)


if __name__ == "__main__":
    app()