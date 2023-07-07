"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 027: Faça um programa que leia o nome completo de uma pessoa,
    mostrando em seguida o primeiro e o último nome separadamente.

    Esse programa pede para o usuário digitar seu nome completo e mostra o primeiro
    e o último separadamente.

    By: José Brenon - 26/04/2023
"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Olá, é um grande prazer te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
