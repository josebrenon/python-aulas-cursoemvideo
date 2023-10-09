"""
    Esse exercício é referente a aula 18 do curso de Python do Curso em vídeo:

    Desafio 086: Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.

    Este programa cria uma lista com três outras listas dentro começando em 0,
    depois cria dois laços um para linha e o outro para coluna depois pede para 
    o usuário digitar os valores e organiza a matriz utilizando outros dois laços
    e verifica quais valores digitados são pares e soma eles, depois pega só os
    valores da ultima coluna e também mostra a soma entre eles, por último verifica
    e mostra o maior valor da segunda linha.

    Autor: José Brenon - 06/10/2023
"""
matriz = [[0,0,0], [0,0,0],[0,0,0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-='*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:
            spar += matriz[l][c]
    print()
print('-='*40)
print(f'A soma dos números pares digitados foi: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos números da última coluna foi: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é o: {mai}')
