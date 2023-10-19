import os
from typing import List, Dict

def load_text_from_file(filepath: str) -> str:
    """
    Load content from a single text file.
    """
    with open(filepath, 'r') as f:
        return f.read()

def load_texts_from_directory(directory_path: str, file_extension=".txt") -> Dict[str, str]:
    """
    Load content from all text files in a directory.
    Returns a dictionary where the keys are filenames and the values are the content of the files.
    """
    texts = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory_path, filename)
            texts[filename] = load_text_from_file(filepath)
    return texts
