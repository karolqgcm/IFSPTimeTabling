# coding=utf-8
import random

import versao1pt1 as pt1

populacaoAG1 = pt1.criarG1(20,10,10,10)

f = open('teste2', 'w')

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

def fitnessG2(populacaoAG2, dictCargaTurma, dictProfessores):
    
    listDisciplinasObrigatoriasTurma = listarDisciplinasObrigatoriasTurma(dictCargaTurma)
    
    listProfessoresDisponiveis = listarProfessoresDisponiveis(dictProfessores)
        
    for individuo in populacaoAG2:
        
        listDisciplinasIndividuo = extrairDisciplinasDeIndividuo(individuo)
        
        dictNumeroDeAulasDisciplinas = contarAulasDisciplinasDadas(listDisciplinasIndividuo)
        
        fitAG2TodasDisciplinasOferecidas=fitnessAG2TodasDisciplinasOferecidas(listDisciplinasObrigatoriasTurma,individuo)
        individuo[-1] += fitAG2TodasDisciplinasOferecidas 
        
        fitAG2TodosProfDisponiveisAlocados=fitnessAG2TodosProfDisponiveisAlocados(listProfessoresDisponiveis, individuo)
        individuo[-1] += fitAG2TodosProfDisponiveisAlocados
    
        fitAG2CargaHoraMateriaCompleta = fitnessAG2CargaHoraMateriaCompleta(dictCargaTurma, dictNumeroDeAulasDisciplinas)
        individuo[-1] += fitAG2CargaHoraMateriaCompleta
        
        for i in range(5):
            individuo[-1] += individuo[i][-1]
    return populacaoAG2

def fitnessAG2TodasDisciplinasOferecidas(listDisciplinasObrigatoriasTurma, individuoAG2):
    fitAG2TodasDisciplinasOferecidas = 0
    listDisciplinasIndividuo = extrairDisciplinasDeIndividuo(individuoAG2)
    if set(listDisciplinasObrigatoriasTurma).issubset(listDisciplinasIndividuo):
        fitAG2TodasDisciplinasOferecidas += 1000
    return fitAG2TodasDisciplinasOferecidas

def fitnessAG2TodosProfDisponiveisAlocados(listProfessoresDisponiveis, individuoAG2):
    fitAG2TodosProfDisponiveisAlocados = 0
    listProfessoresIndividuo = extrairProfIndividuo(individuoAG2)
    if set(listProfessoresDisponiveis).issubset(listProfessoresIndividuo):
        fitAG2TodosProfDisponiveisAlocados += 100    
    return fitAG2TodosProfDisponiveisAlocados

#devera ser extendido para as outras turmas, apenas uma nao faz sentido
def fitnessAG2CargaHoraProfAdequada(dicionarioProfCargaHora, numeroDeAulasDadasProfessores):
    fitAG2CargaHoraProfAdequada = 0    
    return fitAG2CargaHoraProfAdequada

def fitnessAG2CargaHoraMateriaCompleta(dictCargaTurma, dictNumeroDeAulasDisciplinas):
    fitAG2CargaHoraMateriaCompleta = 0
    
    for disciplina in dictNumeroDeAulasDisciplinas:
        for item in dictCargaTurma:
            if item["sigla"]==disciplina:
                if item["cargaHoraria"]!=dictNumeroDeAulasDisciplinas[disciplina]:
                    fitAG2CargaHoraMateriaCompleta -= 15
                else:
                    fitAG2CargaHoraMateriaCompleta += 15
    return fitAG2CargaHoraMateriaCompleta

def extrairDisciplinasDeIndividuo(individuo):    
    listDisciplinasIndividuo = []
    tempIndividuo = individuo[:]
    del tempIndividuo[-1]     
    for dia in tempIndividuo:
        listDisciplinasIndividuo.append(dia[0][1])           
        listDisciplinasIndividuo.append(dia[1][1]) 
    return listDisciplinasIndividuo

def extrairProfIndividuo(individuo):
    listProfIndividuo = []
    tempIndividuo = individuo[:]
    del tempIndividuo[-1]
    for dia in tempIndividuo:
        listProfIndividuo.append(dia[0][0])           
        listProfIndividuo.append(dia[1][0])  
    
    return listProfIndividuo

def listarDisciplinasObrigatoriasTurma(dictCargaTurma):
    listDisciplinasObrigatoriasTurma =[]
    for item in dictCargaTurma:
        listDisciplinasObrigatoriasTurma.append(item["sigla"])
    return listDisciplinasObrigatoriasTurma

def listarProfessoresDisponiveis(dictProfessores):
    listProfessoresDisponiveis =[]
    for item in dictProfessores:
        listProfessoresDisponiveis.append(item["nome"])
    return listProfessoresDisponiveis

def contarAulasProfessorDadas(listProfIndividuo):
    dictNumeroDeAulasProfessores = {x:listProfIndividuo.count(x)*2 for x in listProfIndividuo}    
    return dictNumeroDeAulasProfessores

def contarAulasDisciplinasDadas(listDisciplinasIndividuo):
    dictNumeroDeAulasDisciplinas = {x:listDisciplinasIndividuo.count(x)*2 for x in listDisciplinasIndividuo}  
    return dictNumeroDeAulasDisciplinas



pop2 = criarPopulacaoInicialG2 (10, populacaoAG1)

pop2 = crossOverG2(pop2, 5)

pop2 = mutacaoG2(populacaoAG1,pop2, 10)

print("x-----x-----x-----x")
#print(pop2)

pop2 = fitnessG2(pop2, pt1.dictCargaTurma, pt1.dictProfessores)
print("x-----x-----x-----x")
print(pop2)

f.write("POPULACAO AG2 \n")
for i in pop2:
    f.write(str(i)+ '\n')


