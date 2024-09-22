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
        prompt = f"""Based on the following information, please answer the question. If the information is insufficient to answer the question, please honestly state 'I don't have enough information to answer this question.'
                Context:
                {context}
                Question: {query}
                Answer:"""
        
        response = self.deepseek_api.generate_response(prompt)
        return response.strip()

    # def get_relevant_context(self, query: str) -> List[str]:
    #     query_vector = self.embedding_model.encode([query])[0]
    #     return self.vector_db.search(query_vector, k=3)