import os
from dotenv import load_dotenv
from pdf_processor import process_pdfs_in_directory
from vector_db import VectorDB
from embedding_model import EmbeddingModel
from deepseek_api import DeepSeekAPI
from rag_query_processor import RAGQueryProcessor
import threading

def initialize_system():
    # load environment variables
    load_dotenv()
    
    # initialize components
    pdf_texts = process_pdfs_in_directory("data")
    embedding_model = EmbeddingModel()
    
    # get the output dimension of the embedding model
    sample_embedding = embedding_model.encode(["sample text"])[0]
    embedding_dimension = len(sample_embedding)
    
    vector_db = VectorDB(dimension=embedding_dimension)
    deepseek_api = DeepSeekAPI(os.getenv("DEEPSEEK_API_KEY"))

    # process PDF texts and add to vector database
    embeddings = embedding_model.encode(pdf_texts)
    vector_db.add_vectors(embeddings, pdf_texts)

    # create RAG query processor
    rag_processor = RAGQueryProcessor(vector_db, embedding_model, deepseek_api)
    
    return rag_processor

def update_vector_db():
    global rag_processor
    pdf_texts = process_pdfs_in_directory("data")
    embeddings = rag_processor.embedding_model.encode(pdf_texts)
    rag_processor.vector_db.update_vectors(embeddings, pdf_texts)
