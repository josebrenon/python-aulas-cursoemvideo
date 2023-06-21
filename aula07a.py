"""
    Esse programa é referente a aula 07 do curso de Python do Curso em vídeo:
    Ele pede para o usuário digitar dois números e efetua as operações aritméticas.

    By: José Brenon - 15/04/2023
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('='* 5, 'OS RESULTADOS SÃO', '='* 5)
print('{} + {} = {}'.format(n1, n2, s))
print('{} * {} = {}'.format(n1, n2, m))
print('{} / {} = {}'.format(n1, n2, d))
print('{} // {} = {}'.format(n1, n2, di))
print('{} ** {} = {}'.format(n1, n2, p))
print('='* 5, 'FIM', '='* 5)
