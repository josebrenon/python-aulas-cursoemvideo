"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 020: O mesmo professor do desafio 19 quer sortear a ordem de apresentação
    de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
    e mostre a ordem sorteada.

    Esse programa pede para o usuário digitar quatro nomes importa da biblioteca math a função shuffle,
    separa os nomes em uma lista sorteia eles e mostra o resultado.

    By: José Brenon - 15/04/2023
"""
from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: \n{}'.format(lista))
