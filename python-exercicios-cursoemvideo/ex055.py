"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 055: Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e o menor peso lidos.

    Esse programa lê os pesos de 5 pessoas diferentes, verifica qual deles é o maior
    e o menor e mostra somente esses resultados.

    Autor: José Brenon - 09/08/2023
"""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('''O maior peso lido foi de {}Kg
O menor peso lido foi de {}Kg'''.format(maior, menor))
