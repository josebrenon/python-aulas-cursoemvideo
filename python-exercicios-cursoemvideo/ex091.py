"""
    Esse exercício é referente a aula 19 do curso de Python do Curso em vídeo:

    Desafio 091: Crie um programa onde 4 jogadores joguem um dado e tenham 
    resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
    No final, coloque esse dicionário em ordem, sabendo que o 
    vencedor tirou o maior número no dado.

    Autor: José Brenon - 11/12/2023
"""
from random import randint
from time import sleep
from operator import itemgetter #para organizar os dicionários
jogo = {'jogador 1': randint(1,6), 'jogador 2': randint(1,6),
'jogador 3': randint(1,6), 'jogador 4': randint(1,6)}
ranking = list()
print('='*35)
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f"O {k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # organiza o dicionário
print('='*35)
print(f"  ==  RANKING DOS JOGADORES ==  ")
for i, v in enumerate(ranking):
    print(f"  {i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)


