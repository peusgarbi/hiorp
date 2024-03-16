import PyPDF2
import os

def extrair_texto(file_dir: str) -> str:
    text = ""
    with open(file_dir, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text
