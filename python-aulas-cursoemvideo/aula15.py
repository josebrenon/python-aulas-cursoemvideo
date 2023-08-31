"""
    Esse programa é referente a aula 15 do curso de Python do Curso em vídeo:

    Esse programa é sobre o laço while true e break.

    Autor: José Brenon - 31/08/2023
"""
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma é igual a {s}')