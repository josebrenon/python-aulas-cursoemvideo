"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

    Esse programa pergunta ao usuário qual ano ele quer analizar, se caso quiser analizar
    o ano atual pede para digitar 0, verifica se o usuário digitou 0 se não verifica se 
    o ano que digitou é divisivel por 4 e divisivel por 100 e não divisivel por 400, calculando
    assim se é bissexto ou não e mostra o resultado.

    Autor: José Brenon - 18/07/2023
"""
from datetime import date

ano = int(input('Digite o ano que você quer analisar ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
