import chromadb
from sentence_transformers import SentenceTransformer
import os

class ChromaDBManager:
    def __init__(self, persist_directory="./data/chroma_db"):
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)

        # initialize chromadb client
        self.client = chromadb.PersistentClient(path=persist_directory)

        # initialize embedding models
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

        # get or create collection
        self.collection = self.client.get_or_create_collection(
            name="pdf_documents",
            metadata={"hnsw:space": "cosine"}
        )
    
    def get_embedding(self, text):
        """Generate embedding for text"""
        return self.embedding_model.encode(text).tolist()
    
    def add_documents(self, documents):
        """Add documents to ChromaDB with embeddings"""
        try:
            if not documents:
                raise ValueError("No documents to add")
            
            embeddings = [self.get_embedding(doc) for doc in documents]

            # generate IDs
            ids = [f"doc_{i}" for i in range(len(documents))]

            # add to collection WITHOUT metadata
            self.collection.add(
                embeddings=embeddings,
                documents=documents,
                ids=ids
            )
            
        except Exception as e:
            raise Exception(f"Error adding documents to ChromaDB: {str(e)}")

    def search_similar_documents(self, query, n_results=3):
        """Search for similar documents based on query"""
        try:
            query_embedding = self.get_embedding(query)

            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )

            return results 
        except Exception as e:
            raise Exception(f"Error searching documents: {str(e)}")
        
        