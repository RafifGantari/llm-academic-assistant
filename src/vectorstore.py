import os
from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings

VECTORSTORE_PATH = "artifacts/vectorstore"

def create_vectorstore(docs):
    embeddings = get_embeddings()
    return FAISS.from_documents(docs, embeddings)

def save_vectorstore(vs, path=VECTORSTORE_PATH):
    os.makedirs(path, exist_ok=True)
    vs.save_local(path)

def load_vectorstore(path=VECTORSTORE_PATH):
    embeddings = get_embeddings()

    index_file = os.path.join(path, "index.faiss")
    if not os.path.exists(index_file):
        raise FileNotFoundError("Vectorstore belum dibuat")

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
