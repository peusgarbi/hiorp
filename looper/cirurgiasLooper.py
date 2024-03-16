from parser.cirurgias import dividir_salas, dividir_cirurgias_da_sala, extrair_info_de_cirurgia
from parser.cirurgias import Cirurgia
from typing import List

def loop_pelas_cirurgias(full_text: str) -> List[Cirurgia]:
    salas_list = dividir_salas(full_text)
    cirurgias: List[Cirurgia] = []

    for sala in salas_list:
        cirurgias_da_sala = dividir_cirurgias_da_sala(sala)

        for cirurgia in cirurgias_da_sala:
            info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
            cirurgias.append(info_da_cirurgia)

    return cirurgias
