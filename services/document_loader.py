import pdfplumber
from fastapi import UploadFile


def extract_text(file: UploadFile) -> str:
    """
    Extract text from an uploaded PDF document.
    """
    if file.content_type != "application/pdf":
        raise ValueError("Unsupported file type. Please upload a PDF document.")

    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text