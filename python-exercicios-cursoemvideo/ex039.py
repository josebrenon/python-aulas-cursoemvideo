"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
    conforme a sua idade, se ele ainda vai se alistar ao serviço militar,
    se é a hora exata de se alistar ou se já passou do tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

    Esse programa pergunta se o usuário é homem ou mulher, se for homem, pede para digitar
    o seu ano de nascimento, calcula a idade desse usuário conforme o ano atual, verifica
    se já tiver 18 anos ou mais deve se alistar se for menor de 18 mostra quantos anos
    ainda faltam para se alistar e o ano que será, se já estiver passado da idade mostra
    quantos anos se passaram e qual ano foi o alistamento, se for mulher só mostra que
    não é obrigatório se alistar.

    Autor: José Brenon - 22/07/2023
"""
from datetime import date

ano = date.today().year
sexo = str(input('''Qual o seu sexo? 
[ F ] Para feminino
[ M ] Para masculino
Qual a opção: '''))
if sexo == 'F':
    print('O seu alistamento não é obrigatório!')
if sexo == 'M':
    print('Seu alistamento é obrigatório')
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(ano + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        print('Seu alistamento foi em {}.'.format(ano - saldo))
elif sexo != 'F' and 'M' and 'f' and 'm':
    print('Opção invalida, tente novamente!')
