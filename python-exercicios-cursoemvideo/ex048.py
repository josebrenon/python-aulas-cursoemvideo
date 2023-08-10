"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 048: Faça um programa que calcule a soma entre todos os números
    que são múltiplos de três e que se encontram no intervalo de 1 até 500.

    Esse programa verifica quais números são multiplos de 3 e soma somente eles.

    Autor: José Brenon - 09/08/2023
"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
      soma += c
      cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
