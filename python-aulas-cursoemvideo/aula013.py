"""
    Esse programa é referente a aula 13 do curso de Python do Curso em vídeo:

    Esse programa é sobre o laço for

    Autor: José Brenon - 9/08/2023
"""
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))

"""
pede o início, o fim e o tanto de passos
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

Vai de 1 até o número digitado
n = int(input("Digite um número: "))
for c in range(1, n+1):
    print(c)
print("FIM")

conta para trás
for c in range(6, 0, -1):
    print(c)
print("FIM")
"""