"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 078: Faça um programa que leia 5 valores numéricos e 
    guarde-os em uma lista. No final, mostre qual foi o maior e 
    o menor valor digitado e as suas respectivas posições na lista.

    Esse programa pede para o usuário digitar 5 valores e guarda em uma lista
    no final, mostra qual foi o maior e o menor valor digitado e as suas respectivas posições.

    Autor: José Brenon - 02/10/2023
"""
valores = list()
mai = 0 
meno = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = meno = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < meno:
            meno = valores[c]
print(f'Os números digitados foram {valores}')
print(f'O maior valor lido foi o {mai} nas posições ', end='') 
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor lido foi o {meno} nas posições ', end='')
for i, v in enumerate(valores):
    if v == meno:
        print(f'{i}... ', end='')
