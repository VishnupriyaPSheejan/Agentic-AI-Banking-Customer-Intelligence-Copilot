from pathlib import Path
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
KB=DATA/"knowledge_base"
DATA.mkdir(exist_ok=True); KB.mkdir(exist_ok=True)

def main(seed=42,n=2500):
    rng=np.random.default_rng(seed)
    customers=pd.DataFrame({
        "customer_id":[f"CUST-{i:06d}" for i in range(1,n+1)],
        "age":rng.integers(21,76,n),
        "monthly_income":np.maximum(1800,rng.lognormal(np.log(5200),.45,n)).round(2),
        "savings_balance":np.maximum(100,rng.lognormal(np.log(9000),.9,n)).round(2),
        "credit_utilization":np.clip(rng.beta(2.2,3.2,n),.01,.99).round(4),
        "monthly_transactions":rng.poisson(32,n)+2,
        "payment_delay_days":rng.poisson(2.3,n),
        "loan_count":rng.integers(0,6,n),
        "card_spend":np.maximum(50,rng.lognormal(np.log(1800),.7,n)).round(2),
        "engagement_score":np.clip(rng.normal(.65,.18,n),.05,.99).round(3),
    })
    churn_score=2.2*(1-customers.engagement_score)+.5*customers.credit_utilization+.06*customers.payment_delay_days-.00002*customers.savings_balance
    churn_prob=1/(1+np.exp(-(churn_score-1.0)))
    customers["churn_probability"]=np.clip(churn_prob,0.01,.99).round(4)
    customers["risk_level"]=np.select(
        [customers.credit_utilization>.70, customers.payment_delay_days>7, customers.loan_count>=4],
        ["High","High","Medium"],default="Low")
    customers.to_csv(DATA/"customers.csv",index=False)

    tx=[]
    categories=["grocery","travel","utilities","retail","dining","health","education","electronics"]
    channels=["card","online","branch","atm","wallet"]
    for i in range(n*4):
        cid=rng.choice(customers.customer_id)
        tx.append((f"TXN-{i+1:08d}",cid,round(float(rng.lognormal(4.2,1)),2),rng.choice(categories),rng.choice(channels)))
    pd.DataFrame(tx,columns=["transaction_id","customer_id","amount","category","channel"]).to_csv(DATA/"transactions.csv",index=False)

    products=pd.DataFrame([
        ["P01","Savings Plus","savings","Higher-interest savings account for customers building balances."],
        ["P02","Travel Rewards Card","card","Card designed for customers with frequent travel and eligible spend."],
        ["P03","Personal Instalment Loan","loan","Structured personal financing subject to affordability and eligibility assessment."],
        ["P04","Wealth Starter","investment","Entry-level investment solution for eligible customers with longer-term goals."],
        ["P05","Everyday Cashback Card","card","Cashback card for eligible everyday retail and dining spend."]
    ],columns=["product_id","product_name","category","description"])
    products.to_csv(DATA/"products.csv",index=False)

    docs={
      "savings_policy.txt":"Savings Plus is intended for eligible customers who want to build liquid savings. Suitability should consider customer needs, affordability and product eligibility.",
      "cards_policy.txt":"Card recommendations should consider customer spending patterns, eligibility, affordability and responsible credit usage. Avoid recommending additional credit solely because utilization is already high.",
      "loans_policy.txt":"Personal financing recommendations require affordability assessment, existing obligations and applicable eligibility checks. A copilot should not make an approval decision.",
      "wealth_policy.txt":"Investment discussions should consider customer goals, time horizon, risk profile and suitability. Recommendations require appropriate review.",
      "customer_service_policy.txt":"Customer-facing AI should explain its reasoning, cite supporting information and route uncertain or high-impact decisions to a human colleague."
    }
    for fn,txt in docs.items(): (KB/fn).write_text(txt)
    print(f"Generated banking dataset at {DATA}")

if __name__=="__main__": main()
