"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
    e mostre quantos dólares ela pode comprar.

    Esse programa pede para o usuário digitar um número inteiro e mostra a sua tabuada.

    By: José Brenon - 15/04/2023
"""
real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 4.77  # 4.77 cotação no dia 21/04/2023 / 5.16 cotação no dia 15/04/2023
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
