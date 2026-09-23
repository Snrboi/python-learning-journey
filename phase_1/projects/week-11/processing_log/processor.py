def add_doc():
    try:
        document_name = input("Document Name: ").strip()
        token_count = int(input("Token Count: ").strip())
    except ValueError:
        print("Token count must be a number")
    else: 
        if token_count >= 0 and token_count <= 5000:
            if document_name:
                with open("/home/dell/python-learning-journey/phase_1/projects/week-11/processing_log/processed_document.txt", "a", encoding="utf-8") as file:
                    file.write(document_name + " | " + str(token_count) + "\n")
                print("Document processed successfully")
            else:
                print("Invalid document name")
        else:
            print("Invalid token count! Must be between 0 - 5000")


def view_doc():
    try:
        with open("processed_document.txt", "r", encoding="utf-8") as file:
            documents = file.readlines()
    except FileNotFoundError:
        print("No Processing history found")
    else:
        if documents:
            print("===Processing History===")
            for number, doc in enumerate(documents, start=1):
                print(f"{number}. {doc.strip()}")
            doc_summary()
        else:
            print("No Processing history found")


def doc_summary():
    try:
        with open("processed_document.txt", "r", encoding="utf-8") as file:
            documents = file.readlines()
    except FileNotFoundError:
        print("No Processing history found")
    else:
        summary = []
        if documents:
            for doc in documents:
                try:
                    new_doc = doc.split("|")
                    summary_doc = int(new_doc[1].strip())
                    summary.append(summary_doc)
                except ValueError:
                    print(f"Skipping invalid doc: {doc.strip()}")
            print("===Summary===")
            print(f"Documents processed: {len(summary)}")
            print(f"Total Tokens: {sum(summary)}")
            print(f"Average tokens: {round(sum(summary) / len(summary))}")
        else:
            print("No processing history found") #putting this conditional just in case it this function is not called inside view_doc