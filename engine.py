from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.core import PropertyGraphIndex
import openai
from typing import List, Dict
from src.constants import *
from src.utils import *
import os
import nest_asyncio

# Initialize OpenAI API Key
os.environ["OPENAI_API_KEY"] = open_ai_key
openai.api_key = os.environ["OPENAI_API_KEY"]
nest_asyncio.apply()

def query_and_generate_reports(queries: List[str]) -> List[Dict[str, str]]:
    """
    Query the knowledge graph for each query, aggregate context, and generate summary reports.
    Returns a list of dictionaries containing the query, aggregated context, and generated report.
    """
    results = []

    for query in queries:
        print(f"Processing query: {query}")
        context = query_engine.query(query)

        # Generate a summary report using the aggregated context
        report = generate_summary_report(context, query)

        results.append({
            "query": query,
            "context": context,
            "report": report
        })

    return results

def save_reports_to_file(results: List[Dict[str, str]], filename: str):
    """
    Save query results and their generated reports to a file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        for result in results:
            file.write(f"Query:\n{result['query']}\n\n")
            file.write(f"Context:\n{result['context']}\n\n")
            file.write(f"Generated Report:\n{result['report']}\n\n")
            file.write("-" * 80 + "\n\n")



# Define connection to the Neo4j graph store
graph_store = Neo4jPropertyGraphStore(
    username=neo4j_username,
    password=neo4j_password,
    url=neo4j_url,
)

# Load the index from the existing graph store
index = PropertyGraphIndex.from_existing(
    property_graph_store=graph_store
)

# Create the query engine
query_engine = index.as_query_engine(include_text=True)


# Create the query engine
query_engine = index.as_query_engine(include_text=True)

# Define a list of queries, Different kinds of queries to see the effectiveness of in EV sector
queries = [
    "How to invest in the EV sector? Summarize the most important financial trends in the EV Sector.",
    "What are the recent financial sentiments about renewable energy investments?",
    "Summarize the financial outlook for the technology sector in 2024.",
    "What are the key financial risks in the automotive industry this year?",
    "Provide insights on the financial performance of AI startups in the US."
]

# Execute the queries and generate reports
results = query_and_generate_reports(queries)

# Save the reports to a file
output_file = "financial_sentiment_reports.txt"
save_reports_to_file(results, output_file)

# Print a summary of the generated reports
for result in results:
    print(f"Query: {result['query']}")
    print(f"Generated Report:\n{result['report']}")
    print("-" * 80)

