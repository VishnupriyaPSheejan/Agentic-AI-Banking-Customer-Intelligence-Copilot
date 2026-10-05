import streamlit as st
import pandas as pd
from data_layer import load
from orchestrator import run,narrative

st.set_page_config(page_title="Banking Customer Intelligence Copilot",layout="wide")
st.title("🏦 Agentic AI Banking Customer Intelligence Copilot")
st.caption("GenAI-style banking copilot | RAG | Multi-agent reasoning | Synthetic data | No API key required")

customers,transactions,products=load()

col1,col2=st.columns([1,2])
with col1:
    customer_id=st.selectbox("Customer",customers.customer_id.tolist())
    question=st.text_area("Ask the copilot", "Why is this customer's financial engagement changing?")
    run_btn=st.button("Run Agentic Analysis",type="primary")
with col2:
    c=customers[customers.customer_id==customer_id].iloc[0]
    a,b,d,e=st.columns(4)
    a.metric("Risk",c.risk_level)
    b.metric("Churn probability",f"{c.churn_probability:.0%}")
    d.metric("Engagement",f"{c.engagement_score:.0%}")
    e.metric("Credit utilization",f"{c.credit_utilization:.0%}")
    spend=transactions[transactions.customer_id==customer_id].groupby("category")["amount"].sum().sort_values(ascending=False).head(7)
    st.bar_chart(spend)

if run_btn:
    result=run(customer_id,question)
    st.divider()
    st.subheader("Agentic AI response")
    st.markdown(narrative(result))
    with st.expander("Agent trace"):
        st.json(result)
    st.subheader("Retrieved evidence")
    for e in result["evidence"]:
        st.write(f"**{e['source']}** — similarity {e['score']}")
        st.caption(e["text"])
