import os
import sys
from src.data_processing.text_loader import load_texts_from_directory


def test_load_texts_from_directory():
    # Given: A sample directory with .txt files
    directory_path = "tests/sample_kb_articles"
    expected_filenames = ["sample1.txt", "sample2.txt"]
    
    # When: We load texts from the directory
    loaded_texts = load_texts_from_directory(directory_path)
    
    # Then: We should get the expected texts
    assert set(loaded_texts.keys()) == set(expected_filenames)
    assert loaded_texts["sample1.txt"] == "This is a sample text 1."
    assert loaded_texts["sample2.txt"] == "This is a sample text 2."
