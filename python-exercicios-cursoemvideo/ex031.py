"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
    e R$0,45 parta viagens mais longas.

    Esse programa pergunta a distância de uma viagem em Km, verifica se a viagem foi
    de até 200Km ele cobra R$0,50 por Km se for mais longe cobra R$0,45, mostra quantos Km
    a pessoa viajará e o preço da passagem.

    Autor: José Brenon - 18/07/2023
"""

distancia = float(input('Qual a distância da sua viagem? '))
print('Você esta prestes a fazer uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))

"""
if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.45))
"""