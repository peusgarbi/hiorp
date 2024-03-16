from parser.cirurgias import  pegar_procedimentos_e_ordenar_alfabeticamente
from extractor.cirurgiasPdfExtractor import extrair_texto
from looper.cirurgiasLooper import loop_pelas_cirurgias

texto_total_extraido = extrair_texto("documento.pdf")
cirurgias = loop_pelas_cirurgias(texto_total_extraido)
procedimentos = pegar_procedimentos_e_ordenar_alfabeticamente(cirurgias[0].servicos)
print(procedimentos)
