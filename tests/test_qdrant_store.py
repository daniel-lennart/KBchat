import unittest
from src.config import constants, settings
from src.vector_stores.qdrant_store import create_qdrant_store
from src.embeddings.huggingface_embeddings import create_huggingface_embeddings

class TestQdrantStore(unittest.TestCase):

    def setUp(self):
        self.embeddings = create_huggingface_embeddings()
        self.sample_texts = ["This is a sample text.", "Another example text.", "Yet another text."]
        self.qdrant_store = create_qdrant_store(self.embeddings, self.sample_texts, collection_name="KB_Test_Collection", force_recreate=True)

    def test_connection_to_qdrant(self):
        # Simply test if the Qdrant store has been created
        self.assertIsNotNone(self.qdrant_store)

    def test_store_and_retrieve_vectors(self):
        query = "sample text"
        found_docs = self.qdrant_store.similarity_search(query)
        # Assert that we get results back
        self.assertTrue(len(found_docs) > 0)
        # Assert that the retrieved document matches one of our sample texts
        self.assertIn(found_docs[0].page_content, self.sample_texts)

    def test_store_and_retrieve_edge_cases(self):
        # Very large text
        large_text = " ".join(["sample"] * 10000)
        self.qdrant_store.insert_documents([large_text])
        found_docs = self.qdrant_store.similarity_search("sample")
        self.assertTrue(len(found_docs) > 0)

        # Very similar texts
        similar_texts = ["This is a text.", "This is a text!"]
        self.qdrant_store.insert_documents(similar_texts)
        found_docs = self.qdrant_store.similarity_search("This is a text.")
        self.assertTrue(len(found_docs) == 2)

if __name__ == "__main__":
    unittest.main()
