import os
import PyPDF2
from typing import List

def extract_text_from_pdf(pdf_path: str) -> List[str]:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text_chunks = []
        for page in reader.pages:
            text = page.extract_text()
            # Split text into smaller chunks
            chunks = text.split('\n\n')
            text_chunks.extend(chunks)
    return text_chunks

def process_pdfs_in_directory(directory: str) -> List[str]:
    all_text_chunks = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            text_chunks = extract_text_from_pdf(pdf_path)
            all_text_chunks.extend(text_chunks)
    return all_text_chunks