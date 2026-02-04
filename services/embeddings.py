from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks: list) -> list:
    """
    Generates embeddings for a list of text chunks.

    :param chunks: A list of text chunks.
    :return: A list of embeddings corresponding to each chunk.
    """
    embeddings = model.encode(chunks)
    return embeddings