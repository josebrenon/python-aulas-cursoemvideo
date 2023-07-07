"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 025: Crie um programa que leia o nome de uma pessoa
    e diga se ela tem “SILVA” no nome.

    Esse programa pede para o usuário digitar um nome e mostra se ele tem ou não "SILVA".

    By: José Brenon - 18/04/2023
"""
nome = str(input('Qual é o seu nome? ')).split()
print('Seu nome tem Silva? {}'.format(nome))
