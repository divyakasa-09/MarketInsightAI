import requests
from constants import *
import os
import requests
from bs4 import BeautifulSoup
import openai


def search_with_google_api(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={google_api}&cx={search_engine_id}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []


def generate_search_queries(user_input):
    """
    Generates a list of 5-7 detailed and relevant search queries for financial sentiment analysis
    based on the user's input, such as a target sector, field, or region.
    """
    prompt = f"""
    You are a financial analyst and search query expert. Based on the following user input, generate a list of 5-7 search queries
    for financial sentiment analysis based on user input. Ensure the queries cover diverse aspects of the topic, including sector-specific trends,
    regional financial overviews, and broader financial landscapes. The queries should focus on extracting data relevant to sentiment
    and performance analysis.

    User Input: {user_input}

    Strictly output the queries as a python list of strings. Do not add any additional comments.
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in generating search queries for financial sentiment analysis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    # Extract and clean up the list of queries
    queries =  response.choices[0].message.content.strip()
    return eval(queries)

def fetch_full_content(url):
    """
    Fetches the full content of a webpage given its URL.
    """
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
            print(f"Error: Unable to fetch content from {url} (Status Code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def create_dataset_from_queries(queries, directory="dataset"):
    """
    Process search queries and save results as text files in the same directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_count = 1  # To ensure unique filenames across all queries

    for query in queries:
        print(f"Processing query: {query}")
        valid_count = 0
        page_number = 1

        while valid_count < 10:
            print(f"Fetching search results, page {page_number}...")
            results = search_with_google_api(query + f"&start={page_number * 10}")

            if not results:
                print("No more results found. Try refining the query.")
                break

            for result in results:
                if valid_count >= 10:
                    break  # Stop when 10 valid documents are saved

                title = result["title"]
                link = result["link"]
                snippet = result.get("snippet", "No snippet")

                # Fetch full content of the link
                full_content = fetch_full_content(link)
                if full_content:  # Save only if content is valid
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

            page_number += 1  # Move to the next page of results

    print(f"Finished processing all queries. Total files saved: {file_count - 1}")


def generate_summary_report(context: str, query: str) -> str:
    """
    Generate a detailed summary report for financial sentiment analysis.
    Takes context and query as inputs and returns a comprehensive summary.
    """
    prompt = f"""
    You are a financial sentiment analysis assistant. Using the context provided below, generate a detailed summary report:

    Context:
    {context}

    Query:
    {query}

    The report should include:
    1. A high-level summary of the financial trends related to the query.
    2. Key positive, negative, and neutral sentiments detected.
    3. Reasons or factors driving the sentiments.
    4. Suggestions or insights for potential investors or stakeholders.

    Be concise but ensure that the report is actionable and insightful.
    """
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in financial sentiment analysis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()


