import PyPDF2
import os

def extrair_texto(file_name: str) -> str:
    diretorio_atual = os.getcwd()
    pdf_path = os.path.join(diretorio_atual,  "pdfs", file_name)

    text = ""
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text
