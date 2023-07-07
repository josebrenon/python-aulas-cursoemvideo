"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 007: Desenvolva um programa que leia as duas notas de um aluno,
    calcule e mostre a sua média.

    Esse programa pede para o usuário digitar duas notas, calcula a média entre elas
    e mostra o resultado.

    By: José Brenon - 15/04/2023
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
# m = s / 2
print('A média entre {} e {} é {:.1f}'.format(n1, n2, m))
