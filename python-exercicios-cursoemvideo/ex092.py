"""
    Esse exercício é referente a aula 19 do curso de Python do Curso em vídeo:

    Desafio 092: Crie um programa que leia nome, ano de nascimento e carteira de 
    trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
    diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

    Autor: José Brenon - 11/12/2023
"""
ano_atual = 2018
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = ano_atual - ano_nasc
cadastro['carteira'] = int(input('Carteira de trabalho: (0 não tem): '))
if cadastro['carteira'] > 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = ((cadastro['contratação'] + 35) - ano_atual) + cadastro['idade']
print("="*35)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
print("="*35)

