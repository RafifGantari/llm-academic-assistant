import streamlit as st
from src.vectorstore import load_vectorstore
from src.chain import build_chain

st.title("💬 Chat with Academic Assistant")

try:
    vs = load_vectorstore()
except FileNotFoundError:
    st.warning("📄 No documents found. Please upload documents first.")
    st.stop()

@st.cache_resource
def get_chain(_vs):
    return build_chain(_vs)

query = st.text_input("Tanyakan materi:")

if query:
    chain = get_chain(vs)
    response = chain.invoke(query)
    st.write(response)
