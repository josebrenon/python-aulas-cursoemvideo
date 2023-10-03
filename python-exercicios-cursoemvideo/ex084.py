"""
    Esse exercício é referente a aula 18 do curso de Python do Curso em vídeo:

    Desafio 084: Faça um programa que leia nome e peso de várias pessoas, 
    guardando tudo em uma lista. No final mostre:
    A) Quantas pessoas foram cadastradas. 
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

    Este programa lê o nome de várias pessoas e guarda tudo em uma lista,
    no final conta e mostra quantas pessoas foram cadastradas, verifica qual
    foi o maior peso lido e o menor, e mostra quais pessoas tem o maior peso 
    e quais tem o menor.

    Autor: José Brenon - 02/10/2023
"""
pessoas = list()
dados = [] 
maiorpeso = menorpeso = 0
while True:
    print('-'*50)
    print('CADASTRE UMA NOVA PESSOA')
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
        if r not in 'SN':
            print('Opção inválida! Digite apenas S ou N.')
    if r in 'N':
        break
print('-'*50)
print(f'A quantidade de pessoas cadastradas foi de {len(pessoas)}.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de: ', end= ' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menorpeso}Kg. Peso de: ', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
