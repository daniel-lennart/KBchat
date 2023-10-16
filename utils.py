import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Ensure OPENAI_API_KEY is set as an environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables.")

# Global Config
PERSIST_DIR = 'db'

# Load Vector Database
def load_vectordb(persist_directory=PERSIST_DIR):
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, 
                      embedding_function=embedding)
    return vectordb

# Initialize the Chat Model
def init_chat_model(temperature=0, model_name='gpt-3.5-turbo'):
    return ChatOpenAI(temperature=temperature, model_name=model_name, api_key=OPENAI_API_KEY)

# Initialize the Retriever-QA Chain
def init_qa_chain(chat_model, vectordb, chain_type="stuff", k=2, return_source_documents=True):
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return RetrievalQA.from_chain_type(llm=chat_model, 
                                       chain_type=chain_type, 
                                       retriever=retriever, 
                                       return_source_documents=return_source_documents)

# Generate a Reply
def generate_reply(qa_chain, query):
    return qa_chain(query)

# Cite Sources
def process_llm_response(llm_response):
    reply = llm_response['result']
    sources = [source.metadata['source'] for source in llm_response["source_documents"]]
    return reply, sources
