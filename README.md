

# 📈 Financial Market Insight AI with Knowledge Graph

A **financial market sentiment analysis system** that leverages Generative AI (GenAI), Knowledge Graphs, and Retrieval-Augmented Generation (RAG) to extract, process, and analyze real-time financial data from the web, offering actionable insights for investors, analysts, and stakeholders.

---

## 📚 Project Overview

This project automates **financial market sentiment analysis** by combining:

- ✅ Web scraping + Google Search API for real-time data collection
- ✅ Entity extraction and relationship modeling with **Neo4j** knowledge graphs
- ✅ Vector embedding and indexing with **OpenAI** + **LlamaIndex**
- ✅ Querying + RAG workflow to generate human-readable, context-rich financial reports

It provides **actionable financial insights** across sectors like EV, technology, renewable energy, automotive, and AI startups.

---

## 💡 Key Features

* Real-time data scraping from news, reports, stock feeds
* Knowledge graph construction of companies, sectors, and trends
* Vector embedding using OpenAI `text-embedding-3-small`
* Contextual querying using LlamaIndex’s RAG pipeline
* Automated report generation with sentiment summary, trend analysis, and investment insights
* Modular, reusable, and extensible codebase

---

## 🛠 Tech Stack

* **Language:** Python 3.10
* **Libraries:** `pandas`, `BeautifulSoup`, `requests`, `neo4j`, `llama_index`, `openai`
* **Models:** OpenAI GPT-4o, GPT-3.5-turbo
* **Database:** Neo4j (property graph)
* **Embedding:** OpenAI embeddings
* **Indexing:** LlamaIndex

---



## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

* Python 3.10
* Access to:

  * Neo4j instance (set username, password, and URL in `constants.py`)
  * Google Custom Search API key + Search Engine ID
  * OpenAI API key

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure credentials

Edit `src/constants.py` and fill in:

```python
neo4j_username = 'your-username'
neo4j_password = 'your-password'
neo4j_url = 'your-neo4j-url'

google_api = 'your-google-api-key'
search_engine_id = 'your-search-engine-id'
open_ai_key = 'your-openai-api-key'
```

---

## 🚀 Running the Pipeline

### 1. **Build the Knowledge Graph**

Run `graph_store_creation.py`:

```bash
python src/graph_store_creation.py
```

- ✅ Generates search queries from input
- ✅ Collects web data via Google Search + scraping
- ✅ Creates Neo4j property graph with entities + relations
- ✅ Persists LlamaIndex index to `./storage`

---

### 2. **Query and Generate Reports**

Run `engine.py`:

```bash
python engine.py
```

- ✅ Runs predefined financial queries
- ✅ Retrieves relevant graph context
- ✅ Uses OpenAI to summarize + analyze sentiment
- ✅ Outputs reports to `financial_sentiment_reports.txt`

---

### 3. **Explore in Notebook**

Open:

```
notebook/updated_market_data_analysis.ipynb
```

- ✅ Explore dataset, embeddings, and graph insights
- ✅ Run custom analysis + visualizations

---

## 🧩 Code Modules Explained

| File                                 | Purpose                                                                          |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| `engine.py`                          | Runs full pipeline → queries graph → generates summary reports using OpenAI      |
| `graph_store_creation.py`            | Builds Neo4j graph + LlamaIndex index from scraped financial documents           |
| `utils.py`                           | Contains search query generation, web scraping, and report summarization helpers |
| `constants.py`                       | Stores API keys + credentials                                                    |
| `updated_market_data_analysis.ipynb` | Jupyter notebook for exploring data + testing the system                         |

---

## 📊 Example Queries

* How to invest in the EV sector? Summarize the most important financial trends.
* What are the recent financial sentiments about renewable energy investments?
* Summarize the financial outlook for the technology sector in 2024.
* What are the key financial risks in the automotive industry this year?
* Provide insights on the financial performance of AI startups in the US.

---

## 💥 Project Highlights

✔ Automates real-time financial sentiment extraction
✔ Uses graph-based reasoning to enhance LLM-generated insights
✔ Supports modular expansion to new sectors, regions, and languages
✔ Combines traditional data scraping + modern RAG techniques

---


