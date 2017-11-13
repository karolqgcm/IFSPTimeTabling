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

def fitnessG2(populacaoAG2):
    
    return populacaoAG2

def fitnessAG2TodasDisciplinasOferecidas(listaDisciplinasObrigatoriasDaTurma, individuoAG2):
    fitAG2TodasDisciplinasOferecidas = 0
    return fitAG2TodasDisciplinasOferecidas

def fitnessAG2TodosProfDisponiveisAlocados(listaProfDisponiveis, individuoAG2):
    fitAG2TodosProfDisponiveisAlocados = 0
    return fitAG2TodosProfDisponiveisAlocados

def fitnessAG2CargaHoraProfAdequada(dicionarioProfCargaHora, individuoAG2):
    fitAG2CargaHoraProfAdequada = 0
    return fitAG2CargaHoraProfAdequada

def fitnessAG2CargaHoraMateriaCompleta(dicionarioDiscCargaHora, individuoAG2):
    fitAG2CargaHoraMateriaCompleta = 0
    return fitAG2CargaHoraMateriaCompleta


pop2 = criarPopulacaoInicialG2 (10, populacaoAG1)

pop2 = crossOverG2(pop2, 5)

pop2 = mutacaoG2(populacaoAG1,pop2, 10)

f.write("POPULACAO AG2 \n")
for i in pop2:
    f.write(str(i)+ '\n')
