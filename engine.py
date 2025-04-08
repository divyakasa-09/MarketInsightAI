from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.core import PropertyGraphIndex
from typing import List, Dict
from src.constants import *
from src.utils import *
import nest_asyncio

# Apply nested async loop patching
nest_asyncio.apply()

# Step 1: Connect to the Neo4j graph store
graph_store = Neo4jPropertyGraphStore(
    username=neo4j_username,
    password=neo4j_password,
    url=neo4j_url,
)

# Step 2: Load index from graph store
index = PropertyGraphIndex.from_existing(
    property_graph_store=graph_store
)

# Step 3: Create the query engine from the index
query_engine = index.as_query_engine(include_text=True)

# Step 4: Define list of financial analysis queries
queries = [
    "How to invest in the EV sector? Summarize the most important financial trends in the EV Sector.",
    "What are the recent financial sentiments about renewable energy investments?",
    "Summarize the financial outlook for the technology sector in 2024.",
    "What are the key financial risks in the automotive industry this year?",
    "Provide insights on the financial performance of AI startups in the US."
]

# Step 5: Run queries and generate reports
def query_and_generate_reports(queries: List[str]) -> List[Dict[str, str]]:
    results = []

    for query in queries:
        print(f"Processing query: {query}")
        context = query_engine.query(query)
        report = generate_summary_report(str(context), query)
        results.append({
            "query": query,
            "context": context,
            "report": report
        })

    return results

# Step 6: Save reports to file
def save_reports_to_file(results: List[Dict[str, str]], filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        for result in results:
            file.write(f"Query:\n{result['query']}\n\n")
            file.write(f"Context:\n{result['context']}\n\n")
            file.write(f"Generated Report:\n{result['report']}\n\n")
            file.write("-" * 80 + "\n\n")

# Execute
results = query_and_generate_reports(queries)
save_reports_to_file(results, "financial_sentiment_reports.txt")

# Print to console
for result in results:
    print(f"Query: {result['query']}")
    print(f"Generated Report:\n{result['report']}")
    print("-" * 80)
