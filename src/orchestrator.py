from agents import customer_360_agent,risk_agent,recommendation_agent,rag_agent,critic_agent

def run(customer_id,question):
    c=customer_360_agent(customer_id)
    risk=risk_agent(customer_id)
    rec=recommendation_agent(customer_id)
    evidence=rag_agent(question+" "+rec["recommendation"])
    result={"customer":c,"risk":risk,"recommendation":rec,"evidence":evidence}
    result["critic"]=critic_agent(result)
    return result

def narrative(result):
    c=result["customer"]; r=result["risk"]; rec=result["recommendation"]
    ev=result["evidence"]
    evidence="; ".join(f"{x['source']} ({x['score']:.2f})" for x in ev)
    return (
        f"**Customer 360:** {c['summary']}\n\n"
        f"**Risk assessment:** {r['risk_level']} risk. Key signals: {', '.join(r['signals'])}.\n\n"
        f"**Next-best-action candidate:** {rec['recommendation']}. {rec['reason']}\n\n"
        f"**Evidence retrieved:** {evidence}\n\n"
        f"**Validation:** {'Passed' if result['critic']['passed'] else 'Review required — ' + ', '.join(result['critic']['issues'])}.\n\n"
        f"*This is a synthetic portfolio demonstration, not a financial decision.*"
    )
