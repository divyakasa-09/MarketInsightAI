


# 📊 MarketInsightAI: Real-Time Financial Insights Using Neo4j & LLaMA

**MarketInsightAI** is a real-time financial analysis system that scrapes the web for market data, structures it into a knowledge graph using Neo4j, and delivers insightful, context-aware reports using Retrieval-Augmented Generation (RAG) powered by **LLaMA** and **LlamaIndex**.

This project intelligently connects financial entities (stocks, sectors, risks, sentiment) and produces tailored, LLM-generated insights for any finance-related query — including trends in EV, renewable energy, and AI startups.

---

## 🚀 Features

- ✅ Scrapes **real-time financial news and market reports** via Google Search API  
- ✅ Builds a **Neo4j knowledge graph** to capture financial entities & relationships  
- ✅ Embeds documents using **HuggingFace sentence-transformers**  
- ✅ Uses **LLaMA (local `.bin` model via `llama-cpp-python`)** for text generation  
- ✅ Leverages **LlamaIndex** to implement a robust Retrieval-Augmented Generation pipeline  
- ✅ Generates structured, investor-ready **financial reports**

---

## 🧠 Sample Use Cases

- "What are the most important trends in the EV sector in 2024?"
- "What financial risks should investors consider in the renewable energy market?"
- "Summarize the recent sentiment around AI startups in the US."

---

## 🛠️ Tech Stack

| Component       | Technology/Library                            |
|----------------|------------------------------------------------|
| Language        | Python 3.10                                   |
| Scraping        | Google Search API, BeautifulSoup              |
| Graph Database  | Neo4j                                         |
| Embedding Model | `sentence-transformers/all-MiniLM-L6-v2`      |
| LLM             | LLaMA (via `llama-cpp-python`, local `.bin`)  |
| RAG Framework   | LlamaIndex                                    |
| Other Libraries | NestAsyncIO, Requests, Pandas                 |

---

## 📥 Output

After execution, the project generates a file:


financial_sentiment_reports.txt


Each entry includes:


Query:
What are the financial risks in the EV sector?

Context:
[Relevant extracted content from financial news]

Generated Report:
- Summarizes key risks and trends
- Analyzes investor sentiment (positive/negative/neutral)
- Offers suggestions for investors and stakeholders



## 📌 Takeaways

✅ Learn how to:

- Build AI-powered finance tools using **LLMs + Knowledge Graphs**
- Scrape and structure unstructured real-time financial data
- Implement Retrieval-Augmented Generation using **Neo4j + LLaMA**
- Run a **fully local, open-source LLM stack** (no OpenAI required)

---










