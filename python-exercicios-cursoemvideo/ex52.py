"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 052: Faça um programa que leia um número inteiro
    e diga se ele é ou não um número primo.

    Esse programa lê um número inteiro, pega a quantidade de números que ele tem
    e verifica quantas vezes ele pode ser divisivel caso for 2 vezes é um número primo
    senão não é e mostra quantas vezes ele foi divisivel e se é ou não primo.

    Autor: José Brenon - 09/08/2023
"""
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1

if tot == 2:
    print('O número {} é divisível por 1 e por ele mesmo'.format(n))
    print('E por isso ele é PRIMO!')
else:
    print('O número {} é divisível por 1 e por mais {} números'.format(n, tot - 1))
    print('Por isso ele NÃO é primo!')
