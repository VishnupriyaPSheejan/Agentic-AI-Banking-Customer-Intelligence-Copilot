from data_layer import customer_360
from retriever import retrieve

def customer_360_agent(customer_id):
    c=customer_360(customer_id)
    return {
        "customer_id":customer_id,
        "summary":(
            f"Customer earns approximately ${c['monthly_income']:,.0f}/month, has "
            f"${c['savings_balance']:,.0f} savings, {c['transaction_count']} observed transactions, "
            f"engagement score {c['engagement_score']:.2f}, and {c['churn_probability']:.0%} estimated churn probability."
        ),
        "data":c
    }

def risk_agent(customer_id):
    c=customer_360(customer_id)
    signals=[]
    if c["credit_utilization"]>.70: signals.append("high credit utilization")
    if c["payment_delay_days"]>7: signals.append("frequent payment delays")
    if c["loan_count"]>=4: signals.append("multiple active loans")
    if c["churn_probability"]>.60: signals.append("elevated disengagement/churn probability")
    return {"risk_level":c["risk_level"],"signals":signals or ["no dominant risk signal detected"]}

def recommendation_agent(customer_id):
    c=customer_360(customer_id)
    if c["credit_utilization"]>.70:
        return {"recommendation":"Savings Plus","reason":"Prioritize liquidity and savings rather than additional revolving credit."}
    if c["engagement_score"]<.45:
        return {"recommendation":"Everyday Cashback Card","reason":"Explore an eligible engagement-oriented proposition based on observed everyday spend."}
    if c["savings_balance"]>20000 and c["engagement_score"]>.65:
        return {"recommendation":"Wealth Starter","reason":"The customer shows stronger savings capacity and engagement; suitability should be assessed."}
    return {"recommendation":"Savings Plus","reason":"Savings-oriented proposition is the conservative next-best-action candidate."}

def rag_agent(question):
    return retrieve(question,3)

def critic_agent(result):
    issues=[]
    if not result["evidence"]: issues.append("No evidence retrieved.")
    if result["recommendation"]["recommendation"]=="Personal Instalment Loan" and result["risk"]["risk_level"]=="High":
        issues.append("High-risk customers should not be pushed toward additional credit.")
    return {"passed":not issues,"issues":issues}
