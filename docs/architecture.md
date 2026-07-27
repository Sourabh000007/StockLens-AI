# StockLens AI Architecture

## Overview

StockLens AI follows a layered architecture designed for scalability, maintainability, and separation of concerns.

Each layer has a single responsibility, making the application easier to test, extend, and maintain.

---

# High-Level Architecture

```
                         User
                           │
                           ▼
                 Streamlit Frontend
                           │
                           ▼
                    FastAPI Endpoints
                           │
                           ▼
                      Service Layer
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Company Service   Financial Service   Market Service
                           │
                           ▼
                  AnnualReportChatService
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
     Retrieval Service              Prompt Builder
            │                             │
            ▼                             ▼
        ChromaDB                    Groq LLM
            ▲
            │
     Embedding Service
            ▲
            │
      Document Chunker
            ▲
            │
     AnnualReportParser
            ▲
            │
      Annual Report PDF
```

---

# Backend Layers

## API Layer

Responsible for:

- HTTP endpoints
- Request validation
- Response serialization

Examples:

```
app/api/company_routes.py
app/api/financial_routes.py
app/api/market_routes.py
app/api/annual_report_routes.py
```

---

## Service Layer

Contains business logic.

Responsibilities:

- Coordinate repositories
- Call AI services
- Transform data
- Build responses

Examples:

```
CompanyService
FinancialService
MarketService
AnnualReportChatService
```

---

## Repository Layer

Responsible for fetching data from external sources.

Examples:

```
Yahoo Finance
Future NSE APIs
Future News APIs
```

Repositories never contain business logic.

---

## AI Layer

Responsible for:

- Prompt Engineering
- Groq API Communication
- JSON Parsing
- Company Report Generation

```
GroqClient

PromptBuilder

AnswerPromptBuilder
```

---

## RAG Layer

Responsible for:

- PDF Parsing
- Markdown Caching
- Chunking
- Embeddings
- Vector Search
- Retrieval

Pipeline:

```
PDF

↓

Parser

↓

Chunker

↓

Embedding

↓

ChromaDB

↓

Retriever

↓

Prompt Builder

↓

LLM
```

---

## Models

Contains:

- API Models
- Financial Models
- Market Models
- RAG Models

All models use Pydantic.

---

# RAG Pipeline

```
Annual Report PDF

↓

PyMuPDF4LLM Parser

↓

Markdown

↓

Report Cache

↓

Chunking

↓

Sentence Transformer

↓

Embeddings

↓

ChromaDB

↓

Similarity Search

↓

Retrieved Chunks

↓

Prompt Builder

↓

Groq LLM

↓

Answer + Sources
```

---

# Design Principles

StockLens AI follows several software engineering principles:

- Separation of Concerns
- Dependency Injection
- Layered Architecture
- Single Responsibility Principle
- Strong Typing with Pydantic
- Reusable Components
- Testable Services

---

# Future Architecture

Planned additions include:

- Multi-document RAG
- Portfolio Analysis Engine
- Earnings Call Analysis
- Company Comparison
- Authentication
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment