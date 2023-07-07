"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 005: Faça um programa que leia um número Inteiro e mostre na tela
    o seu sucessor e seu antecessor.

    Esse programa pede para o usuário digitar um número e mostra na tela seu antecessor
    e seu sucessor.

    By: José Brenon - 15/04/2023
"""
n = int(input('Digite um número para saber seu antecessor e seu sucessor: '))
print('Analisando o número {}, seu antecessor é {} e o sucessor é {}'.format(n, (n - 1), (n + 1)))
