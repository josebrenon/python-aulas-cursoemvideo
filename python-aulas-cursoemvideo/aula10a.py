"""
    Esse programa é referente a aula 10 do curso de Python do Curso em vídeo:
    Ele pede para o usuário digitar seu nome e verifica se for Brenon ele mostra uma mensagem
    se não mostra outra.

    Autor: José Brenon - 18/07/2023
"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Brenon':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
