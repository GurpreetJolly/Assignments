import numpy as np
from mistralai.client import Mistral
#import os

print("\n\n")
print("*************************************")
print("********** Semantic Search **********")

#print(f"Current directory: {os.getcwd()}")

# Step 1: Create embeddings for documents
def get_embedding(text, client):
    response = client.embeddings.create(
        model = "mistral-embed",
        inputs = text
    )
    return np.array(response.data[0].embedding)


# Step 2: Cosine similarity function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Step 3: Search function
def semantic_search(query, documents, doc_embeddings, client, top_k=2):
    query_embedding = get_embedding(query, client)

    similarities = []
    for i, emb in enumerate(doc_embeddings):
        sim = cosine_similarity(query_embedding, emb)
        similarities.append((documents[i], sim))

    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_k]


def main():
    api_key = None
    with open("./assignment_20260301_sentiment_analysis/mistral_api_key", "r") as file:
        api_key = file.read().strip()
    client = Mistral(api_key=api_key)

    # Example documents
    documents = [
        "Cats are small domesticated carnivorous mammals.",
        "Dogs are loyal animals often kept as pets.",
        "Artificial intelligence enables machines to learn from data.",
        "Neural networks are used in deep learning systems.",
        "Pizza is a popular Italian dish with cheese and tomato sauce."
    ]
    doc_embeddings = [get_embedding(doc, client) for doc in documents]

    # Step 4: Run search
    query = "Does dogs like cats"  #"machine learning algorithms"

    results = semantic_search(query, documents, doc_embeddings, client)

    print("Query:", query)
    print("\nTop Results:\n")

    for doc, score in results:
        print(f"{score:.3f} - {doc}")

if __name__ == "__main__":
    main()


# # Step 4: Run search
# query = "machine learning algorithms"

# results = semantic_search(query)

# print("Query:", query)
# print("\nTop Results:\n")

# for doc, score in results:
#     print(f"{score:.3f} - {doc}")