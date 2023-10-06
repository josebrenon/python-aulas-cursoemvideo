"""
    Esse exercício é referente a aula 18 do curso de Python do Curso em vídeo:

    Desafio 085:Crie um programa onde o usuário possa digitar sete valores 
    numéricos e cadastre-os em uma lista única que mantenha separados os 
    valores pares e ímpares. No final, mostre os valores pares e 
    ímpares em ordem crescente.

    Este programa pede ao usuário para digitar 7 valores, analisa quais deles
    são pares e quais são impares, se for par coloca no index 0 da lista e se for
    impar coloca no index 1, depois organiza cada uma das listas separadamente 
    e mostra os resultados.

    Autor: José Brenon - 02/10/2023
"""
num = [[],[]]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-='*40)
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')
