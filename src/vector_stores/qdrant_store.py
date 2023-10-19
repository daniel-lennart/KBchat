from langchain.vectorstores import Qdrant
from src.config import constants, settings

def create_qdrant_store(embeddings, texts, collection_name="KB_Test_Collection", force_recreate=False):
    """
    Create a Qdrant vector store using the provided embeddings.
    
    Parameters:
    - embeddings: The embeddings object to use for converting texts to vectors.
    - texts: A list of texts to embed and store in Qdrant.
    - collection_name: The name of the collection in Qdrant. Defaults to "KB_Collection".
    - force_recreate: Whether to recreate the Qdrant collection or not.
    
    Returns:
    - A Qdrant vector store.
    """
    return Qdrant.from_texts(
        texts=texts,
        embedding=embeddings,
        host=settings.QDRANT_HOST,
        api_key=settings.QDRANT_API_KEY,
        collection_name=collection_name,
        force_recreate=force_recreate
    )
