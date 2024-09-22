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
        prompt = f"基于以下信息回答问题。如果信息不足以回答问题，请诚实地说'我没有足够的信息来回答这个问题'。\n\n背景信息：{context}\n\n问题：{query}\n回答："
        
        response = self.deepseek_api.generate_response(prompt)
        return response.strip()

    def get_relevant_context(self, query: str) -> List[str]:
        query_vector = self.embedding_model.encode([query])[0]
        return self.vector_db.search(query_vector, k=3)