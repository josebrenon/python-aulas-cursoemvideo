"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 072: Crie um programa que tenha uma dupla totalmente preenchida 
    com uma contagem por extenso, de zero até vinte. Seu programa deverá ler 
    um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

    Esse programa Lê um número pelo teclado e verifica se ele está entre 0 e 20,
    depois ele analisa qual foi o número digitado e mostrar qual é o correspondente
    na tupla.

    Autor: José Brenon - 27/09/2023
"""
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze','Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente!', end=' ')
print(f'Você escolheu o {numeros[escolha]}')
while True:
    opcao = str(input('Você quer continuar? [S/N]: '))
    if opcao in 'Nn':
        break
    if opcao not in 'SsnN':
        print('Opção invalida!', end=' ')
    if opcao in 'Ss':
        while True:
            escolha = int(input('Digite um número entre 0 e 20: '))
            if 0 <= escolha <= 20:
                break
            print('Tente novamente!', end=' ')
        print(f'Você escolheu o {numeros[escolha]}')
print(f'{"FIM":.^21}')
