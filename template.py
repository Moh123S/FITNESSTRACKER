import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'fitnesstracker'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"data/__init__.py",
    f"data/external",
    f"data/interim",
    f"data/processed",
    f"data/raw",
    f"docs/__init__.py",
    f"models/__init__.py",
    f"notebooks/__init__.py",
    f"references",
    f"reports/figures/__init__.py",
    f"src/data/__init__.py",
    f"src/features/__init__.py",
    f"src/models/__init__.py",
    f"src/visualization/__init__.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "requirements.txt"


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