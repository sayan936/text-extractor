from fastapi import APIRouter
from pydantic import BaseModel
from services.vectore_store import retrieve_chunks
from services.llm import generate_answer


router =  APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    # Retrieve relevant context from the vector store
    chunks = retrieve_chunks(request.question)
    context = "\n".join(chunks)
    # Generate an answer using the LLM
    answer = generate_answer(context,request.question)

    return {"answer": answer}