"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre
    seu novo salário, com 15% de aumento.

    Esse programa pede para o usuário digitar o salário de um funcionário,
    calcula e mostra o resultado com 15% de aumento.

    By: José Brenon - 15/04/2023
"""
salario = float(input('Qual é o salario do funcionário? R$'))
novo = salario + salario * 15 / 100
print('O funcionario que recebia R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
