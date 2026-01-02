import streamlit as st
from src.loader import load_and_split
from src.vectorstore import create_vectorstore, save_vectorstore

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open(f"data/documents/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    docs = load_and_split(f"data/documents/{uploaded_file.name}")
    vs = create_vectorstore(docs)
    save_vectorstore(vs)

    st.success("Dokumen berhasil diproses!")
