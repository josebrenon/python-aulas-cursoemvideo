"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 054: Crie um programa que leia o ano de nascimento
    de sete pessoas. No final, mostre quantas pessoas ainda
    não atingiram a maioridade e quantas já são maiores.

    Esse programa pergunta o ano de nascimento de 7 pessoas, verifica quantas delas são maiores
    de idade e mostra quantas delas são e quantas não são maiores.

    Autor: José Brenon - 09/08/2023
"""
ano = 2017
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if ano - nascimento >= 21:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(maior, menor))
