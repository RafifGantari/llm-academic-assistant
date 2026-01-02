from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.set_page_config(page_title="LLM Academic Assistant", layout="wide")

st.title("📚 LLM Academic Assistant")
st.write("Gunakan sidebar untuk upload dokumen dan mulai chat.")
import os
st.write(os.getenv("GROQ_API_KEY"))
