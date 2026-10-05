from pathlib import Path
import json
from orchestrator import run

ROOT=Path(__file__).resolve().parents[1]

def evaluate():
    questions=[
        "customer credit card recommendation",
        "loan affordability and existing obligations",
        "savings eligibility",
        "investment suitability",
        "customer service AI explanation"
    ]
    scores=[]
    for q in questions:
        result=run("CUST-000017",q)
        scores.append({
            "question":q,
            "evidence_retrieved":len(result["evidence"]),
            "critic_passed":result["critic"]["passed"]
        })
    out={"tests":len(scores),"critic_pass_rate":sum(x["critic_passed"] for x in scores)/len(scores),"cases":scores}
    (ROOT/"models").mkdir(exist_ok=True)
    (ROOT/"models/evaluation.json").write_text(json.dumps(out,indent=2))
    return out

if __name__=="__main__":
    print(json.dumps(evaluate(),indent=2))
