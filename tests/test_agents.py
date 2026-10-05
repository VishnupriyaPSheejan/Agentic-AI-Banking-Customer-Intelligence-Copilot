import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))

def test_local_agent_pipeline():
    from generate_data import main
    from build_index import build
    main(n=100)
    build()
    from orchestrator import run
    result=run("CUST-000017","customer savings and product eligibility")
    assert "customer" in result
    assert "evidence" in result
    assert len(result["evidence"]) > 0
