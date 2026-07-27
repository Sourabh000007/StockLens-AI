# 📈 StockLens AI

> An AI-powered equity research platform for Indian stock markets that combines financial data, annual report RAG, and Large Language Models to generate comprehensive company analysis.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

StockLens AI is an end-to-end AI-powered equity research platform designed for the Indian stock market.

Instead of simply displaying financial numbers, StockLens AI combines structured financial data with Retrieval-Augmented Generation (RAG) over annual reports to provide contextual and explainable company insights.

The goal is to build a research assistant that helps investors understand businesses rather than just view financial metrics.

---

# ✨ Features

### 📊 Company Information

- Company Profile
- Business Summary
- Sector & Industry
- Website
- Country

---

### 📈 Market Data

- Live Market Price
- Daily Change
- 52 Week High / Low
- Volume
- Market Capitalization
- Interactive Candlestick Charts

---

### 💰 Financial Statements

- Income Statement
- Balance Sheet
- Cash Flow Statement

Supported Metrics:

- Revenue
- Operating Income
- Net Income
- Assets
- Liabilities
- Equity
- Operating Cash Flow
- Investing Cash Flow
- Financing Cash Flow

---

### 🤖 AI Company Report

Generate a structured equity research report including:

- Business Overview
- Financial Analysis
- Growth Drivers
- Strengths
- Weaknesses
- Risks
- Opportunities
- Investment Outlook
- Company Health Score

---

### 📄 Annual Report RAG

Ask natural language questions directly against a company's annual report.

Example:

> What are TCS's AI initiatives?

The system:

- Parses Annual Reports
- Chunks Documents
- Generates Embeddings
- Stores vectors in ChromaDB
- Retrieves relevant sections
- Uses Groq LLM to answer
- Returns cited source chunks

---

## 🏗 Architecture

```
                        Annual Report PDF
                                │
                                ▼
                       AnnualReportParser
                                │
                                ▼
                           Report Cache
                                │
                                ▼
                           Text Chunker
                                │
                                ▼
                      Embedding Generation
                                │
                                ▼
                            ChromaDB
                                │
                                ▼
                       Retrieval Service
                                │
                                ▼
                    AnnualReportChatService
                                │
                                ▼
                          Groq LLM
                                │
                                ▼
                          Final Answer
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Pydantic v2

---

## AI / LLM

- Groq API
- Llama Models

---

## RAG

- PyMuPDF4LLM
- ChromaDB
- Sentence Transformers

---

## Data Processing

- Pandas
- NumPy

---

## Visualization

- Plotly
- Streamlit

---

## APIs

- Yahoo Finance

---

# 📂 Project Structure

```
StockLens-AI
│
├── app
│   ├── ai
│   ├── api
│   ├── builders
│   ├── core
│   ├── models
│   ├── rag
│   ├── repositories
│   ├── services
│   └── main.py
│
├── frontend
│
├── scripts
│
├── tests
│
├── docs
│
├── data
│   ├── cache
│   ├── reports
│   └── vector_db
│
├── pyproject.toml
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/StockLens-AI.git

cd StockLens-AI
```

Install dependencies

```bash
uv sync
```

Create a `.env`

```
GROQ_API_KEY=your_key
GROQ_MODEL=llama-3.3-70b-versatile
```

---

# ▶ Running the Backend

```bash
uv run python -m app.main
```

FastAPI Docs

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running Streamlit

```bash
uv run python -m streamlit run frontend/main.py
```

---

# 📚 API Endpoints

## Company

```
GET /company
```

---

## Financials

```
GET /financials
```

---

## Market Data

```
GET /market
```

---

## Annual Report Chat

```
POST /annual-report/chat
```

Example Request

```json
{
  "company": "TCS",
  "report_year": 2025,
  "question": "What are TCS AI initiatives?"
}
```

Example Response

```json
{
  "answer": "...",
  "sources": [
    {
      "chunk_id": "TCS_2025_0061",
      "page": 22
    }
  ]
}
```

---

# 🧪 Testing

Run all tests

```bash
pytest
```

Run RAG tests

```bash
uv run python -m scripts.rag.test_retrieval
```

```bash
uv run python -m scripts.rag.test_chat_service
```

---

# 🚧 Roadmap

## ✅ Completed

- Company Information
- Market Data
- Financial Statements
- Financial Charts
- AI Company Report
- Annual Report Parsing
- Document Chunking
- Embeddings
- ChromaDB Integration
- Retrieval Pipeline
- Annual Report Chat API
- Source Citations

---

## 🚀 In Progress

- Streamlit Dashboard Integration
- Better RAG Retrieval
- Improved Prompt Engineering

---

## 📌 Planned

- Company Comparison
- Portfolio Analysis
- Earnings Call Transcript Analysis
- Multi-Document RAG
- AI Watchlists
- Financial Ratio Analysis
- Docker Support
- Authentication
- Deployment
- CI/CD Pipeline

---

# 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.