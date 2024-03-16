import PyPDF2

def extrair_texto(pdf_path: str) -> str:
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

texto_extraido = extrair_texto('documento.pdf')
print(texto_extraido)
