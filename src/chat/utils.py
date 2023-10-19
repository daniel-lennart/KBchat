from dotenv import load_dotenv
import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone

# Load environment variables from .env file
load_dotenv()

# Extract necessary environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = 'gcp-starter'
INDEX_NAME = 'langchain-retrieval-augmentation'

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Load Vector Database
def load_vectordb():
    embedding = OpenAIEmbeddings()  # Define the embeddings here
    index = pinecone.Index(index_name=INDEX_NAME)
    vectorstore = Pinecone(index, embedding.embed_query, text_key="text")
    return vectorstore

# Initialize the Chat Model
def init_chat_model(temperature=0, model_name='gpt-3.5-turbo'):
    return ChatOpenAI(temperature=temperature, model_name=model_name, api_key=OPENAI_API_KEY)

# Initialize the Retriever-QA Chain
def init_qa_chain(chat_model, vectordb, chain_type="stuff", k=2, return_source_documents=True):
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return RetrievalQA.from_chain_type(llm=chat_model, chain_type=chain_type, retriever=retriever, return_source_documents=return_source_documents)

# Generate a Reply
def generate_reply(qa_chain, query):
    return qa_chain(query)

# Cite Sources
def process_llm_response(llm_response):
    reply = llm_response['result']
    sources = [source.metadata['source'] for source in llm_response["source_documents"]]
    return reply, sources
