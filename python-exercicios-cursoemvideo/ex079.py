"""
    Esse exercício é referente a aula 17 do curso de Python do Curso em vídeo:

    Desafio 079:  Crie um programa onde o usuário possa digitar vários 
    valores numéricos e cadastre-os em uma lista. Caso o número já exista 
    lá dentro, ele não será adicionado. No final, serão exibidos todos 
    os valores únicos digitados, em ordem crescente.

    Esse programa pede para o usuário digitar vários valores e cadastra esses
    números em uma lista. Caso o valor ja existir ele não será adicionado.
    Autor: José Brenon - 02/10/2023
"""
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opção = str(input('Quer continuar [S/N]: ')).strip().upper()
    if opção in 'Nn':
        break
print('-='*30)
valores.sort()
print(f'A lista final ficou: {valores}')
