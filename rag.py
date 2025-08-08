import os
from dotenv import load_dotenv 
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv() 

print("Setting up the RAG pipeline with LlamaIndex and Groq...")

Settings.llm = Groq(model="llama3-8b-8192")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
print("LLM and Embedding model configured.")

print("Loading specific document: project_aether_doc.txt...")
documents = SimpleDirectoryReader(
    input_files=["project_aether_doc.txt"]
).load_data()

# Create vector store index
print("Creating vector store index...")
index = VectorStoreIndex.from_documents(documents)
print("Index created successfully.")

query_engine = index.as_query_engine()
query = input("give your query: ")
print(f"\nQuerying the engine with: '{query}'")
response = query_engine.query(query)

print("\n--- RAG Response (from LlamaIndex + Groq) ---")
print(response)