"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 029: Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite.

    Esse progama pede para o usuário digitar a velocidade do carro, verifica se
    exedeu o limite de 80Km/h, se sim calcula quantos Km passou e adiciona R$7,00
    para cada Km, mostra que ultrapassou o limite de velocidade e quanto será a multa.

    Autor: José Brenon - 18/07/2023
"""

velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você exedeu o limite permitido que é de 80Km/h\n'
    'Você deve pagar uma multa de R${:.2f}'.format(multa))
    
print('Tenha um bom dia! Dirija com segurança!')

