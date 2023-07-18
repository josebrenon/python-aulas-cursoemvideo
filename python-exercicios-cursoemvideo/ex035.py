"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 035: Desenvolva um programa que leia o comprimento de três retas
    e diga ao usuário se elas podem ou não formar um triângulo.

    Esse programa pede três seguimentos para saber se com eles é possivel
    formar um triângulo, verifica se cada seguimento é menor do que a soma dos outros dois,
    e mostra se é ou não possivel formar um triângulo.

    Autor: José Brenon - 18/07/2023
"""

print('-=-' * 20)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=-' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo"')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')
