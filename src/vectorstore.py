from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings
import os

VECTORSTORE_DIR = "artifacts/vectorstore"

def create_vectorstore(docs):
    embeddings = get_embeddings()
    vs = FAISS.from_documents(docs, embeddings)

    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
    vs.save_local(VECTORSTORE_DIR)

    return vs

def load_vectorstore():
    if not os.path.exists(VECTORSTORE_DIR):
        raise FileNotFoundError("Vectorstore belum dibuat")

    embeddings = get_embeddings()
    return FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
