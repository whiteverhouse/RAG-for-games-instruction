# Game Q&A RAG Chatbot

A RAG-based chatbot for answering game-related questions. It uses DeepSeek's API for response generation and searches for relevant info in PDF files from the data directory.

## Features

- Processes PDF files and extracts texts
- Uses vector database for info storage and retrieval
- Generates answers with DeepSeek API
- Supports multiple game rule PDFs

## Setup

1. Clone this repo
1. Create a new virtual environment:
   ```
   conda create --name myenv python=3.x
   ```
4. Activate the Conda environment:
   ```
   conda activate myenv
   ```

5. Install the packages mentioned in requirements.txt:
   ```
   conda install --file requirements.txt
   ```
   
   If some packages are not available via Conda, use pip within the Conda environment:
   ```
   pip install -r requirements.txt
## Usage

1. Put game rule PDFs in the data directory
2. Run the main program:
   ```bash
   python src/main.py`
3. Enter your questions

## File Structure

- src/: Source code
- data/: PDF files
- requirements.txt: Project dependencies
- README.md: Project info

## Notes

- Ensure you have a valid DeepSeek API key in the .env file
- Don't commit the .env file to version control
- Currently supports UNO and Monopoly rules; add more PDFs to expand

## Technical Details

- Embedding model: 'paraphrase-multilingual-MiniLM-L12-v2' (supports multiple languages including Chinese)
- Vector dimension: 384 (may change based on the multilingual model)
- Vector database: FAISS

Note: The system automatically adjusts to the embedding model's output dimension.

