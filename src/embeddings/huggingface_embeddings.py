from langchain.embeddings import HuggingFaceEmbeddings
from src.config import constants, settings

def create_huggingface_embeddings():
    """
    Create HuggingFace embeddings based on the pre-defined model.
    
    Returns:
    - A HuggingFace embeddings object.
    """
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL_NAME
    )
