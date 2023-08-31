"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 068: Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interrompido quando o jogador perder, mostrando o total
    de vitórias consecutivas que ele conquistou no final do jogo.

    Esse programa pede para o usuário digitar um número, e o computador pensa em outro,
    ele soma os dois valores e verifica se o número é par ou impar
    depois verifica se o valor do usuário e do computador é par ou impar, se o resultado da soma
    for par quem digitou um número par vence senão perde, caso o jogador perca o jogo encerra e conta
    quantas vezes o jogador venceu.
    
    Autor: José Brenon - 31/08/2023
"""
from random import randint
print('-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-'*40)
cont = 0
while True:
    computador = randint(1, 10) #Computador pensou em um número de 1 a 10
    jogador = int(input('Digite um número: '))#jogador digitou um número de 1 a 10
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma %2 == 0 else 'DEU ÍMPAR')
    print('-'*40)
    if tipo == 'P':
        if soma %2 == 0:
           print('Você VENCEU!')
           cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma %2 == 1:
            print('Você GANHOU!')
            cont +=1
        else:
            print('Você PERDEU')
            break
    print('-'*40)
    print('Vamos jogar de novo...')
    print('-'*40) 
if cont == 0:
    print(f'Você não ganhou nenhuma vez')
elif cont == 1:
    print(f'Você ganhou {cont} vez')
else:
    print(f'Você ganhou {cont} vezes')
