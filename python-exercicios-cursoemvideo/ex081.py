"""
    Esse exercício é referente a aula 17 do curso de Python do Curso em vídeo:

    Desafio 081: Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso mostre:
    A) Quantos números foram digitados.                                                                                                                 B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

    Este programa lê vários números e os armazena em uma lista. 
    Depois de ler todos os números, ele exibe a quantidade de 
    números digitados, a lista de valores ordenada de forma 
    decrescente e verifica se o valor 5 foi digitado e está na lista.

    Autor: José Brenon - 02/10/2023
"""

numeros = list() # Inicializa a lista de números

while True: # Loop para adicionar números à lista
    numeros.append(int(input('Digite um número: '))) # Solicita um número ao usuário e adiciona o número à lista  
    r = ' ' # Inicia a variável r vazia
    while r not in 'SN': # Cria um laço para saber a resposta, e só finaliza se digitar S ou N
        r = str(input('Quer continuar [S/N]: ')).strip().upper() # Solicita ao usuário se ele deseja continuar
    if r == 'N': # Se a resposta for N ele encerra o laço
        break

print('-=' * 46) # Imprime uma linha de separação
print(f'A quantidade de números digitados foi de {len(numeros)} elementos') # Imprime a quantidade de números digitados
numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(f'A lista em ordem decrescente fica: {numeros}') # Imprime a lista em ordem decrescente
if 5 in numeros: # Verifica se o valor 5 está na lista
    print('O valor 5 faz parte desta lista.') # Se estiver, imprime uma mensagem diferente
else:
    print('O valor 5 não consta nesta lista!') # Se não estiver, imprime uma mensagem
