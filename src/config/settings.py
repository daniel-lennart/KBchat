# src/config/settings.py

from decouple import config

# OpenAI API Key
OPENAI_API_KEY = config('OPENAI_API_KEY', default='')

# Qdrant API Key and Host
QDRANT_API_KEY = config('QDRANT_API_KEY', default='')
QDRANT_HOST = config('QDRANT_HOST', default='')

# Embedding Model Name
EMBEDDING_MODEL_NAME = config('EMBEDDING_MODEL_NAME', default='sentence-transformers/all-mpnet-base-v2')

