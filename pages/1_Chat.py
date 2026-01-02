import streamlit as st
from src.vectorstore import load_vectorstore
from src.chain import build_chain

@st.cache_resource
def get_vs():
    return load_vectorstore()

@st.cache_resource
def get_chain(_vs):
    return build_chain(_vs)

query = st.text_input("Tanyakan materi:")

if query:
    vs = get_vs()
    chain = get_chain(vs)
    response = chain.invoke(query)
    st.write(response)
