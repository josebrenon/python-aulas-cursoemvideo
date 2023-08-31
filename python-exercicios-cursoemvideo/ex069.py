"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 069:: Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
    ou não continuar. No final, mostre:

    A) quantas pessoas tem mais de 18 anos.

    B) quantos homens foram cadastrados.

    C) quantas mulheres tem menos de 20 anos.

    Esse programa lê a idade e o sexo de várias pessoas e a cada pessoa cadastrada ele
    adiciona mais um ao contador e pergunta se quer cadastrar mais uma, verifica se 
    disser Sim ele continua pedindo senão ele encerra mostrando os resultados de quantas
    pessoas têm mais de 18 anos, quantos homens foram cadastrados e quantas mulheres
    tem menos de 20 anos.
    
    Autor: José Brenon - 31/08/2023
"""
totIdade = totH = totM = 0
while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA   ')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        totIdade += 1
    if sexo in 'M':
         totH += 1
    if sexo in 'F' and idade < 20:
        totM += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''O total de pessoas maiores de 18 anos: {totIdade}
O total de homens cadastrados foi: {totH}
O total de mulheres com menos de 20 anos foi: {totM}''')
