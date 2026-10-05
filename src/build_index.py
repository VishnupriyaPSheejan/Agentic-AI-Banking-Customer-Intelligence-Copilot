from pathlib import Path
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT=Path(__file__).resolve().parents[1]
KB=ROOT/"data/knowledge_base"
MODEL=ROOT/"models"
MODEL.mkdir(exist_ok=True)

def build():
    docs=[]
    for p in sorted(KB.glob("*.txt")):
        docs.append({"source":p.name,"text":p.read_text()})
    vectorizer=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
    matrix=vectorizer.fit_transform([d["text"] for d in docs])
    with open(MODEL/"rag_index.pkl","wb") as f:
        pickle.dump({"vectorizer":vectorizer,"matrix":matrix,"docs":docs},f)
    print(f"Indexed {len(docs)} knowledge documents.")

if __name__=="__main__": build()
