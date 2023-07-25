"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
    calcule seu Índice de Massa Corporal (IMC) e mostre seu status, conforme a tabela abaixo:
    IMC abaixo de 18,5: Abaixo do Peso, entre 18,5 e 25: Peso Ideal, 25 até 30: Sobrepeso,
    30 até 40: Obesidade, Acima de 40: Obesidade Mórbida.

    Esse programa lê o peso e a altura de uma pessoa, calcula o IMC, verifica se estiver
    abaixo de 18,5 mostra que está abaixo do peso, se estiver entre 18,5 e 25 mostra que está
    no peso ideal, se estiver de 25 até 30 é sobrepeso, se estiver de 30 a 40 é obesidade e se
    estiver acima de 40 é obesidade mórbida.

    Autor: José Brenon - 25/07/2023
"""
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('OPA! Você está ABAIXO DO PESO!')
elif imc <= 25:
    print('PARABÉNS! Você está na faixa de PESO NORMAL!')
elif imc <= 30:
    print('Você está na faixa de SOBREPESO!')
elif imc <= 40:
    print('Você está na faixa de OBESIDADE!')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA, CUIDADO!')
