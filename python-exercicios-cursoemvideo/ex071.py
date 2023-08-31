"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
    No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
    e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
    considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

    Esse programa pergunta qual valor a ser sacado, ele começa com o valor das cédulas
    em 50 e o total de cédulas em 0, verifica se o total é maior ou igual ao valor da cédula,
    se for ele tira o valor da cédula do total (50 do total) e adiciona mais um ao total de
    cédulas, senão se o total for maior que zero ele mostra quantas cédulas foram usadas de qual valor,
    se o valor da cédula for 50 ela passa a valer 20, se for 20 passa a valer 10 e se for 10 passa a
    valer 1 e atualiza o total de cedulas para 0 por fim se o total chegar a 0 ele finaliza

    Autor: José Brenon - 31/08/2023
"""
print('='*30)
print(f'{"BANCO BRENON LINDO":^30}')
print('='*30)
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50 
totced = 0
while True:
    if total >= ced:
        total -= ced 
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco BRENON LINDO!')
print('='*30)
