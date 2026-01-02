import streamlit as st
import os

UPLOAD_DIR = "data/documents"

# ⬇️ PENTING: pastikan folder ada
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File {uploaded_file.name} berhasil diupload")
