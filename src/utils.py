import os
import requests
from bs4 import BeautifulSoup
from constants import *

from llama_index.llms.llama_cpp import LlamaCPP

# Load local LLaMA model
llm = LlamaCPP(
    model_path="./models/llama-2-7b-chat.ggmlv3.q4_0.bin",  # Update if needed
    temperature=0.2,
    max_tokens=512,
    context_window=2048
)

def search_with_google_api(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={google_api}&cx={search_engine_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

def generate_search_queries(user_input):
    prompt = f"""
    You are a financial analyst and search expert. Based on the following user input, generate a list of 5–7 search queries
    for financial sentiment analysis. Cover sector-specific trends, regional insights, and broader financial topics.

    User Input: {user_input}

    Output a Python list of strings only.
    """
    result = llm.complete(prompt)
    try:
        return eval(result.text.strip())  # Convert string list to Python list
    except Exception as e:
        print("Failed to parse queries:", e)
        return []

def fetch_full_content(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            full_text = "\n".join([p.get_text() for p in paragraphs])
            return full_text.strip() if full_text else None
        else:
            print(f"Error fetching {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_dataset_from_queries(queries, directory="dataset"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_count = 1
    for query in queries:
        print(f"Processing query: {query}")
        valid_count = 0
        page_number = 1

        while valid_count < 10:
            print(f"Fetching page {page_number}")
            results = search_with_google_api(query + f"&start={page_number * 10}")
            if not results:
                break

            for result in results:
                if valid_count >= 10:
                    break
                title = result["title"]
                link = result["link"]
                snippet = result.get("snippet", "")
                full_content = fetch_full_content(link)
                if full_content:
                    filename = f"{directory}/doc_{file_count}.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"Query: {query}\n")
                        f.write(f"Title: {title}\n")
                        f.write(f"Link: {link}\n")
                        f.write(f"Snippet: {snippet}\n\n")
                        f.write(f"Full Content:\n{full_content}")
                    print(f"Saved: {filename}")
                    valid_count += 1
                    file_count += 1
                else:
                    print(f"Skipped: {link} (No valid content)")
            page_number += 1

    print(f"Finished. Total files saved: {file_count - 1}")

def generate_summary_report(context: str, query: str) -> str:
    prompt = f"""
    You are a financial sentiment analyst. Use the following context to generate an actionable summary report:

    Context:
    {context}

    Query:
    {query}

    The report should include:
    1. A high-level summary of financial trends
    2. Sentiment insights (positive, negative, neutral)
    3. Driving factors behind sentiments
    4. Suggestions for investors or stakeholders

    Be concise but insightful.
    """
    result = llm.complete(prompt)
    return result.text.strip()
