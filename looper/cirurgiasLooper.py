from parser.cirurgias import dividir_salas, dividir_cirurgias_da_sala, extrair_info_de_cirurgia
from parser.cirurgias import Cirurgia
from pydantic import BaseModel
from typing import List

class Cirurgias(BaseModel):
    sala1: List[Cirurgia]
    sala2: List[Cirurgia]
    sala3: List[Cirurgia]
    sala4: List[Cirurgia]
    sala5: List[Cirurgia]

def loop_pelas_cirurgias(full_text: str) -> Cirurgias:
    salas_list = dividir_salas(full_text)

    sala1: List[Cirurgia] = []
    sala2: List[Cirurgia] = []
    sala3: List[Cirurgia] = []
    sala4: List[Cirurgia] = []
    sala5: List[Cirurgia] = []

    cirurgias_da_sala1 = dividir_cirurgias_da_sala(salas_list.sala1)
    for cirurgia in cirurgias_da_sala1:
        info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
        sala1.append(info_da_cirurgia)

    cirurgias_da_sala2 = dividir_cirurgias_da_sala(salas_list.sala2)
    for cirurgia in cirurgias_da_sala2:
        info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
        sala2.append(info_da_cirurgia)

    cirurgias_da_sala3 = dividir_cirurgias_da_sala(salas_list.sala3)
    for cirurgia in cirurgias_da_sala3:
        info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
        sala3.append(info_da_cirurgia)

    cirurgias_da_sala4 = dividir_cirurgias_da_sala(salas_list.sala4)
    for cirurgia in cirurgias_da_sala4:
        info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
        sala4.append(info_da_cirurgia)

    cirurgias_da_sala5 = dividir_cirurgias_da_sala(salas_list.sala5)
    for cirurgia in cirurgias_da_sala5:
        info_da_cirurgia = extrair_info_de_cirurgia(cirurgia)
        sala5.append(info_da_cirurgia)

    return Cirurgias(sala1=sala1, sala2=sala2, sala3=sala3, sala4=sala4, sala5=sala5)
