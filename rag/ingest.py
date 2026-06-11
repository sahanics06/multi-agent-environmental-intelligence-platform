from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

documents = []

files = [
    "knowledge/who_air_quality.txt",
    "knowledge/epa_guidelines.txt"
]

for file in files:

    loader = TextLoader(file)

    documents.extend(
        loader.load()
    )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(
    documents
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="vector_db"
)

print(
    f"Ingested {len(docs)} chunks."
)