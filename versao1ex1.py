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


def criarIndividuoG1():
    individuo = []
    for i in range(2):
        p = random.choice(listProfessores)
        d = random.choice(listMaterias)
        gene = [p, d]
        individuo.append(gene)
    individuo.append(0);
    return individuo
    

def criarPopulacaoInicialG1(numeroIndividuos):
    populacao = []
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuoG1())
    return populacao

def crossOverG1(populacao, numeroCruzamentos):
    
    for cruzamento in range(numeroCruzamentos):
        mae = random.choice(populacao)
        pai = random.choice(populacao)
        
        if mae != pai:
            filho = [mae[0], pai[1], 0]
            populacao.append(filho)
        else:
            cruzamento += 1
    return populacao


def mutacaoG1(populacao, porcentagemMutacao):
    for individuo in populacao:        
        if random.randint(0,100) <= porcentagemMutacao:
            p = random.choice(listProfessores)
            d = random.choice(listMaterias)
            gene = [p, d]
            individuo[1] = gene
    return populacao

def selecaoG1(numeroIndividuos, populacao):
    populacao.sort(key=lambda x: x[2], reverse=True)    
    populacao = populacao[:numeroIndividuos]
    return populacao

def fitnessG1(populacao):
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
    populacao = criarPopulacaoInicialG1(nIndividuosPopInicial)
    fitnessG1(populacao)
    
    #print("DADOS DA GERAÇÃO #" + str(geracao))
    #print("Média de fitness" + str(midFitness(populacao)))
    #print("Máximo de fitness" + str(maxFitness(populacao)))
    #print("Mínimo de fitness" + str(minFitness(populacao))+ '\n')
    
    for geracao in range(1, nGeracoes):        
        populacao = crossOverG1(populacao, nCruzamentos)
        populacao = mutacaoG1(populacao, porcentagemMutacao)
        fitnessG1(populacao)
        populacao = selecaoG1(nIndividuosPopInicial, populacao)
        #print("DADOS DA GERAÇÃO #" + str(geracao))
        #print("Média de fitness" + str(midFitness(populacao)))
        #print("Máximo de fitness" + str(maxFitness(populacao)))
        #print("Mínimo de fitness" + str(minFitness(populacao))+'\n')
    return populacao
        
populacaoG1 = criarG1(20,10,10,10)

print(populacaoG1)

def criarIndividuoG2(populacaoG1):
    individuo = []
    for i in range(5):
        individuo.append(random.choice(populacaoG1))
    return individuo

def criarPopulacaoInicialG2(numeroIndividuos, populacaoG1):
    populacao = []
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuoG2(populacaoG1))
    return populacao

def crossOverG2():
    return populacao

def mutacaoG2():
    return populacao

def selecaoG2():
    return populacao

def fitnessG2():
    return populacao
