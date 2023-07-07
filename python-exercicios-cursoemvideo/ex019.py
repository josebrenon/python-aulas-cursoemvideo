"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

    Esse programa pede para o usuário digitar quatro nomes importa da biblioteca math a função choice,
    separa os nomes em uma lista escolhe um e mostra o resultado.

    By: José Brenon - 15/04/2023
"""
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
s = choice(alunos)
print('O aluno sorteado foi: {}'.format(s))
