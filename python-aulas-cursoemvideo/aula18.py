"""
    Esse programa é referente a aula 18 do curso de Python do Curso em vídeo:

    Esse programa é sobre listas compostas.

    Autor: José Brenon - 03/10/2023
"""
'''teste = list()
teste.append('Brenon')
teste.append(21)
galera = list()
galera.append(teste[:]) # copia os valores da lista teste para galera, mas não altera o conteúdo original
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)
'''
galera = list()
dado = list()
totmai = totmeno = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmeno +=1
print(f'Temos {totmai} maiores e {totmeno} menores de idade.')
