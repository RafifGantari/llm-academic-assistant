from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.set_page_config(
    page_title="LLM Academic Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 LLM Academic Assistant")
st.caption("AI-powered assistant for academic learning, document-based Q&A, and research support")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📄 Upload Documents")
    st.write("Upload PDF documents for content analysis")

with col2:
    st.markdown("### 💬 Chat with AI")
    st.write("Ask questions and generate summaries from uploaded documents")

with col3:
    st.markdown("### 📊 Academic Insights")
    st.write("Get clear explanations based on retrieved document context")