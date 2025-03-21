from utils import *
from llama_index.core import SimpleDirectoryReader
from llama_index.core import SimpleDirectoryReader
from llama_index.core import PropertyGraphIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import os
import openai
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
import nest_asyncio
import asyncio

# Apply nest_asyncio
nest_asyncio.apply()

os.environ["OPENAI_API_KEY"] = open_ai_key
openai.api_key = os.environ["OPENAI_API_KEY"]



# Change the input as needed
user_input = "Financial sentiment analysis for the electric vehicle sector in the US"
queries = generate_search_queries(user_input)
queries
create_dataset_from_queries(queries)


# Documents Reader
documents = SimpleDirectoryReader("dataset").load_data()


graph_store = Neo4jPropertyGraphStore(
    username=neo4j_username,
    password=neo4j_password,
    url=neo4j_url,
)


# Create the index
index = PropertyGraphIndex.from_documents(
    documents,
    embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
    kg_extractors=[
        SchemaLLMPathExtractor(
            llm=OpenAI(model="gpt-3.5-turbo", temperature=0.0)
        )
    ],
    property_graph_store=graph_store,
    show_progress=True,
    use_async=True
)


# save
index.storage_context.persist(persist_dir="./storage")
print("index saved")