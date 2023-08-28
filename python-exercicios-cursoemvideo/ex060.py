"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
    5! = 5 x 4 x 3 x 2 x 1 = 120
        
    Esse programa pede para o usuário digitar um número para saber o seu fatorial, 
    ele inicia o contador no mesmo número que foi digitado, verifica enquanto c for
    maior que 0, mostra os valores até 1 e depois calcula o fatorial do número mostrando
    o resultado no final.

    Autor: José Brenon - 28/08/2023
"""
n = int(input("Digite um número para saber o seu fatorial: "))
c = n
f = 1
print(f'Calculando o {n}! = ', end='')
while c > 0:
#for c in range(n, 0, -1):
    print(f"{c}", end="")
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end="")
    #print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f"{f}")
