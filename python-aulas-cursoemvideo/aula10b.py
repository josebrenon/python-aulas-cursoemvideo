"""
    Esse programa é referente a aula 10 do curso de Python do Curso em vídeo:
    Ele pede para o usuário digitar duas notas, calcula a média entre elas
    e verifica se é maior que 6 mostra uma mensagem se não mostra outra.

    Autor: José Brenon - 18/07/2023
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
