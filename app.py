import streamlit as st
import os 
from utils.pdf_processor import PDFProcessor
from utils.chroma_manager import ChromaDBManager
from utils.llm_integration import GeminiLLM
import tempfile
from dotenv import load_dotenv

# load env variable
load_dotenv()

# configure page
st.set_page_config(
    page_title="PDF Book Reader",
    page_icon="📚",
    layout="wide"
)

# initialize session state
if 'chroma_db' not in st.session_state:
    st.session_state.chroma_db = None
if 'pdf_processor' not in st.session_state:
    st.session_state.pdf_processor = PDFProcessor()
if 'llm' not in st.session_state:
    try:
        st.session_state.llm = GeminiLLM()
    except ValueError:
        st.session_state.llm = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'document_processed' not in st.session_state:
    st.session_state.document_processed = False

def process_pdf(uploaded_file):
    """Process uploaded PDF file"""
    try:
        with st.spinner("Processing PDF..."):
            # extract text
            text = st.session_state.pdf_processor.extract_text_from_pdf(uploaded_file)

            if not text.strip():
                st.error("No text could be extracted from the PDF. Please try a different file.")
                return False
            
            # split into chunks
            chunks = st.session_state.pdf_processor.split_text_into_chunks(text)

            # initialize ChromaDB
            st.session_state.chroma_db = ChromaDBManager()

            # Add doc to chromaDB
            st.session_state.chroma_db.add_documents(chunks)

            st.session_state.document_processed = True
            st.success(f"PDF processed successfully! Created {len(chunks)} chunks.")
            return True
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        return False 
    
def chat_with_document(query):
    """Chat with the document using RAG"""
    if not st.session_state.chroma_db:
        return "Please upload and process a PDF document first."
    
    try:
        # Search for relevant documents
        search_results = st.session_state.chroma_db.search_similar_documents(query)

        if not search_results['documents']:
            return "No relevant information found in the document."
        
        # combine context from similar document
        context = "\n".join(search_results['documents'][0])

        # generate response using LLM 
        if st.session_state.llm:
            response = st.session_state.llm.generate_response(context, query)
            return response
        else:
            return "LLM not initialized. Please check your API Key."
    except Exception as e:
        return f"Error during chat: {str(e)}"

# Main APP
def main():
    st.title("📚 PDF Book Reader")
    st.markdown("Upload a PDF book and chat with it using API")

    # sidebar for PDF upload
    with st.sidebar:
        st.header("Upload PDF")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

        if uploaded_file is not None:
            if st.button("Process PDF"):
                if process_pdf(uploaded_file):
                    st.session_state.chat_history = [] # clear chat history for a new documents
        
        st.markdown("---")
        st.header("API Configuration")
        api_key = st.text_input("Gemini API Key", type="password", value=os.getenv('GEMINI_API_KEY', ''))

        if api_key and st.session_state.llm is None:
            try:
                st.session_state.llm = GeminiLLM(api_key=api_key)
                st.success("API Key configured Successfully!")
            except Exception as e:
                st.error(f"Error configuring API: {str(e)}")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Document Information")
        if st.session_state.document_processed:
            st.success("✅ Document is ready for chatting!")
            if uploaded_file:
                st.info(f"**Uploaded file:** {uploaded_file.name}")  
        else:
            st.info("Please upload a PDF document to get started.")
        
        st.markdown("---")
        st.header("How to use")
        st.markdown("""
        1. Upload a PDF file using the sidebar
        2. Click 'Process PDF' to analyze the document
        3. Start chatting with your document in the chat interface
        4. The AI will answer questions based on the document content
        """)

    with col2:
        st.header("Chat with your documents")

        # display chat history
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.chat_history:
                if message['role'] == "user":
                    st.markdown(f"**You:** {message['content']}")
                else:
                    st.markdown(f"**AI:** {message['content']}") 
                st.markdown("---")
        
        # chat input
        if st.session_state.document_processed:
            user_query = st.text_input("Ask a question about the document:", key="user_input")

            if st.button("Send") and user_query:
                # add user messages to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_query})

                # get AI response
                with st.spinner("Thinking..."):
                    ai_response = chat_with_document(user_query)
                
                # Add AI response to chat history
                st.session_state.chat_history.append({"role": "ai", "content": ai_response})

                # Rerun to update chat display
                st.rerun()
        else:
            st.warning("Please upload and process a PDF document first to start chatting")

if __name__ == "__main__":
    main()

