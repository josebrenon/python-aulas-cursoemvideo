"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 067: Faça um programa que mostre a tabuada de vários números,
    um de cada vez, para cada valor digitado pelo usuário. O programa será
    interrompido quando o número solicitado for negativo.

    Esse programa pede para o usuário digitar um número para saber a sua tabuada
    até que ele digite um número negativo.

    Autor: José Brenon - 31/08/2023
"""
c = 0
print('-='*8)
print('Programa tabuada')
print('-='*8)
while True:
    n = int(input("Qual número você quer saber a tabuada? "))
    print('~'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {c * n}")
    print('~'*30)
print('-='*30)
print('Programa tabuada finalizado, volte sempre!')
print('-='*30)
