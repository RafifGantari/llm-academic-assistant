from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.llm import get_llm


def build_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
Gunakan konteks berikut untuk menjawab pertanyaan.
Jika tidak tahu, katakan tidak tahu.

Konteks:
{context}

Pertanyaan:
{question}
""")

    chain = (
        {
            "context": retriever,   # menerima STRING
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
