"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a
    compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
    quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
    ou então o empréstimo será negado.

    Esse programa pergunta o valor da casa, o salário do comprador e em quantos anos
    ele vai pagar, calcula quantos meses tem a quantidade de ano escolhida e o valor da prestação,
    verifica se esse valor excedeu 30% do salário, se exceder mostra que foi negado, se não mostra
    que foi aprovado.

    Autor: José Brenon - 20/07/2023
"""
v_casa = float(input('Digite qual é o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
qnt_anos = int(input('Digite quantos anos de financiamento: '))
# Calculando a prestação
prestacao = v_casa / (qnt_anos * 12)
# Mostra o valor da prestação
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(v_casa, qnt_anos, prestacao))
# Verifica se o empréstimo pode ser concedido ou não
if prestacao <= salario * 30 / 100:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
