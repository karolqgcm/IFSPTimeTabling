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
    

def criarPopulacaoInicial(numeroIndividuos):
    populacao = []
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuo())
    return populacao

def crossOver(populacao, numeroCruzamentos):
    
    for cruzamento in range(numeroCruzamentos):
        mae = random.choice(populacao)
        pai = random.choice(populacao)
        
        if mae != pai:
            filho = [mae[0], pai[1], 0]
            populacao.append(filho)
        else:
            cruzamento += 1
    return populacao


def mutacao(populacao, porcentagemMutacao):
    for individuo in populacao:        
        if random.randint(0,100) <= porcentagemMutacao:
            p = random.choice(listProfessores)
            d = random.choice(listMaterias)
            gene = [p, d]
            individuo[1] = gene
    return populacao

def selecao(numeroIndividuos, populacao):
    populacao.sort(key=lambda x: x[2], reverse=True)    
    populacao = populacao[:numeroIndividuos]
    return populacao

def fitness(populacao):
    for individuo in populacao:
        if individuo[0][0]==individuo[1][0]:
            individuo[2] += 10
        if individuo[0][1]==individuo[1][1]:
            individuo[2] += 10   
        if individuo[0][1]==individuo[1][1] and individuo[0][0]!=individuo[1][0] or individuo[0][1]!=individuo[1][1] and individuo[0][0]==individuo[1][0]:
            individuo[2] -= 30
        for i in range(2):
            materias=(item["materias"] for item in dictProfessores if item["nome"] == individuo[i][0]).next()
            for materia in materias:
                if materia == individuo[i][1]:
                    individuo[2] += 15               

        
    
def maxFitness(populacao):
    return max([individuo[-1] for individuo in populacao])

def minFitness(populacao):
    return min([individuo[-1] for individuo in populacao])

def midFitness(populacao):
    return sum([individuo[-1] for individuo in populacao])/len(populacao)

def criarG1(nIndividuosPopInicial, nCruzamentos, porcentagemMutacao, nGeracoes):
    geracao = 0
    populacao = criarPopulacaoInicial(nIndividuosPopInicial)
    fitness(populacao)
    print("DADOS DA GERAÇÃO #" + str(geracao))
    print("Média de fitness" + str(midFitness(populacao)))
    print("Máximo de fitness" + str(maxFitness(populacao)))
    print("Mínimo de fitness" + str(minFitness(populacao))+ '\n')
    
    for geracao in range(1, nGeracoes):        
        populacao = crossOver(populacao, nCruzamentos)
        populacao = mutacao(populacao, porcentagemMutacao)
        fitness(populacao)
        populacao = selecao(nIndividuosPopInicial, populacao)
        print("DADOS DA GERAÇÃO #" + str(geracao))
        print("Média de fitness" + str(midFitness(populacao)))
        print("Máximo de fitness" + str(maxFitness(populacao)))
        print("Mínimo de fitness" + str(minFitness(populacao))+'\n')
        
criarG1(20,10,10,10)
