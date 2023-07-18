"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 028: Escreva um programa que faça o computador “pensar” em um número
    inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
    escolhido pelo computador. O programa deverá escrever na tela se o usuário
    venceu ou perdeu.

    Esse programa escolhe um número de 1 a 5, pede para o usuário digitar o número
    que ele acha que foi o escolhido, verifica se ele acertou e mostra se venceu ou perdeu.

    Autor: José Brenon - 18/07/2023
"""
from random import randint
from time import sleep

n = randint(0, 5)
print('-=-' * 20)
print('Pensei em um número, consegue me dizer qual?')
print('-=-' * 20)
r = int(input('Qual número eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if r == n:
    print('Você ganhou parabéns! O número que eu pensei exatamente o {}'.format(n))
else:
    print('Você perdeu! O número que eu pensei foi {} e não {}'.format(n, r))
