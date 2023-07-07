"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:

    – O nome com todas as letras maiúsculas e minúsculas.

    – Quantas letras ao todo (sem considerar espaços).

    – Quantas letras tem o primeiro nome.

    Esse programa pede para o usuário digitar seu nome completo, tira os espaços do começo, do fim
    e do meio, e mostra o nome com todas as letras maiúsculas e minúsculas, quantas letras tem ao todo

    By: José Brenon - 18/04/2023
"""
nome = str(input(print('Digite seu nome completo: '))).strip()
print('Analisando o seu nome...')
print('O seu nome em maiusculas fica {}'.format(nome.upper()))
print('O seu nome em minusculas fica {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
