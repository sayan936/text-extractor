from fastapi import APIRouter, UploadFile
from services.document_loader import extract_text
from services.vectore_store import store_embeddings
from services.chunker import chunk_text
from services.embeddings import embed_chunks


router = APIRouter()
@router.post("/upload")
async def upload_document(file: UploadFile):
    # Step 1: Extract text from the uploaded document
    text = extract_text(file)

    # Step 2: Chunk the extracted text
    chunks = chunk_text(text)

    # Step 3: Generate embeddings for each chunk
    embeddings = embed_chunks(chunks)

    # Step 4: Store the embeddings in the vector store
    store_embeddings(embeddings,chunks)

    return {"message": "Document uploaded and processed successfully."}