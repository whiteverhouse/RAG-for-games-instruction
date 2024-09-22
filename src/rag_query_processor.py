from typing import List
from vector_db import VectorDB
from embedding_model import EmbeddingModel
from deepseek_api import DeepSeekAPI

class RAGQueryProcessor:
    def __init__(self, vector_db: VectorDB, embedding_model: EmbeddingModel, deepseek_api: DeepSeekAPI):
        self.vector_db = vector_db
        self.embedding_model = embedding_model
        self.deepseek_api = deepseek_api

    def process_query(self, query: str) -> str:
        query_vector = self.embedding_model.encode([query])[0]
        relevant_texts = self.vector_db.search(query_vector, k=3)
        
        context = "\n".join(relevant_texts)
        prompt = f"Answer the question based on the following information:\n\n{context}\n\nQuestion: {query}\nAnswer:"
        
        response = self.deepseek_api.generate_response(prompt)
        return response