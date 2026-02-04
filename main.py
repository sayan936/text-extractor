from fastapi import FastAPI
from api import upload ,qa


app = FastAPI()
app.include_router(upload.router, prefix="/documents", tags=["upload"])
app.include_router(qa.router, prefix="/qa", tags=["qa"])
