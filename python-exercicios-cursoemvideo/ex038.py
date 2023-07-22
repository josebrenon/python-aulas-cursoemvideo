"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 038: Escreva um programa que leia dois números inteiros e compare-os.
    Mostrando uma mensagem na tela: O primeiro valor é maior, o segundo valor é maior,
    não existe valor maior, os dois são iguais.

    Esse programa pede para o usuário digitar dois números inteiros, verifica qual deles
    é maior e mostra, qual dos valores é o maior, se não mostra que são iguais.

    Autor: José Brenon - 22/07/2023
"""

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')
