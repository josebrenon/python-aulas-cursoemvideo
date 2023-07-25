"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 041: A Confederação Nacional de Natação precisa de um programa que
    leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
    Até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JÚNIOR, até 25 anos: SÊNIOR,
    acima de 25 anos: MASTER.

    Esse programa lê o ano de nascimento de um atleta, calcula a idade conforme o ano atual,
    verifica se tiver até 9 anos mostra que é mirim, se for até 14 anos é infantil, se for
    até 19 anos é Júnior, até 25 anos é sênior, e acima de 25 é master.

    Autor: José Brenon - 22/07/2023
"""
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print('O aleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
