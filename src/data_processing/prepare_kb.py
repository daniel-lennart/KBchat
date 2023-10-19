import os
import pinecone
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader

# Load environment variables from .env file
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not set in .env or environment variables.")

INDEX_NAME = 'langchain-retrieval-augmentation'

def load_and_process_kb():
    """
    Load KB articles, process them, convert them into a vector DB,
    and save them to Pinecone.
    """
    
    # Initialize Pinecone
    pinecone.init(api_key=PINECONE_API_KEY, environment="gcp-starter")
    
    # Check if the index exists and create if not
    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(name=INDEX_NAME, metric='dotproduct', dimension=1536)  # Assuming embedding dimension is 1536
    
    # Use Pinecone's indexer
    indexer = pinecone.Index(index_name=INDEX_NAME)

    # Load and process the text files
    loader = DirectoryLoader('./src/kb_articles/', glob="./*.txt", loader_cls=TextLoader)
    documents = loader.load()
    
    # Splitting the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = {doc.metadata['source']: text_splitter.split_text(doc.page_content) for doc in documents}  # Using 'content' attribute

    # Embed the texts
    embedding = OpenAIEmbeddings()
    print("Methods of OpenAIEmbeddings:", dir(embedding))
    vectors = {doc_id: embedding.embed_query(text) for doc_id, text in texts.items()}

    
    # Upsert vectors to Pinecone
    indexer.upsert(vectors)
