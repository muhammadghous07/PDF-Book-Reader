import PyPDF2
import io
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

    def extract_text_from_pdf(self, pdf_file):  
        """Extract text from uploaded pdf file"""
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.getvalue()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
        
    def split_text_into_chunks(self, text):
        """Split text into manageable chunks for embedding"""
        chunks = self.text_splitter.split_text(text)
        return chunks
    
