"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.

    Esse programa pede para o usuário digitar seu nome e escolher uma das três opções que são:
    pedra, papel ou tesoura, ele sorteia numa lista as três opções e verifica se o jogador
    escolher pedra ele ganha de tesoura, se ele escolher papel ele ganha de pedra e se ele
    escolher tesoura ele ganha de papel.

    Autor: José Brenon - 25/07/2023
"""
from random import randint
from time import sleep
itens = ('Pedra ', 'Papel', 'Tesoura')
computador = randint(0, 2)
nome_jogador = str(input('Digite seu nome: '))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=' * 20)
print('{} jogou {}'.format(nome_jogador, itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 20)

if computador == 0:  # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('{} VENCEU'.format(nome_jogador))
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
if computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('{} GANHOU'.format(nome_jogador))
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
if computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('{} VENCEU'.format(nome_jogador))
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVALIDA')
