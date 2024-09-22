from typing import List
import faiss
import numpy as np

class VectorDB:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add_vectors(self, vectors: List[List[float]], texts: List[str]):
        # Convert list to NumPy array
        vectors_np = np.array(vectors).astype('float32')
        self.index.add(vectors_np)
        self.texts.extend(texts)

    def search(self, query_vector: List[float], k: int) -> List[str]:
        # Convert query vector to NumPy array
        query_vector_np = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector_np, k)
        return [self.texts[i] for i in indices[0]]

    def update_vectors(self, vectors: List[List[float]], texts: List[str]):
        self.index.reset()
        self.texts = []
        self.add_vectors(vectors, texts)