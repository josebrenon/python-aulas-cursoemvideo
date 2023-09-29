"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 076: Crie um programa que tenha uma tupla única com nomes de produtos
    e seus respectivos preços, na sequência, mostre uma listagem de preços, 
    organizando os dados em forma tabular.

    Esse programa cria uma tupla com nomes e preços de produtos, e mostra cada um deles
    em forma tabular

    Autor: José Brenon - 29/09/2023
"""
produtos = ('Lapis', 1.75, 'Caneta', 2.50, 'Caderno', 12.00, 'Estojo', 13.50, 'Mochila', 120.00)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos %2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    if pos %2 == 1:
      print(f'R${produtos[pos]:>7.2f}')
print('-'*40)
