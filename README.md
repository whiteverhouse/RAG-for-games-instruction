# Game Q&A RAG Chatbot

A RAG-based chatbot for answering game-related questions. It parse and vectorize gamebooks of board games for info storage and retrieval, and uses DeepSeek's API for response generation and searches for relevant info in the database.

## Features
- Web-based user interface with conversation history for improved interaction
- Generates answers with LLM, powered by DeepSeek API
- Supports multiple game rule PDFs
- Supports multilingual


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
   python src/app.py   
3. Open a web browser and navigate to `http://localhost:5000`
4. Use the interface to ask questions and interact with the chatbot


## File Structure

- src/: Source code
- data/: PDF files
- requirements.txt: Project dependencies
- README.md: Project info

## Notes
- You need to put down a valid DeepSeek API key in the .env file to get the LLM to work
- multilingual Embedding model: 'paraphrase-multilingual-MiniLM-L12-v2' 
- Vector dimension: 384 (may change based on the multilingual model)
- Vector database: FAISS
- The system automatically adjusts to the embedding model's output dimension.

