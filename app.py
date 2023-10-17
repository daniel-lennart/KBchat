import streamlit as st
import utils
import prepare_kb
import documentation


# Load Vector DB and initialize chat model and QA chain
vectordb = utils.load_vectordb()
chat_model = utils.init_chat_model()
qa_chain = utils.init_qa_chain(chat_model, vectordb)

# Main layout
st.title("Support Chat Interface")

# Sidebar content
# Link to docs
if st.sidebar.button("How does this work?"):
    documentation.show_documentation()
# Custom Reload Database Button in sidebar with distinct color


st.sidebar.title("Example queries:")

example_queries = [
    "how to install PowerBI?",
    "Where to download PowerBI?",
    "Where to get CCP logs?",
    "Where to get SAP logs?",
    "How to login to Amazon Connect?",
    "What KB articles do you suggest for investigating login issues with Amazon Connect?"
]

# Check if a query is selected using session state
if 'selected_query' not in st.session_state:
    st.session_state.selected_query = None

for query in example_queries:
    if st.sidebar.button(query):
        st.session_state.selected_query = query

# Display the selected query in the chat input field
user_input = st.text_input("Ask me something...", value=st.session_state.selected_query if st.session_state.selected_query else "")

if st.button("Send"):
    st.write("You:", user_input)
    
    # Get AI's response using the query and the initialized QA chain
    llm_response = utils.generate_reply(qa_chain, user_input)
    
    # Process the response to extract reply and source summaries
    reply, sources = utils.process_llm_response(llm_response)
    
    # Display AI's response
    st.write("AI:", reply)
    
    # Display the source info in the sidebar's info block
    source_info = f"Sources: {', '.join(sources)}"
    st.sidebar.info(source_info)
    
    # Reset the selected query after sending
    st.session_state.selected_query = None

st.sidebar.title("Only use this if KB has been updated!")


# Reload Database Button
if st.sidebar.button("Reload Knowledge Base"):
    st.sidebar.success("Reloading the Knowledge Base...")
    prepare_kb.load_and_process_kb()  # Function from prepare_kb.py that processes and saves the KB to a vector DB.
    st.sidebar.success("Knowledge Base Reloaded Successfully!")