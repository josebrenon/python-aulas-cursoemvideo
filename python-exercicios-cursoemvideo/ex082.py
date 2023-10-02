"""
    Esse exercício é referente a aula 17 do curso de Python do Curso em vídeo:

    Desafio 082: Crie um programa que vai ler vários números e colocar em uma lista. 
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
    os valores ímpares digitados, respectivamente. 
    Ao final, mostre o conteúdo das três listas geradas.

    Este programa criam três listas: números, pares e impares. 
    A lista números armazena todos os números digitados pelo usuário. 
    A lista pares armazena apenas os números pares digitados pelo usuário. 
    A lista impares armazena apenas os números ímpares digitados pelo usuário.
    O programa lê vários números e pergunta se o usuário quer continuar ou não. 
    Em seguida, ele separa os números pares dos ímpares e armazena-os 
    nas listas pares e impares, respectivamente.
    Por fim, o programa exibe o conteúdo das três listas.

    Autor: José Brenon - 02/10/2023
"""
numeros = list() # Lista com todos os números
pares = [] # Lista com os números pares
impares = []# Lista com os números ímpares
while True:# Enquanto for verdadeiro...
    número = int(input('Digite um número inteiro: ')) # Pede para o usuário digitar um número
    numeros.append(número) # Adicionando o número digitado a lista numeros
    r = ' ' # Inicializa a variável r com um espaço em branco
    while r not in 'SN':# Enquanto r não for 'S' ou 'N'
        r = str(input('Quer continuar [S/N]: ')).strip().upper() # Solicita ao usuário uma entrada e converte para maiúsculas
    if r == 'N':# Se r for 'N'
      break # Sai da repetição
for i, v in enumerate(numeros): #  Itera em uma lista listada de números
    if v %2 == 0: # Se o resto da divisão por dois for igual a 0
        pares.append(v)# Adiciona a lista pares
    else:
        impares.append(v)# Caso contrário, adiciona a lista impares

print('-='*40)# Imprime uma linha de separação
print('Lista de números:', numeros)# Imprime a lista de números
print('Lista de pares:', pares)# Imprime a lista de pares
print('Lista de ímpares:', impares)# Imprime a lista de ímpares
