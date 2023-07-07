"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 014: Escreva um programa que converta uma temperatura
    digitando em graus Celsius e converta para graus Fahrenheit.

    Esse programa pede para o usuário digitar a temperatura em graus Celsius,
    converte para Fahrenheit e mostra o resultado.

    By: José Brenon - 15/04/2023
"""
c = float(input('Informe a temperatura em ºC:'))
f = 9 * c / 5 + 32
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF!'.format(c, f))
