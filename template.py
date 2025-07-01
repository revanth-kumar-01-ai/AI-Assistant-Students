import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ai_student_assistant"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/services/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/prompts/__init__.py",
    f"src/{project_name}/configs/__init__.py",
    f"src/{project_name}/configs/configuration.py",
    "tests/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "setup.py",
    "main.py",         
    ".env",
    "requirements.txt",
    "README.md",
    "research/trials.ipynb",
    "artifacts/.gitkeep"   
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} is already exists")