from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"

def load():
    return (
        pd.read_csv(DATA/"customers.csv"),
        pd.read_csv(DATA/"transactions.csv"),
        pd.read_csv(DATA/"products.csv")
    )

def customer_360(customer_id):
    customers,tx,products=load()
    c=customers[customers.customer_id==customer_id]
    if c.empty: raise ValueError("Customer not found")
    c=c.iloc[0].to_dict()
    t=tx[tx.customer_id==customer_id]
    category=t.groupby("category")["amount"].sum().sort_values(ascending=False).head(5).to_dict()
    c["top_spend_categories"]=category
    c["transaction_count"]=len(t)
    c["average_transaction"]=round(float(t.amount.mean()),2) if len(t) else 0
    return c
