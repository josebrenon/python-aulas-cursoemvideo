"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
    de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais,
    ISÓSCELES: dois lados iguais, um diferente, ESCALENO: todos os lados diferentes

    Esse programa pede três seguimentos para saber se com eles é possível
    formar um triângulo, verifica se cada seguimento é menor do que a soma dos outros dois,
    e mostra se é ou não possível formar um triângulo e se todos os lados forem iguais mostra
    que é um triângulo equilátero, se tiver dois lados iguais e um diferente é isósceles, se
    todos os lados diferirem é um escaleno.

    Autor: José Brenon - 22/07/2023
"""
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')
