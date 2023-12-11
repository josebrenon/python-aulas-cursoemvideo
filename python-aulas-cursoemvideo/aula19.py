"""
    Esse programa é referente a aula 19 do curso de Python do Curso em vídeo:

    Esse programa é sobre dicionários.

    Autor: José Brenon - 11/12/2023
"""

estado = dict()
brasil = list()

for c in range(2):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

'''pessoas = {'nome': 'Brenon', 'sexo': 'M', 'idade': 21}
pessoas['peso'] = 56.8
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #O Brenon tem 21 anos
#print(pessoas.keys())#dict_keys(['nome', 'sexo', 'idade'])
#print(pessoas.values())#dict_values(['Brenon', 'M', 21])
#print(pessoas.items())#dict_items([('nome', 'Brenon'), ('sexo', 'M'), ('idade', 21)])
"""for k in pessoas.keys():
    print(k)""" #Mostra nome, sexo, idade
for v in pessoas.values():
    print(v) # mostra Brenon, M, 21
for k, v in pessoas.items():
    print(f"{k} = {v}") #Mostra nome = Brenon, sexo = M, idade = 21, peso = 56.8
'''