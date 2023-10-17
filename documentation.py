import streamlit as st

def show_documentation():
    st.title("Understanding the Support Chat Interface Demo")

    st.write("""
    Welcome to our Support Chat Interface demo! This system is designed to provide quick and accurate answers to your queries by harnessing the power of artificial intelligence. But how does it work? Let's break it down.
    """)

    st.header("1. Loading Knowledge into a Vector Database:")
    st.write("""
    - We start by taking a set of text files containing knowledge, think of them as our digital books.
    - These files are transformed into a format (vectors) that computers find easy to compare and search, creating a "Vector Database".
    """)

    st.header("2. User Interaction:")
    st.write("""
    - When you type a question into the chat, our system tries to find the most relevant information from our digital books.
    - It does this by comparing your question (also transformed into a vector) with the Vector Database.
    """)

    st.header("3. Generating Conversational Replies:")
    st.write("""
    - Once the system identifies relevant information, it doesn't just throw it at you.
    - Instead, it uses a Language Model to craft a conversational reply. This makes the interaction feel more like talking to a human assistant than querying a database.
    """)

    st.header("4. Summarizing Knowledge:")
    st.write("""
    - Often, our digital books contain a lot more information than you might need.
    - The system is designed to sift through all that information and present only the bits that answer your question. Think of it as an expert skimming through a book and highlighting the important parts for you.
    """)

    st.header("Why is this useful for business?")
    st.write("""
    This approach means faster, more accurate support for users. Instead of trawling through long articles or FAQs, users get precise answers instantly. It reduces the time spent searching for information and increases user satisfaction.
    """)

    if st.button('Go Back to Demo'):
        st.write('Redirecting to main demo...')  # Here you would redirect to the main demo.

if __name__ == "__main__":
    show_documentation()
