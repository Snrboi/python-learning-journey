from functools import reduce

documents = [
    {"title": "Python Basics", "score": 0.72, "words": 1200},
    {"title": "Machine Learning", "score": 0.91, "words": 2400},
    {"title": "RAG Systems", "score": 0.87, "words": 1800},
    {"title": "AI Agents", "score": 0.95, "words": 3100},
    {"title": "Neural Networks", "score": 0.83, "words": 2700}
]

highest_score = reduce(lambda a, b: a if a["score"] > b["score"] else b, documents)
total_words = reduce(lambda a, b: a + b["words"], documents, 0)
scores = reduce(lambda a, b: a + b["score"] , documents, 0)
average_scores = scores / len(documents)

print(highest_score)
print(total_words)
print(average_scores)