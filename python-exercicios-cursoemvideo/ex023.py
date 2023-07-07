"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 023: Faça um programa que leia um número de 0 a 9999
    e mostre na tela cada um dos dígitos separados.

    Esse programa pede para o usuário digitar um número de 0 a 9999 calcula a sua unidade, dezena,
    centena e milhar, e mostra cada uma delas.

    By: José Brenon - 18/04/2023
"""
num = int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
