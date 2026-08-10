documents = [
    "Python basics",
    "",
    "Machine learning",
    "",
    "AI agents"
]

new_document = [document for document in documents if document != ""]

print(new_document)

# creating a new filtered list may be better at times because the new list contains clean data but the old list may contain data that if fixed may be useful but deleting it gets rid of it forever so filtering the skewed entries into a new list while preserving the old one may be ideal.