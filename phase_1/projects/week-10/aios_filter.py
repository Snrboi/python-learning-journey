from functools import reduce

documents = [
    {"title": "Python Basics", "score": 0.72},
    {"title": "Machine Learning", "score": 0.91},
    {"title": "RAG Systems", "score": 0.87},
    {"title": "AI Agents", "score": 0.95},
    {"title": "Neural Networks", "score": 0.83}
]

filtered = reduce(lambda a, b: a if a["score"] > b["score"] else b, documents)

print(filtered)