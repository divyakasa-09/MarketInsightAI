from utils import *
from llama_index.core import SimpleDirectoryReader, PropertyGraphIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

import nest_asyncio
import os


nest_asyncio.apply()


user_input = "Financial sentiment analysis for the electric vehicle sector in the US"
queries = generate_search_queries(user_input)
create_dataset_from_queries(queries)


documents = SimpleDirectoryReader("dataset").load_data()


graph_store = Neo4jPropertyGraphStore(
    username=neo4j_username,
    password=neo4j_password,
    url=neo4j_url,
)


llm = LlamaCPP(
    model_path="./models/llama-2-7b-chat.ggmlv3.q4_0.bin",  
    temperature=0.0,
    max_tokens=512,
    context_window=2048,
)


embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


index = PropertyGraphIndex.from_documents(
    documents,
    embed_model=embed_model,
    kg_extractors=[
        SchemaLLMPathExtractor(llm=llm)
    ],
    property_graph_store=graph_store,
    show_progress=True,
    use_async=True
)


index.storage_context.persist(persist_dir="./storage")
print("✅ Index saved successfully using LLaMA and HuggingFace embeddings.")
