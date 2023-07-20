"""
    Esse programa é referente a aula 12 do curso de Python do Curso em vídeo:
    Ele pede para o usuário digitar seu nome e verifica se for Brenon ele mostra uma mensagem
    se for outro nome especificado no programa mostra outra mensagem se não mostra outra.

    Autor: José Brenon - 18/07/2023
"""
nome = str(input('Qual é seu nome? '))
if nome == 'Brenon':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
