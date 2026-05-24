# Intelli-Credit: Next-Gen Corporate Credit Appraisal 🏦⚡

**Intelli-Credit** is a production-grade, AI-driven credit underwriting platform built for the Indian corporate ecosystem. It is designed to replace a senior credit manager’s traditional **3-week manual credit appraisal workflow** with a seamless, highly auditable **3-minute AI-orchestrated cycle**. 

Developed for the **IIT Hyderabad Intelli-Credit Challenge**, the platform bridges the intelligence gap in corporate lending by automating financial document ingestion, cross-validating multi-layer tax records, conducting real-time legal/MCA web research, and compiling a regulator-ready **Credit Appraisal Memo (CAM)** with fully traceable citations.

---

## 🎯 Platform Overview

Indian commercial banks face a massive bottleneck in credit underwriting: analyzing **40+ disparate documents** from **8+ different sources** to assess risk. This manual process is slow, opaque, and highly prone to oversight. 

**Intelli-Credit** automates the entire document-to-decision pipeline. By utilizing a hybrid intelligence engine, it reads annual reports, calculates key banking metrics, cross-references digital records for circular trading, scrapes court databases, and synthesizes it all into an explainable credit score.

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ M1: Ingest & Parse     │ ───> │ M2: Agentic Search     │ ───> │ M3: Score & Decide     │
│ • PDF Tables & Ratios  │      │ • MCA Registry Lookup  │      │ • Five-Cs Rubric       │
│ • GST Cross-Check      │      │ • Legal Case Checker   │      │ • Committee CAM PDF    │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

---

## ✨ Key Features & Modules

### 📊 M1: Document Intelligence (Financial Ingestion)
*   **Deep Financial Parsing**: Extracts balance sheets, P&L statements, and cash flows from complex, multi-page PDFs using custom deterministic extraction and advanced OCR fallback.
*   **Key Ratio Analytics**: Automatically computes critical RBI-regulated metrics, including **DSCR**, **Current Ratio**, **Debt-to-Equity**, and **Interest Coverage Ratio**.
*   **GST Cross-Validation**: Simulates GSTR-2A (supplier-reported purchases) vs GSTR-3B (self-declared sales) mismatch analysis to identify fake Input Tax Credits (ITC) and flag potential circular trading networks.

### 🔍 M2: Live Web Research Agent (Market Sentiment)
*   **ReAct Search Engine**: An active, real-time agent powered by **Tavily** that browses news articles to gauge industry sentiment and corporate news.
*   **MCA Registry Verifier**: Automatically verifies the company's registration details, incorporation date, and corporate status directly from Ministry of Corporate Affairs data.
*   **e-Courts Litigation Checker**: Conducts semantic web research to discover pending legal disputes, director litigations, and regulatory penalties.
*   **Hybrid Data Fusion**: Merges extraction data with real-time web facts, performing gap-filling and flagging >15% discrepancies between official documents and public records.

### ⚖️ M3: Decision Engine & Explainability (Scorer)
*   **Transparent Credit Scorecard**: Replaces regulatory-unfriendly "black box" machine learning models with a clear, weighted, 100-point credit rubric aligned with the RBI Early Warning Signals (EWS) framework.
*   **Hard-Reject Guardrails**: Instantly blocks applications if critical legal violations are found or if the company status is marked as struck off, liquidated, or dormant.
*   **Explainable Rationale**: Employs an LLM-synthesized narrative that translates scorecard parameters into standard banking terminology for the credit committee.

### 📑 Regulator-Ready PDF CAM Generator
*   **Instant Export**: Generates a beautiful, professional Credit Appraisal Memo (CAM) dynamically using **ReportLab**.
*   **Detailed Appendices**: Includes executive summaries, rating badges, benchmark checks, news lists, risk warnings, and citation sources.

### 👥 Human-in-the-Loop Integration
*   **Credit Officer Notes**: Enables the underwriter to insert qualitative site-visit observations (e.g., promoter integrity, plant capacity) which adjust scoring weights and limits dynamically.

---

## 📊 Credit Scoring Rubric (Five Cs of Credit)

Intelli-Credit computes a robust **Smart Credit Score (0-100)** distributed evenly across five primary risk domains.

| Component | Weight | Target Parameters | Ideal Benchmark | Deductions & Flags |
| :--- | :---: | :--- | :--- | :--- |
| **1. Liquidity** | 20% | Current Ratio (CR) | `CR > 1.5` | Flagged: `CR < 1.0` (0 points) |
| **2. Solvency** | 20% | Debt-to-Equity (D/E), Interest Coverage Ratio (ICR) | `D/E < 1.5`, `ICR > 3.0` | Flagged: D/E > 3.0 ("Hyphenated Leverage"), Low ICR |
| **3. Efficiency**| 20% | Year-over-Year Revenue Growth | `Growth > 15%` | Flagged: Negative Revenue Growth (Deducts 15 pts) |
| **4. Market Intel**| 20% | MCA Active Status, Public Media Sentiment | Status: Active, Sentiment > 0.70 | Flagged: Inactive status, negative public news |
| **5. Risk Control**| 20% | Litigation Search, Qualitative Threat Assessment | 0 Litigation Cases, < 3 Qualitative Risks | Flagged: Active lawsuits, high count of operational risks |

