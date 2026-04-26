import os
from git import Repo
from pathlib import Path

def get_python_files(repo_path: str):
    try:
        Repo(repo_path)
    except Exception:
        print("Not a valid git repository!")
        return []
    
    path = Path(repo_path)
    return list(path.rglob("*.py"))

