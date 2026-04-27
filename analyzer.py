import os
from git import Repo
from pathlib import Path
import ast

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

