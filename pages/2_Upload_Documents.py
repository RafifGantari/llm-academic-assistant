from src.loader import load_documents
from src.vectorstore import create_vectorstore
import streamlit as st

st.title("Upload Dokumen")

uploaded_files = st.file_uploader(
    "Upload PDF / TXT",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if st.button("Proses Dokumen") and uploaded_files:
    with st.spinner("Memproses dokumen..."):
        docs = load_documents(uploaded_files)
        create_vectorstore(docs)   # ⬅️ simpan ke disk

        st.success("Dokumen berhasil diproses! Silakan buka halaman Chat.")
