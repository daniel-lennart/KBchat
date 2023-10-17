from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader

# You'll have to add the relevant code here to load and process your KB articles,
# convert them into a vector DB, and save them to disk.

def load_and_process_kb():
    """
    Load KB articles, process them, convert them into a vector DB,
    and save them to disk.
    """
    # Load and process the text files
    loader = DirectoryLoader('kb_articles/', glob="./*.txt", loader_cls=TextLoader)
    documents = loader.load()
    
    # Splitting the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    # Embed and store the texts
    persist_directory = 'db'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, 
                                     embedding=embedding,
                                     persist_directory=persist_directory)
    # Persist the db to disk
    vectordb.persist()
