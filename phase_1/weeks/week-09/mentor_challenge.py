# Goal: sort a document according to the highest scores
# Input: list of dictionaries
# Output: a document sorted from highest scores
# Steps: go through documents and return a new document sorted by scores from highest
# Python concepts:sorted(), lambda, reverse 

documents = [
    {"title": "Python Basics", "score": 0.72},
    {"title": "AI Agents", "score": 0.95},
    {"title": "Git Guide", "score": 0.61},
    {"title": "RAG Systems", "score": 0.88}
]

sorted_documents = sorted(documents, key= lambda doc: doc["score"], reverse= True)
print(sorted_documents)