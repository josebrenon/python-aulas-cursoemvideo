"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
    de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

    Esse programa pede para o usuário digitar o comprimento do cateto oposto e do cateto adjacente
    de um triângulo retângulo, importa da biblioteca math a função hypot calcula e mostra os resultados.

    By: José Brenon - 15/04/2023
"""
from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
print('Se o cateto oposto é {} e o cateto adjacente é {} a hipotenusa é {:.2f}'.format(co, ca, hypot(co, ca)))
