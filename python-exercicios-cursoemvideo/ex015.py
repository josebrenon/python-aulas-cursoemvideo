"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 015: Escreva um programa que pergunte a quantidade de km percorridos
    por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

    Esse programa pede para o usuário digitar a quantidade de km percorridos por um carro,
    e a quantidade de dias que utilizou o carro, calcula o preço a pagar e mostra os resultados.

    By: José Brenon - 15/04/2023
"""
d = int(input('Digite a quantidade de dias que você usou o carro: '))
km = float(input('Digite a quantidade de km rodados: '))
vf = (d * 60) + (km * 0.15)
print('Você devera pagar R${:.2f} pelo aluguel do carro!'.format(vf))
