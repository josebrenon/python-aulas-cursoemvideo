"""
    Esse programa é referente a aula 09 do curso de Python do Curso em vídeo:
    Ele pega a frase 'Curso em Vídeo Python' divide ela e coloca e uma lista,
    conta quantas letras 'O' maiúsculas e motra, mostra o tamanho da frase e
    mostra na palavra 2 a letra 3.

    By: José Brenon - 18/04/2023
"""
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(frase.upper().count('O'))
print(len(frase))
print(dividido[2][3])  # Mostra na palavra 2 a letra 3
