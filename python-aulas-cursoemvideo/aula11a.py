"""
    Esse programa é referente a aula 11 do curso de Python do Curso em vídeo:
    Ele muda as cores dos prints;

    Autor: José Brenon - 18/07/2023
"""
"""print('\033[7;37;44mBrenon lindo!\033[m')
a = 3
b = 5
print('Os valores são \33[32m{}\033[m e \33[31m{}\033[m'.format(a, b))
"""
nome = 'Brenon'
cores = {'Limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá! Prazer em te conhecer, {}{}{}!!!!'.format(cores['amarelo'], nome, cores['Limpa']))