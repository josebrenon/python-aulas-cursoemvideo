"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 046: Faça um programa que mostre na tela uma contagem regressiva
    para o estouro de fogos de artifício, indo de 10 até 0,
    com uma pausa de 1 segundo entre eles.

    Esse programa cria um laço for que conta de 10 até 0 a cada 1 segundo
    e no final escreve que os fogos foram acionados.

    Autor: José Brenon - 09/08/2023
"""
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("BOOOMM!!")
