def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    """
    Splits the input text into chunks of specified size with overlap.

    :param text: The input text to be chunked.
    :param chunk_size: The size of each chunk.
    :param overlap: The number of overlapping characters between chunks.
    :return: A list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks