import os
from parser import parser
from chroma_conn import chroma_conn, retriever


def generate_doc_for_chunk(chunk, qa_chain, output_dir="docs"):
    module_folder = os.path.join(output_dir, os.path.dirname(chunk["file"]).split("/", 1)[1],
                                 os.path.splitext(os.path.basename(chunk["file"]))[0])
    print(module_folder)
    os.makedirs(module_folder, exist_ok=True)

    query = f"Explain this {chunk['type']} in simple terms for developers:\n{chunk['code']}"
    try:
        response = qa_chain.invoke({'input': f'{query}'})
    except Exception as e:
        print(f"Exception on file {chunk['file']}, exception: {e}")
        return
    explanation = response["answer"]

    md_content = f"# {chunk['name']} ({chunk['type']})\n\n"

    if chunk["docstring"]:
        md_content += f"**Docstring:**\n```python\n{chunk['docstring']}\n```\n\n"

    md_content += f"**Code:**\n```python\n{chunk['code']}\n```\n\n"
    md_content += f"**Explanation:**\n{explanation}\n\n"

    if chunk["imports"]:
        md_content += f"**Imports:**\n```\n{', '.join(chunk['imports'])}\n```\n"

    md_file_path = os.path.join(module_folder, f"{chunk['name']}.md")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return md_file_path


def generate_documentation(code_directory):
    output_dir = "docs"
    chunks = parser.parse_codebase(code_directory)
    vectorstore = chroma_conn.create_or_open_chroma_collection(code_directory)

    qa_chain = retriever.build_research_assistant(vectorstore)

    for i, chunk in enumerate(chunks):
        md_file = generate_doc_for_chunk(chunk, qa_chain, output_dir=output_dir)
        print(md_file)

        if i % 10 == 0:
            print(i + 250)
