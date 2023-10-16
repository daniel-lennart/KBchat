import streamlit as st
import utils  # Importing the utils.py file
import prepare_kb  # If needed, for re-loading and processing the Knowledge Base

# Load Vector DB and initialize chat model and QA chain
vectordb = utils.load_vectordb()
chat_model = utils.init_chat_model()
qa_chain = utils.init_qa_chain(chat_model, vectordb)

# Main layout
st.title("Support Chat Interface")
st.sidebar.title("Additional Information")
st.sidebar.info("Here you'll see source info related to the AI's responses.")
st.sidebar.header("Example Queries:")
st.sidebar.text("1. How do I enable regular cleaning in Microsoft Edge?\n"
                "2. How do I access privacy settings in Microsoft Edge?\n"
                "3. Which browser should I use for Amazon Connect?\n"
                "4. How do I collect CCP logs in Amazon Connect?\n"
                "5. What tools do I need to investigate issues in Amazon Connect?\n"
                "6. How to install PowerBI Desktop?\n"
                )

# Chat Window
user_input = st.text_input("Ask me something...")
if st.button("Send"):
    st.write("You:", user_input)
    
    # Get AI's response using the query and the initialized QA chain
    llm_response = utils.generate_reply(qa_chain, user_input)
    
    # Process the response to extract reply and source information
    reply, sources = utils.process_llm_response(llm_response)
    
    # Display AI's response and source info in the chat window and sidebar respectively
    st.write("AI:", reply)
    st.sidebar.write("Sources:", ", ".join(sources))

# Reload Database Button
if st.sidebar.button("Reload Knowledge Base"):
    st.sidebar.success("Reloading the Knowledge Base...")
    prepare_kb.load_and_process_kb()  # Function from prepare_kb.py that processes and saves the KB to a vector DB.
    st.sidebar.success("Knowledge Base Reloaded Successfully!")

