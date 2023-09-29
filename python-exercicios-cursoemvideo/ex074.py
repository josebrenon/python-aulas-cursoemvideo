"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar 
    em uma tupla. Depois disso, mostre a listagem de números gerados e também indique 
    o menor e o maior valor que estão na tupla

    Esse programa gera 5 números aleatórios e coloca em uma tupla, depois mostra os 
    números que foram gerados, e indica o maior e o menor valor sorteado. 

    Autor: José Brenon - 29/09/2023
"""
from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os números gerados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')
  