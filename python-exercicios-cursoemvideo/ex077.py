"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 076: Crie um programa que tenha uma tupla com várias palavras 
    (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
    quais são as suas vogais.

    Esse programa cria uma tupla com varias palavras mostra todas elas e quais
    são as vogais delas.

    Autor: José Brenon - 02/10/2023
"""
palavras = ('curso', 'aprender', 'gratis', 'loja', 'python', 'linguagem',
            'praticar','programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} existem ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')