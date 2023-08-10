"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão
    de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

    Esse programa lê o primeiro termo e a razão de uma PA e mostra os seus 10
    primeiros termos.

    Autor: José Brenon - 09/08/2023
"""

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = pt + (10 - 1) * r
for c in range(pt, d + r, r):
    print(c, end=' -> ')
print('ACABOU')
