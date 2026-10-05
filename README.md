# Agentic AI Banking Customer Intelligence & Risk Copilot

A portfolio-grade **GenAI + RAG + Agentic AI** banking solution designed around customer 360 intelligence, financial risk signals and next-best-product recommendations.

The application is intentionally **API-key-free by default**. It uses a deterministic local retrieval and agent framework so anyone can clone the repository and see the full workflow immediately.

Optional LLM integration can be added later without changing the agent interfaces.

## Business problem

Relationship managers and customer-success teams often need to answer several questions before engaging a customer:

1. What is happening with the customer?
2. Is there an emerging financial-risk signal?
3. Why is engagement changing?
4. Which product or action may be relevant?
5. Which policy or product information supports the recommendation?
6. Can the reasoning be explained with evidence?

This project creates a Customer 360 Copilot that combines:

- Structured customer/account/transaction data
- Unstructured product and policy documents
- Predictive risk and churn signals
- Recommendation logic
- RAG retrieval
- Multi-agent orchestration
- Critic/validation step
- Explainable final response

## Agent architecture

```text
                    User Question
                         │
                         ▼
                 ┌───────────────┐
                 │ Orchestrator  │
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
   Customer 360      Risk Agent   Recommendation
      Agent                            Agent
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  RAG Policy Agent
                         │
                         ▼
                 Financial Insights
                         │
                         ▼
                 Critic / Validator
                         │
                         ▼
                  Final Copilot
```

## OCBC-relevant capabilities

- GenAI copilot
- RAG
- Agentic AI
- Recommendation systems
- Predictive modelling
- NLP
- Customer engagement
- Structured + unstructured data
- Financial risk signals
- Data storytelling
- Explainable AI
- Evaluation and guardrails

## Run locally

### Python

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python src/generate_data.py
python src/build_index.py
streamlit run src/app.py
```

Open:
http://localhost:8501

### Docker

```bash
docker compose up --build
```

Open:
http://localhost:8501

No API key is required.

## Example questions

Try:

- `Why is this customer's financial engagement declining?`
- `What are the main risk signals for CUST-000017?`
- `What product could be relevant to this customer?`
- `Give me a customer 360 summary for CUST-000017`
- `What evidence supports the recommendation?`

## RAG design

The local RAG pipeline uses:

1. Product/policy documents
2. Text chunking
3. TF-IDF vectorization
4. Cosine similarity retrieval
5. Top-k evidence selection
6. Agent response generation

The design can later be swapped for:

- Vertex AI Vector Search
- FAISS
- Pinecone
- OpenSearch
- pgvector

without changing the business-agent interfaces.

## Predictive layer

The project includes:

- Financial risk score
- Engagement/churn probability
- Customer segmentation
- Next-best-product recommendation

These are generated from synthetic data and are intended for demonstration only.

## Project structure

```text
agentic-ai-banking-customer-intelligence-copilot/
├── data/
│   ├── customers.csv
│   ├── transactions.csv
│   ├── products.csv
│   └── knowledge_base/
├── src/
│   ├── generate_data.py
│   ├── build_index.py
│   ├── data_layer.py
│   ├── retriever.py
│   ├── agents.py
│   ├── orchestrator.py
│   ├── app.py
│   └── evaluation.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Safety / responsible AI

This is not a real banking decision system. It does not use real customer data and must not be used to approve/decline financial products.

For production banking deployment, additional controls would be required for:

- PII handling
- access control
- audit trails
- model risk management
- fairness testing
- human approval
- hallucination detection
- prompt injection protection
- regulatory compliance
- explainability
