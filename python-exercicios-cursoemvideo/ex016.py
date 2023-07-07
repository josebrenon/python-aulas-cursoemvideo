"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 016: Crie um programa que leia um número Real qualquer pelo teclado
    e mostre na tela a sua porção Inteira.

    Esse programa pede para o usuário digitar um número real, importa da biblioteca math
    a função trunc e mostra a parte inteira do número.

    By: José Brenon - 15/04/2023
"""
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua proporção inteira é {}'.format(num, trunc(num)))