### 🚦 Decision Thresholds & Actions

> [!NOTE]
> Final ratings are dynamically mapped based on aggregate scorecard performance:

*   🟢 **LEND (Score 76 - 100)**: Auto-approve applications, calculate risk-adjusted credit limit, and suggest a prime interest rate.
*   🟡 **REFER (Score 46 - 75)**: Flag for manual committee review. Demands verification of high-risk components.
*   🔴 **REJECT (Score 0 - 45)**: Automatic system rejection. Triggered by a low cumulative score or critical "Hard-Reject" flags (e.g., Inactive MCA Status).

---

## 🎨 Technology Stack

The platform is built on a highly modular, decoupled stack designed for sub-second API updates and premium aesthetics:

### ⚙️ Backend Core
*   **FastAPI**: High-performance, asynchronous Python web framework for handling background calculations.
*   **ReportLab**: Enterprise-grade PDF generator for rendering the finalized Credit Appraisal Memos.
*   **Uvicorn**: Lightning-fast ASGI web server implementation.
*   **Pandas & NumPy**: For financial computations and trend calculations.

### 🧠 AI & LLM Orchestration
*   **High-Availability LLM Gateway**: Custom cascading router with failover logic: **Google Gemini Suite** (cascades through 7 models: 2.5-Flash, 1.5-Flash, 1.5-Pro, etc.) ➔ **Groq (Llama 3 70B)** ➔ **OpenRouter** ➔ **Local Ollama (Mistral)**.
*   **Tavily Search API**: Specialized search engine tuned to return structural data formats for LLM agents.
*   **OCR Parsing**: Robust extraction using `pdfplumber` for text-based reports with fallback architectures.

### 🖥️ Premium Frontend Dashboard
*   **Vanilla HTML5 & JavaScript**: Lightweight client-side application with no external compile-time dependencies.
*   **CSS Custom Properties**: A bespoke, responsive styling system featuring vibrant dark-mode gradients and **glassmorphism** effects.
*   **Axios**: For managing asynchronous HTTP requests.

---

## 🗂️ Project Structure

```
diyaj14/INTELLI-CREDIT/
├── backend/
│   ├── app.py                  # Unified FastAPI API and file router
│   ├── orchestrator.py         # Ingestion-to-Decision workflow orchestrator
│   ├── check_module1.py        # Local testing module for extraction pipeline
│   └── minimal_test.py         # Minimal integration runner
│
├── frontend/
│   ├── index.html              # Landing Page & Pitch Desk
│   ├── dashboard.html          # Interrogative Credit Officer Dashboard
│   ├── report.html             # Explanatory Rating & Verification Report UI
│   ├── api-docs.html           # Developer API Documentation
│   ├── architecture.html       # Medallion & Agentic System Architecture UI
│   ├── features.html           # Feature details
│   ├── case-studies.html       # Case studies
│   ├── app.js                  # Frontend API state management & event loop
│   ├── style.css               # Bespoke credit portal design system
│   └── landing.css             # Glassmorphic marketing styling
│
├── modules/
│   ├── llm_gateway.py          # Cascading LLM client (Gemini ➔ Groq ➔ OpenRouter ➔ Ollama)
│   ├── document_intelligence/  # Ingests and processes annual statements
│   │   ├── document_pipeline.py
│   │   ├── ingestor.py
│   │   └── extractor.py
│   ├── research_agent/         # Active Tavily crawler for sentiment and MCA
│   │   ├── research_pipeline.py
│   │   ├── search_engine.py
│   │   └── hybrid_merger.py    # Merges PDF & Web data and identifies discrepancies
│   ├── credit_scoring/         # RBI EWS and Five Cs scoring logic
│   │   ├── scorecard.py
│   │   └── recommendation.py
│   └── report_generator/       # Renders report details to CAM PDF
│       └── pdf_generator.py
│
├── Dockerfile                  # Production containerization
├── Procfile                    # Heroku/Render process script
├── railway.json                # Railway cloud configuration
├── requirements.txt            # Package dependencies
├── .env.example                # Template for server API configuration
└── .gitignore                  # Production Git exclusions
```

---

## 🚀 Quick Start & Local Setup

### Prerequisites
*   **Python 3.11+** installed locally.
*   A terminal shell (PowerShell or Bash).

### 1. Clone the Repository
```bash
git clone https://github.com/diyaj14/INTELLI-CREDIT.git
cd INTELLI-CREDIT
```

