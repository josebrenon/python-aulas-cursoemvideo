"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 061: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
    mostrando os 10 primeiros termos da progressão usando a estrutura while.

    Esse programa lê o primeiro termo e a razão de uma PA e mostra os seus 10
    primeiros termos.

    Autor: José Brenon - 28/08/2023
"""
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = pt
c = 1
while c <= 10:
    print(f"{t} -> ", end='')
    t += r
    c += 1
print('FIM')