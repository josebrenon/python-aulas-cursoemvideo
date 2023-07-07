"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre quantas
    vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que
    posição ela aparece a última vez.

    Esse programa pede para o usuário digitar uma frase e mostra quantas vezes a letra "A"
    aparece, em que posição aparece pela primeira vez e a última.

    By: José Brenon - 26/04/2023
"""
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))