### 2. Configure the Environment
Copy the example environment file and open `.env` to configure your API keys:
```bash
cp .env.example .env
```
Update the keys in your `.env` file:
```env
# Gemini API Key (Recommended for primary performance)
GOOGLE_API_KEY=AIzaSy...

# Web Research API (Required for web news and litigation)
TAVILY_API_KEY=tvly-...

# Groq API Key (Secondary fallback)
GROQ_API_KEY=gsk_...

# OpenRouter Key (Tertiary fallback)
OPENROUTER_API_KEY=sk-or-v1-...
```
*(If no API keys are available, Intelli-Credit will automatically fall back to search simulations and pre-cached demonstration assets).*

### 3. Install Dependencies
Create and activate a Python virtual environment:
```bash
# Set up virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Bash/Mac/Linux)
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt
```

### 4. Start the Application
Run the unified FastAPI server:
```bash
python backend/app.py
```
The application will launch on **`http://localhost:8001`**. 

Open your browser and navigate to `http://localhost:8001/` to access the Landing Page. Click **"Start Analysis"** to enter the Credit Officer Dashboard!

---

## 🔌 API Endpoints

The backend exposes simple, structured REST endpoints:

*   **`POST /analyze`**: Starts the asynchronous pipeline.
    *   *Parameters*: `files` (Uploaded PDFs/Excels), `company_name` (Target corporate), `promoter_names` (Comma-separated director names), `primary_insights` (Human site notes), `demo_mode` (Toggle simulation), `llm_provider` (Override model preference).
    *   *Response*: Returns a unique `session_id`.
*   **`GET /status/{session_id}`**: Retrieves the active progress stage (0-100%) and the final results upon completion.
*   **`GET /reports/{filename}`**: Downloads the generated PDF Credit Appraisal Memo.
*   **`GET /assets/{filename}`**: Serves static asset files to the client interface.

---

## 🏗️ Production Readiness & Scalability

While the prototype uses SQLite and local file buffers, the architecture is mapped to enterprise specifications:

### 💎 Databricks Medallion Architecture
Intelli-Credit is fully designed to utilize **Delta Lake** schemas:
1.  **Bronze Layer**: Captures raw ingested documents (annual reports, scanned PDF packages, JSON raw web responses) with full audit paths.
2.  **Silver Layer**: Features clean, tabular data tables extracted by table parsers, parsed transaction records, and verified entity relationships.
3.  **Gold Layer**: Synthesizes feature-engineered arrays, computed accounting ratios, consolidated corporate flags, and ML-ready risk indicators.

```
Ingested PDFs / Web Snippets ➔ [Bronze Delta Lake] ➔ Tabular Data / Entities ➔ [Silver Delta Lake] ➔ Ratios / ML Scores ➔ [Gold Delta Lake]
```

### 📈 Scaling for Enterprise Volume
*   **Asynchronous Processing**: Offload PDF processing and scrapers to **Celery** workers backed by an **Apache Kafka** or **RabbitMQ** event queue.
*   **Fast Caching**: Deploy **Redis** to cache frequent Tavily search queries and corporate registry hits (TTL 24 hours).
*   **Database Partitioning**: Migrate SQLite to **PostgreSQL** in production with schema sharding organized by region/postal zones.
*   **Model Lineage**: Integrates with **MLflow** to track prompt versioning, scoring coefficient tuning, and extraction accuracy thresholds.

---

## 🛡️ Security, Privacy & RBI Compliance

*   ✅ **RBI EWS Alignment**: Built in strict alignment with RBI circular *RBI/2015-16/75 (Early Warning Signals)* to detect early corporate distress.
*   ✅ **Consent Management**: Architected to sit on top of the **Account Aggregator (AA) Ecosystem** (Sahamati framework), ensuring no financial data is pulled without explicit, cryptographic taxpayer consent.
*   ✅ **Data Minimization**: PII details (directors, promoters, pan codes) are hashed and masked, leaving only the computed risk vectors visible.
*   ✅ **Audit Integrity**: Every credit recommendation generated by the LLM is cited using page numbers and live URL footprints to eliminate hallucination liabilities.

---

## 👥 Hackathon Context & Wow Factors

Built for **IIT Hyderabad's Intelli-Credit Challenge** to show how state-of-the-art AI solves real-world underwriting gaps:

1.  **"3 Weeks vs. 3 Minutes" Live Timer**: Built-in stopwatch in the UI proves operational efficiency in real time.
2.  **Explainable Scoring Dashboard**: Shows exact scoring deductions so that decisions are never black boxes.
3.  **Simulation Demo Mode**: Pre-loaded mock scenarios ("Apex Textiles Pvt Ltd") demonstrating the pipeline's behavior in high-risk scenarios.
4.  **Automatic Safe-Key Check**: Enhanced repository guardrails prevent key leaks while maintaining a fully transparent setup environment.

---

**Built with ❤️ for the IIT Hyderabad Intelli-Credit Challenge.**
