"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
    com 5% de desconto.

    Esse programa pede para o usuário digitar o preço de um produto, calcula e mostra o resultado
    com 5% de desconto.

    By: José Brenon - 15/04/2023
"""
p = float(input('Qual o valor do produto? R$'))
novo = p - (p * 5 / 100)
print('O produto que valia R${:.2f} com desconto de 5% fica em R${:.2f}'.format(p, novo))
