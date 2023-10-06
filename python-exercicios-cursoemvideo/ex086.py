"""
    Esse exercício é referente a aula 18 do curso de Python do Curso em vídeo:

    Desafio 086: Crie um programa que declare uma matriz de dimensão 3x3 
    e preencha com valores lidos pelo teclado. No final, mostre a matriz 
    na tela, com a formatação correta.

    Este programa cria uma lista com três outras listas dentro começando em 0,
    depois cria dois laços um para linha e o outro para coluna depois pede para 
    o usuário digitar os valores e organiza a matriz utilizando outros dois laços
    e mostra o resultado.

    Autor: José Brenon - 06/10/2023
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
