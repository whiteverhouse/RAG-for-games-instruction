from langchain_community.document_loaders import DirectoryLoader
DATA_PATH="data"

def load_documents():
    loader=DirectoryLoader(DATA_PATH,glob="*.pdf")
    documents=loader.load()
    return documents

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000
)