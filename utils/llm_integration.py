import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiLLM:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')  
        if not self.api_key:
            raise ValueError("Gemini API key not provided")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-pro')  

    def generate_response(self, context, user_query):
        """Generate response using Gemini API"""
        prompt = f"""
        Based on the following context from the document, answer the user's question.
        If the answer cannot be found in the context, please say so.

        Context:
        {context}

        User Question: {user_query}

        Answer:
        """

        try: 
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"  
        
        