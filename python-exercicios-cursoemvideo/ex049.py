"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 049: Refaça o DESAFIO 9, mostrando a tabuada de um
    número que o usuário escolher, só que agora utilizando um laço for.

    Esse programa pede um número inteiro e usando o laço for mostra a sua tabuada.

    Autor: José Brenon - 09/08/2023
"""
n = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, (n * c)))
