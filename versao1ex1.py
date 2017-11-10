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

print(populacaoG1)

def criarIndividuoG2(populacaoG1):
    f.write("Criar individuos AG2\n")
    individuo = []
    for i in range(5):
        individuo.append(random.choice(populacaoG1))
    individuo.append(0)
    f.write(str(individuo) + "\n")
    return individuo

def criarPopulacaoInicialG2(numeroIndividuos, populacaoG1):
    populacao = []
    f.write("Criar população AG2\n")
    for i in range(numeroIndividuos):
        populacao.append(criarIndividuoG2(populacaoG1))
    return populacao

def crossOverG2(populacaoG2, numeroCruzamentos):
    f.write("Fazer crossover AG2\n")
    for cruzamento in range(numeroCruzamentos):
        mae = random.choice(populacaoG2)
        pai = random.choice(populacaoG2)
        
        if mae != pai:
            filho = [mae[0], mae[1], mae[2], pai[3], pai[4], 0]
            populacaoG2.append(filho)
            f.write("Novo individuo por crossover: \n")
            f.write(str(filho)+"\n")            
        else:
            cruzamento += 1
    return populacaoG2


def mutacaoG2(populacaoAG1,populacaoAG2,porcentagemMutacaoAG2):
    f.write("Mutação AG2\n")
    for individuo in populacaoAG2:
        if random.randint(0,100) <= porcentagemMutacaoAG2:
            individuo[4]= random.choice(populacaoAG1)
            f.write("individuo mutado AG2\n")
            f.write(str(individuo)+"\n")            
    return populacaoAG2

def selecaoG2():
    return populacao

def fitnessG2(populacaoAG2):
    return populacao

pop2 = criarPopulacaoInicialG2 (10, populacaoG1)

pop2 = crossOverG2(pop2, 5)

pop2 = mutacaoG2(populacaoG1,pop2, 10)

f.write("POPULACAO AG2 \n")
for i in pop2:
    f.write(str(i)+ '\n')
