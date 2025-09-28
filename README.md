📚 PDF Book Reader with AI Chat

A Streamlit-based web application that allows users to upload PDF books and chat with them using AI. Built with RAG (Retrieval Augmented Generation) architecture, ChromaDB for vector storage, and Google Gemini API for intelligent responses.

🚀 Features
PDF Upload & Processing: Upload any PDF document and extract text content

AI-Powered Chat: Ask questions about your PDF content and get intelligent answers

RAG Architecture: Uses Retrieval Augmented Generation for accurate, context-aware responses

Vector Database: ChromaDB for efficient similarity search and document retrieval

Free API Support: Compatible with Google Gemini API and Groq API

User-Friendly Interface: Clean Streamlit UI with real-time chat interface

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python

Vector Database: ChromaDB

Embeddings: Sentence Transformers (all-MiniLM-L6-v2)

LLM: Google Gemini Pro / Groq

PDF Processing: PyPDF2

Text Splitting: LangChain Text Splitter

📋 Prerequisites
Python 3.8 or higher

Google Gemini API key 

🏗️ Installation

1. Clone or download the project:

# Create project directory
mkdir "PDF Book Reader"
cd "PDF Book Reader"

2. Create project structure:

PDF Book Reader/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── utils/
│   ├── __init__.py
│   ├── pdf_processor.py
│   ├── chroma_manager.py
│   └── llm_integration.py
├── data/
└── static/

3. Install dependencies:

pip install -r requirements.txt

4. Set up environment variables:

    a. Create a .env file in the root directory

    b. Add your API key:
    GEMINI_API_KEY=your_gemini_api_key_here

🔑 Getting API Keys

Google Gemini API (Free)

1. Visit Google AI Studio

2. Sign in with your Google account

3. Click "Create API Key"

4. Copy the key and add it to your .env file

🎯 Usage

1. Run the application:

streamlit run app.py

2. Access the web interface:

    a. Open your browser and go to http://localhost:8501

3. Using the application:

    a. Upload PDF: Use the sidebar to upload a PDF file

    b. Process Document: Click "Process PDF" to analyze the document

    c. Start Chatting: Ask questions about your PDF content in the chat interface

    d. Get Answers: Receive AI-generated responses based on the document content

📁 Project Structure

PDF Book Reader/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (API keys)
├── .gitignore           # Git ignore file
├── utils/               # Utility modules
│   ├── __init__.py
│   ├── pdf_processor.py    # PDF text extraction and processing
│   ├── chroma_manager.py   # ChromaDB vector database operations
│   └── llm_integration.py  # Gemini
├── data/                # ChromaDB storage directory
└── static/              # Static assets (if any)

🔧 Configuration

Environment Variables (.env)
 
GEMINI_API_KEY=your_google_gemini_api_key

Model Configuration

Embedding Model: all-MiniLM-L6-v2

Text Chunk Size: 1000 characters

Chunk Overlap: 200 characters

Similarity Search Results: 3 chunks

🐛 Troubleshooting

Common Issues
API Key Errors:

Ensure your API key is correctly set in the .env file

Verify the key has not expired

PDF Processing Failures:

Ensure the PDF is text-based (not scanned images)

Check file size (recommended < 50MB)

ChromaDB Errors:

Delete the data/ folder to reset the vector database

Ensure write permissions in the project directory

Module Import Errors:

Verify all dependencies are installed: pip install -r requirements.txt

Check the project structure matches exactly

Error Messages and Solutions

"Error adding documents to ChromaDB": Reset the ChromaDB by deleting the data/ folder

"No text could be extracted": Try a different PDF file or ensure it contains extractable text

"API key not found": Check your .env file and restart the application

📊 How It Works

Architecture
PDF Processing:

Upload PDF → Extract text → Split into chunks

Vector Storage:

Generate embeddings → Store in ChromaDB

Query Processing:

User question → Generate query embedding → Similarity search

Response Generation:

Retrieved context + User question → LLM → AI response

RAG Pipeline

PDF Upload → Text Extraction → Chunking → Embedding → ChromaDB Storage
                                                         ↓
User Query → Embedding → Similarity Search → Context + Query → LLM → Response

🌟 Future Enhancements

Support for multiple PDFs

Document summarization

Export chat conversations

User authentication

Advanced search filters

Support for other file formats (DOCX, TXT)

Chat history persistence

🤝 Contributing

Fork the project

Create a feature branch

Commit your changes

Push to the branch

Open a Pull Request

📄 License

This project is open source and available under the MIT License.
