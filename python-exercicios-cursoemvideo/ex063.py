"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 063:  Escreva um programa que leia um número N inteiro qualquer e
    mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
    Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

    Esse programa pergunta ao usuário quantos termos ele quer ver da sequencia
    de fibonacci, depois verfica enquanto N for maior que 0 ele soma o primeiro
    com o ultimo até chegar no número de termos escolhido.

    Autor: José Brenon - 28/08/2023
"""
print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM')
print('~' * 30)
