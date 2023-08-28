"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 065: Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual foi o maior
    e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
    ou não continuar a digitar valores.

    Esse programa lê varios números inteiros, perguntando sempre se ele quer
    digitar mais algum coisa, verifica quantos números foram digitados pelo usuário e mostra
    calcula e mostra a média entre eles, o maior e o menor valores lidos.

    Autor: José Brenon - 28/08/2023
"""

opcao = 'S'
soma = cont = media = maior = menor = 0
while opcao in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / cont
print(f'''Você digitou {cont} números e a média entre eles foi {media:.2f}
O maior número foi {maior} e o menor foi {menor}''')
