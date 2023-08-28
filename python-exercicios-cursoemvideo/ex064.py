"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 064: Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que é a condição
    de parada. No final, mostre quantos números foram digitados e qual foi a 
    soma entre eles (desconsiderando o flag).

    Esse programa lê varios números conta quantos foram digitados e soma todos eles
    desconsiderando o ponto de parada que é 999, no final mostra os resultados.

    Autor: José Brenon - 28/08/2023
"""
n = 0
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: ')) 
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')