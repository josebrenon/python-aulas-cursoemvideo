"""
    Esse exercício é referente a aula 17 do curso de Python do Curso em vídeo:

    Desafio 080:  Crie um programa onde o usuário possa digitar cinco valores 
    numéricos e cadastre-os em uma lista, já na posição correta de inserção 
    (sem usar o sort()). No final, mostre a lista ordenada na tela.

    Esse programa solicita ao usuário a inserção de números inteiros em uma 
    lista. A lista é ordenada a cada inserção, garantindo que os números 
    sejam adicionados em ordem crescente.

    Autor: José Brenon - 02/10/2023
"""
números = list()
for c in range(5):
    número_digitado = int(input('Digite um número inteiro qualquer para adicioná-lo à lista: '))
    if len(números) == 0 or número_digitado > números[-1]:
        números.append(número_digitado)
        print(f'Número {número_digitado} adicionado ao final da lista')
    else:
        posição = 0
        while posição < len(números) and número_digitado > números[posição]:
            posição += 1
        números.insert(posição, número_digitado)
        print(f'O número {número_digitado} adicionado na posição {posição} da lista')
print('-='*30)
print('Lista ordenada: ', números)
