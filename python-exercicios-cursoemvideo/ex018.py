"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 018: Faça um programa que leia um ângulo qualquer
    e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

    Esse programa pede para o usuário digitar um ângulo, importa da biblioteca math
    as funções sin, cos, tan, radians, calcula o seno, cosseno e a tangente e mostra os resultados.

    By: José Brenon - 15/04/2023
"""
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
print('O seno de {} é {:.2f}'.format(angulo, sin(radians(angulo))))
print('O cosseno de {} é {:.2f}'.format(angulo, cos(radians(angulo))))
print('A tangente de {} é {:.2f}'.format(angulo, tan(radians(angulo))))
