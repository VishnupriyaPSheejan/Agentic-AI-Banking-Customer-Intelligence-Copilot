from pathlib import Path
import pickle
from sklearn.metrics.pairwise import cosine_similarity

ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/"models/rag_index.pkl"

def retrieve(query,k=3):
    with open(INDEX,"rb") as f: idx=pickle.load(f)
    q=idx["vectorizer"].transform([query])
    scores=cosine_similarity(q,idx["matrix"])[0]
    order=scores.argsort()[::-1][:k]
    return [{"source":idx["docs"][i]["source"],"text":idx["docs"][i]["text"],"score":round(float(scores[i]),4)} for i in order]
