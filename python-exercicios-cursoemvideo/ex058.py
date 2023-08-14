'''
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 058: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
    em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
    mostrando no final quantos palpites foram necessários para vencer.

    Esse programa faz o computador pensar em um número entre 0 e 10, pergunta para o usuário
    qual foi, verifica, se foi o mesmo número mostra que o usuário ganhou, senão verifica,
    se a resposta foi menor ele diz que é mais, senão diz que é menos, também conta quantas
    tentativas foram necessárias para vencer e mostra o resultado.
    
    Autor: José Brenon - 14/08/2023
'''
from random import randint

n = randint(0, 10)
r = int(input('''Pensei em um número entre 0 e 10, consegue me dizer qual foi?
Qual número eu pensei? '''))
cont = 1

while n != r:
    cont += 1
    if r < n:
        r = int(input('Mais... Tente novamente: '))
    else:
        r = int(input('Menos... Tente novamente: '))
    
if r == n and cont == 1:
    print('''Você ganhou! O número que eu pensei foi exatamente o {}
Você precisou de {} tentativa'''.format(n, cont))
else:
    print('''Você ganhou O número que eu pensei foi exatamente o {}
Você precisou de {} tentativas'''.format(n, cont))
