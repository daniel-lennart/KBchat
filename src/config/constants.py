# src/config/constants.py

# Index Name for Qdrant
INDEX_NAME = 'langchain-retrieval-augmentation'

# Constants for text splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Constants for embeddings
EMBEDDING_DIMENSION = 768  # This might need adjustment based on the specific HuggingFace model used

# Path to KB articles
KB_ARTICLES_PATH = './src/kb_articles/'

# Glob pattern for loading KB articles
KB_ARTICLES_GLOB = "./*.txt"

# Model name for HuggingFace embeddings
HF_EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
