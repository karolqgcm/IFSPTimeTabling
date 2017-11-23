# coding=utf-8
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

f = open('teste1', 'w')

for item in dictProfessores:
    listProfessores.append(item["nome"])

listMaterias = []

for item in dictCargaTurma:
    listMaterias.append(item["sigla"])


def criarIndividuoG1():
    individuo = []
    f.write("Criar individuos AG1\n")
    for i in range(2):
        p = random.choice(listProfessores)
        d = random.choice(listMaterias)
        gene = [p, d]
        individuo.append(gene)
    individuo.append(0);
    f.write(str(individuo) + "\n")
    return individuo
    

def criarPopulacaoInicialG1(numeroIndividuos):
    populacao = []
    f.write("Criar população AG1\n")
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuoG1())
    return populacao

def crossOverG1(populacao, numeroCruzamentos):
    f.write("Fazer crossover AG1\n")
    
    for cruzamento in range(numeroCruzamentos):
        mae = random.choice(populacao)
        pai = random.choice(populacao)
        
        if mae != pai:
            filho = [mae[0], pai[1], 0]
            f.write("Novo individuo por crossover: \n")
            f.write(str(filho)+"\n")
            
            populacao.append(filho)
        else:
            cruzamento += 1
    return populacao


def mutacaoG1(populacao, porcentagemMutacao):
    f.write("Mutação AG1\n")
    
    for individuo in populacao:        
        if random.randint(0,100) <= porcentagemMutacao:
            p = random.choice(listProfessores)
            d = random.choice(listMaterias)
            gene = [p, d]
            individuo[1] = gene
            f.write("individuo mutado AG1\n")
            f.write(str(individuo)+"\n")
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
    
    f.write("DADOS DA GERAÇÃO #" + str(geracao)+'\n')
    f.write("Média de fitness" + str(midFitness(populacao))+'\n')
    f.write("Máximo de fitness" + str(maxFitness(populacao))+'\n')
    f.write("Mínimo de fitness" + str(minFitness(populacao))+ '\n')
    
    for geracao in range(1, nGeracoes):        
        populacao = crossOverG1(populacao, nCruzamentos)
        populacao = mutacaoG1(populacao, porcentagemMutacao)
        fitnessG1(populacao)
        populacao = selecaoG1(nIndividuosPopInicial, populacao)
        f.write("DADOS DA GERAÇÃO #" + str(geracao)+'\n')
        f.write("Média de fitness" + str(midFitness(populacao))+'\n')
        f.write("Máximo de fitness" + str(maxFitness(populacao))+'\n')
        f.write("Mínimo de fitness" + str(minFitness(populacao))+'\n')
    return populacao
        
populacaoG1 = criarG1(20,10,10,10)

