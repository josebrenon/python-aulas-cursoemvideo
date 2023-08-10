"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
    mais velho e quantas mulheres têm menos de 20 anos.

    Esse programa pergunta quantas pessoas têm no total, lê o nome, a idade e o sexo dessas pessoas,
    faz a média da idade deles, verifica entre os homens qual é o mais velho e mostra a idade
    e o nome, verifica quantas mulheres tem com menos de 20 anos e mostra esse resultado.

    Autor: José Brenon - 09/08/2023
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
totpessoas = int(input('Quantas pessoas têm no total: '))
for p in range(1, totpessoas + 1):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / totpessoas

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
