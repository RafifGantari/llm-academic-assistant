from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
import os


def load_documents(uploaded_files):
    all_docs = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    for file in uploaded_files:
        suffix = os.path.splitext(file.name)[1].lower()

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file.getvalue())
            tmp_path = tmp.name

        if suffix == ".pdf":
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()

        elif suffix == ".txt":
            loader = TextLoader(tmp_path, encoding="utf-8")
            docs = loader.load()

        else:
            docs = []

        docs = splitter.split_documents(docs)
        all_docs.extend(docs)

        os.remove(tmp_path)

    return all_docs
