"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado 
    e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado
    o primeiro valor 3.
    C) Quais foram os números pares.

    Esse programa Lê quatro valores pelo teclado e guarda eles em uma tupla, 
    conta e mostra quantas vezes o número 9 foi digitado verifica e mostra
    em qual posição foi digitado o primeiro valor 3 e por fim verifica e mostra
    quantos foram os números pares. 

    Autor: José Brenon - 29/09/2023
"""
num = (int(input(f'Digite um número: ')), int(input(f'Digite outro número: ')), int(input(f'Digite mais um número: ')),
       int(input(f'Digite o último número: ')))
print(f'Os números digitados foram {num}')
if 9 in num:
    if num.count(9) == 1:
        print(f'O número 9 foi digitado {num.count(9)} vez.')
    else:    
        print(f'O número 9 foi digitado {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na {num.index(3)+1}ª posição')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares digitados foram: ',end='')
for n in num:
    if n %2 == 0:
        print(n, end=' ')