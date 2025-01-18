import streamlit as st
from upload import upload
from retrieve import retrieve
from qdrant_client import QdrantClient

# Qdrant configuration
url = ""
api_key = ""

# Initialize Qdrant client
client = QdrantClient(url=url, api_key=api_key)

# Set page config
st.set_page_config(page_title="Streamlit App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose an option:", ["Chat", "Documents"])

# Chat functionality
if option == "Chat":
    st.title("Chat Section")
    
    # Get list of collections
    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]
    
    # Display all collections
    st.write("Available collections:")
    for name in collection_names:
        st.write(f"- {name}")
    
    # Collection dropdown
    selected_collection = st.selectbox("Choose a collection:", collection_names)
    
    # Question input
    question = st.text_input("Enter your question:")
    
    # Limit slider
    limit = st.slider("Select number of chunks:", 1, 10, 3)
    
    if st.button("Enter"):
        if selected_collection and question:
            # Create a placeholder for streaming response
            response_placeholder = st.empty()
            full_response = ""
            
            # Get streaming response
            for chunk in retrieve(selected_collection, question, limit):
                full_response += chunk
                # Update placeholder with accumulated response
                response_placeholder.markdown(full_response + "▌")
            
            # Final update without cursor
            response_placeholder.markdown(full_response)

# Document upload functionality
elif option == "Documents":
    st.title("Document Section")
    st.write("Upload a new document below:")

    # Collection name input
    collection_name = st.text_input("Enter collection name:")

    # File uploader
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
    
    if uploaded_file is not None and collection_name:
        # Save uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Call upload function with file path and collection name
        upload(uploaded_file.name, collection_name)
        st.success("File uploaded successfully!")