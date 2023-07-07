"""
    Esse programa é referente a aula 08 do curso de Python do Curso em vídeo:
    Ele importa da biblioteca math a função para calcular raiz quadrada.

    By: José Brenon - 15/04/2023
"""
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
