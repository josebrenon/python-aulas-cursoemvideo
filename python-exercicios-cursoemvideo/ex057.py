'''
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
    Caso esteja errado, peça a digitação novamente até ter um valor correto.

    Esse programa pede para o usuário digitar seu sexo e verifica se foi M ou F 
    senão mostra uma mensagem de erro e repete o progama até que seja a opção correta.

    Autor: José Brenon - 14/08/2023
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
