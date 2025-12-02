from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate

from groq import Groq
from langchain_groq import ChatGroq
import os


def build_research_assistant(vectordb):
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 10}
    )

    llm = ChatGroq(
        temperature=0.0,
        model="llama-3.1-8b-instant"
        # model="openai/gpt-oss-20b"
    )

    prompt = PromptTemplate(
        input_variables=["context", "input"],
        template="""
            You are a code assistant. Use ONLY the provided context.
            Explain the selected function or file clearly.

            Context:
            {context}

            
            {input}

            Answer concisely:
            """
    )

    document_chain = create_stuff_documents_chain(llm, prompt)

    qa_chain = create_retrieval_chain(retriever, document_chain)
    return qa_chain

def ask_question(qa_chain, query):
    print(f"\nQuestion: {query}\n")
    result = qa_chain.invoke({"input": query})
    
    print(" Answer:\n", result["answer"])
    # print("\n Sources:")
    # for doc in result["context"]:
    #     meta = doc.metadata
    #     print(f"- {meta['title']} (chunk {meta['chunk_index']}) → {meta['pdf_url']}")  