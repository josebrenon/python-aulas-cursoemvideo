"""
    Esse exercício é referente a aula 06 do curso de Python do Curso em vídeo:

    Desafio 003: Crie um programa que leia dois números e mostre a soma entre eles.

    Esse programa pede para o usuário digitar dois números e mostra a soma entre eles.

    By: José Brenon - 15/04/2023
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))
