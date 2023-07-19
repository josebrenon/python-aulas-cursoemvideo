"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 034: Escreva um programa que pergunte o salário de um funcionário
    e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
    calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

    Esse programa pergunta o salário de um funcionário, verifica se o salário é
    superior a R$1250.00, se for calcula o valor do aumento em 10% e mostra o resultado
    se não calcula um aumento de 15% e mostra o resultado de quanto ganhava e quanto passa a ganhar
    após o aumento relativo ao valor do salário.

    Autor: José Brenon - 18/07/2023
"""

salario = float(input('Digite o salário do funcionário: R$'))

if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))
