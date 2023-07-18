"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 030: Crie um programa que leia um número inteiro e mostre na tela
    se ele é PAR ou ÍMPAR.

    Esse programa pede para o usuário digitar um número qualquer, verifica se
    ele é par ou ímpar e mostra o resultado.

    Autor: José Brenon - 18/07/2023
"""
número = int(input('Digite um número qualquer para saber se ele é par ou ímpar: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ímpar'.format(número))