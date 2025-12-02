import langchain
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from sentence_transformers import SentenceTransformer
import uuid
from parser import parser


def create_collection(collection_name):
    chroma_client = chromadb.PersistentClient(path="vectorstore")
    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )
    return collection

def add_chunks_to_chroma(chunks, collection, embedder):
    texts = []
    ids = []
    metadatas = []

    for chunk in chunks:
        chunk_text = chunk["code"]

        meta = {
            "file": chunk["file"],
            "name": chunk["name"],
            "type": chunk["type"],
            "start_line": chunk["start_line"],
            "end_line": chunk["end_line"]
        }

        texts.append(chunk_text)
        ids.append(str(uuid.uuid4()))
        metadatas.append(meta)

    embeddings = embedder.encode(texts, convert_to_numpy=True)
    collection.add(
        embeddings=embeddings,
        metadatas=metadatas,
        documents=texts,
        ids=ids
    )

    print(f"Inserted {len(texts)} chunks")


def get_embedder():
    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return embedder
    

def add_to_chroma(code_directory):
    chunks = parser.parse_codebase(code_directory)

    embedder = get_embedder()
    collection = create_collection(code_directory)

    add_chunks_to_chroma(chunks, collection, embedder)

def create_or_open_chroma_collection(collection_name):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings,
        collection_name=collection_name
        )
    
    if vectorstore._collection.count() == 0:
        add_chunks_to_chroma(collection_name)
    
        vectorstore = Chroma(
            persist_directory="vectorstore",
            embedding_function=embeddings,
            collection_name=collection_name
            )   
        print("data in now stored in chromadb")
    return vectorstore
    