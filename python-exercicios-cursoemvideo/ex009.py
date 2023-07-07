"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 009: Faça um programa que leia um número Inteiro qualquer
    e mostre na tela a sua tabuada.

    Esse programa pede para o usuário digitar um número inteiro e mostra a sua tabuada.

    By: José Brenon - 15/04/2023
"""
n = int(input('Digite um número para ver a sua tabuada: '))
print('='*10)
print('{} x {:2} = {:2}'.format(n, 1, n*1))
print('{} x {:2} = {:2}'.format(n, 2, n*2))
print('{} x {:2} = {:2}'.format(n, 3, n*3))
print('{} x {:2} = {:2}'.format(n, 4, n*4))
print('{} x {:2} = {:2}'.format(n, 5, n*5))
print('{} x {:2} = {:2}'.format(n, 6, n*6))
print('{} x {:2} = {:2}'.format(n, 7, n*7))
print('{} x {:2} = {:2}'.format(n, 8, n*8))
print('{} x {:2} = {:2}'.format(n, 9, n*9))
print('{} x {:2} = {:2}'.format(n, 10, n*10))
print('='*10)
