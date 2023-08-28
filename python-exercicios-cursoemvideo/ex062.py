"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 062: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
    mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

    Esse programa lê o primeiro termo e a razão de uma PA e mostra os seus 10
    primeiros termos e pergunta quantos termos a mais quer mostrar, ele para
    quando o usuário não quiser mostrar mais nenhum termo (0).

    Autor: José Brenon - 28/08/2023
"""
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f"{t} -> ", end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer adicionar a mais? '))
print(f'A progressão foi finalizada com {total} termos no total.')
