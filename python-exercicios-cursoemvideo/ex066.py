"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 066: Crie um programa que leia números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que
    é a condição de parada. No final, mostre quantos números foram digitados
    e qual foi a soma entre elas (desconsiderando o flag).

    Esse programa lê varios números conta quantos foram digitados e soma todos eles
    desconsiderando o ponto de parada que é 999, no final mostra os resultados.

    Autor: José Brenon - 31/08/2023
"""
n = s = cont = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n == 999:
        break
    cont += 1
    s += n
print(f'''Você digitou {cont} número e a soma entre eles foi {s}''')