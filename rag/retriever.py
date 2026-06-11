from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)


def retrieve_context(query):

    docs = vectordb.similarity_search(
        query,
        k=3
    )

    return "\n".join(
        doc.page_content
        for doc in docs
    )