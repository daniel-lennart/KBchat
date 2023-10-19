import sys
import os
import unittest
from src.embeddings.huggingface_embeddings import create_huggingface_embeddings
from src.config import constants, settings

class TestHuggingFaceEmbeddings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.embeddings = create_huggingface_embeddings()

    def test_embeddings_for_multiple_texts(self):
        texts = ["This is a sample text.", "Another sample text."]
        embedding_vectors = self.embeddings.embed_documents(texts)
        # Assuming embeddings return a list of lists (one for each text)
        self.assertEqual(len(embedding_vectors), 2)

    def test_embeddings_for_single_text(self):
        text = "This is a sample text."
        embedding_vector = self.embeddings.embed_query(text)
        # Assuming embeddings return a list of floats
        self.assertTrue(isinstance(embedding_vector, list))
        self.assertTrue(all(isinstance(val, float) for val in embedding_vector))

    def test_embeddings_for_edge_cases(self):
        # Very long text
        long_text = "a" * 5000
        embedding_vector = self.embeddings.embed_query(long_text)
        self.assertTrue(isinstance(embedding_vector, list))

        # Text with special characters
        special_text = "Text with special characters !@#$%^&*()_+-=[]{}|;:,.<>/?"
        embedding_vector_special = self.embeddings.embed_query(special_text)
        self.assertTrue(isinstance(embedding_vector_special, list))

if __name__ == "__main__":
    unittest.main()
