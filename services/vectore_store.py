import faiss
import numpy as np


EMBEDDING_DIMENSION = 384
index = faiss.IndexFlatL2(EMBEDDING_DIMENSION)
text_chunks = []



def store_embeddings(embeddings: list, chunks: list):
    global text_chunks
    index.add(np.array(embeddings) )
    text_chunks.extend(chunks)


def retrieve_chunks(query: str, top_k: int = 5) -> list:
    from services.embeddings import model

    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, top_k)
    print(indices)
    # Filter out invalid indices (-1) and return valid chunks
    valid_indices = [i for i in indices[0] if i >= 0]
    return [text_chunks[i] for i in valid_indices]