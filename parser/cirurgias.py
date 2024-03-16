from typing import List, Optional
from pydantic import BaseModel
import re

def extrair_data_das_cirurgias(texto: str) -> str:
    data_regex = re.compile(r"Data: (.*?)\s")
    return data_regex.findall(texto)[0].strip()

class Salas(BaseModel):
    sala1: str
    sala2: str
    sala3: str
    sala4: str
    sala5: str

def dividir_salas(texto: str) -> Salas:
    sala1regex = re.compile(r"Sala de Cirurgia 01(.*?)Sala de Cirurgia 02", re.DOTALL)
    sala2regex = re.compile(r"Sala de Cirurgia 02(.*?)Sala de Cirurgia 03", re.DOTALL)
    sala3regex = re.compile(r"Sala de Cirurgia 03(.*?)Sala de Cirurgia 04", re.DOTALL)
    sala4regex = re.compile(r"Sala de Cirurgia 04(.*?)Sala de Cirurgia 05", re.DOTALL)
    sala5regex = re.compile(r"Sala de Cirurgia 05(.*?)$", re.DOTALL)

    data = {
        "sala1": sala1regex.findall(texto)[0],
        "sala2": sala2regex.findall(texto)[0],
        "sala3": sala3regex.findall(texto)[0],
        "sala4": sala4regex.findall(texto)[0],
        "sala5": sala5regex.findall(texto)[0],
    }

    return Salas(**data)

def dividir_cirurgias_da_sala(texto: str) -> List[str]:
    regex1 = re.compile(r"(Horário:.*?)(?=Horário:|$)", re.DOTALL)
    return regex1.findall(texto)

class Cirurgia(BaseModel):
    horario: str
    paciente: str
    idade: str
    nascimento: str
    cirurgiao: str
    acomodacao: str
    convenio: str
    servicos: str

def extrair_info_de_cirurgia(texto: str) -> Cirurgia:
    horario_regex = re.compile(r"Horário: (.*?) Paciente", re.DOTALL)
    paciente_regex = re.compile(r"Paciente: (.*?) Idade", re.DOTALL)
    idade_regex = re.compile(r"Idade: (.*?) Nascimento", re.DOTALL)
    nascimento_regex = re.compile(r"Nascimento: (.*?)\s", re.DOTALL)
    cirurgiao_regex = re.compile(r"Cirurgião: (.*?) Acomodação", re.DOTALL)
    acomodacao_regex = re.compile(r"Acomodação (.*?) Convênio", re.DOTALL)
    convenio_regex = re.compile(r"Convênio: (.*?)\s", re.DOTALL)
    servicos_regex = re.compile(r"Serviços: (.*?)(?=\nMateriais|\sMateriais|Materiais|\nObs|\sObs|Obs|$)", re.DOTALL)

    return Cirurgia(
        horario=re.findall(horario_regex, texto)[0],
        paciente=re.findall(paciente_regex, texto)[0],
        idade=re.findall(idade_regex, texto)[0],
        nascimento=re.findall(nascimento_regex, texto)[0],
        cirurgiao=re.findall(cirurgiao_regex, texto)[0],
        acomodacao=re.findall(acomodacao_regex, texto)[0],
        convenio=re.findall(convenio_regex, texto)[0],
        servicos=re.findall(servicos_regex, texto)[0],
    )

def pegar_procedimentos_e_ordenar_alfabeticamente(texto: str) -> List[str]:
    procedimentos = texto.split("+")
    for i in range(len(procedimentos)):
        procedimentos[i] = procedimentos[i].strip()
    return sorted(procedimentos)
