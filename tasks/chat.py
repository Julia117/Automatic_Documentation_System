from chroma_conn import chroma_conn, retriever
from prompt_toolkit import prompt


def chat():
    code_directory = "harmony-main"
    vectorstore = chroma_conn.create_or_open_chroma_collection(code_directory)
    qa_chain = retriever.build_research_assistant(vectorstore)

    while True:
        user_input = prompt(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        retriever.ask_question(
            qa_chain, user_input
        )
