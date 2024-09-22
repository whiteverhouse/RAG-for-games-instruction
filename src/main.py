import os
from dotenv import load_dotenv
from pdf_processor import process_pdfs_in_directory
from vector_db import VectorDB
from embedding_model import EmbeddingModel
from deepseek_api import DeepSeekAPI
from rag_query_processor import RAGQueryProcessor

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    pdf_texts = process_pdfs_in_directory("data")
    embedding_model = EmbeddingModel()
    
    # Get the output dimension of the embedding model
    sample_embedding = embedding_model.encode(["sample text"])[0]
    embedding_dimension = len(sample_embedding)
    
    vector_db = VectorDB(dimension=embedding_dimension)
    deepseek_api = DeepSeekAPI(os.getenv("DEEPSEEK_API_KEY"))

    # Process PDF texts and add to vector database
    embeddings = embedding_model.encode(pdf_texts)
    vector_db.add_vectors(embeddings, pdf_texts)

    # Create RAG query processor
    rag_processor = RAGQueryProcessor(vector_db, embedding_model, deepseek_api)

    # Example query
    query = "How do you play a card in UNO?"
    response = rag_processor.process_query(query)
    print(f"Question: {query}")
    print(f"Answer: {response}")

if __name__ == "__main__":
    main()