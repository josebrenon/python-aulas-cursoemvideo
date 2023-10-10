"""
    Esse exercício é referente a aula 18 do curso de Python do Curso em vídeo:

    Desafio 088: Faça um programa que ajude um jogador da MEGA SENA 
    a criar palpites.O programa vai perguntar quantos jogos serão gerados 
    e vai sortear 6 números entre 1 e 60 para cada jogo, 
    cadastrando tudo em uma lista composta.

    Este programa pergunta ao usuário quantos jogos ele quer sortear, sorteia
    6 números aleatórios sem repetir guarda em uma lista, depois
    mostra os resultados.

    Autor: José Brenon - 06/10/2023
"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'* 34)
print(f'{"JOGA NA MEGA SENA":^34}')
print('-'* 34)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' * 10, f' << SORTEANDO {quant} JOGOS >>', '='* 10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('='* 10, f'<< BOA SORTE >>', '='* 10)
