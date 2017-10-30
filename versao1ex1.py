import random

dictProfessores = [
    {"nome": "Nelson", "materias": ["SEG", "DW2"], "disponivel": 8},
    {"nome": "Luciana", "materias": ["PI2", "TOP"], "disponivel": 8}, 
    {"nome": "Mario", "materias": ["PI2", "TOP"], "disponivel": 12},
    {"nome": "Henrique", "materias": ["DW2"], "disponivel": 4}    
]

dictCargaTurma = [
    {"sigla": "PI2", "cargaHoraria": 8},
    {"sigla": "SEG", "cargaHoraria": 4},
    {"sigla": "DW2", "cargaHoraria": 4},
    {"sigla": "TOP", "cargaHoraria": 4}
]

listProfessores = []

for item in dictProfessores:
    listProfessores.append(item["nome"])

listMaterias = []

for item in dictCargaTurma:
    listMaterias.append(item["sigla"])
    
def criarIndividuo():
    individuo = []
    for i in range(2):
        p = random.choice(listProfessores)
        d = random.choice(listMaterias)
        gene = [p, d]
        individuo.append(gene)
    individuo.append(0);
    return individuo
    

def criarPopulacao(numeroIndividuos):
    populacao = []
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuo())
    return populacao


def fitness(populacao):
    for individuo in populacao:
        if individuo[0][0]==individuo[1][0]:
            individuo[2] += 10
        print(individuo)
        
fitness(criarPopulacao(3))


        