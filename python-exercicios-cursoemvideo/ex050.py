"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 050: Desenvolva um programa que leia seis números inteiros e mostre
    a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

    Esse programa lê seis números inteiros, verifica se o número é par e soma somente esses.

    Autor: José Brenon - 09/08/2023
"""
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} pares e a soma foi {}'.format(cont, soma))
