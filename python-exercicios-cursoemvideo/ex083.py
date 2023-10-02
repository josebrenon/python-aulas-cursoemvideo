"""
    Esse exercício é referente a aula 17 do curso de Python do Curso em vídeo:

    Desafio 083: Crie um programa onde o usuário digite uma expressão qualquer 
    que use parênteses. Seu aplicativo deverá analisar se a expressão passada 
    está com os parênteses abertos e fechados na ordem correta.

    Este programa verifica se uma expressão matemática é válida. 
    A função funciona da seguinte forma:
    Ela pede ao usuário para digitar uma expressão, cria uma lista vazia para 
    armazenar as aberturas dos parênteses, ela percorre cada caractere da string 
    'exp', se o caractere for um parêntese aberto, adiciona-o à pilha, se o caractere 
    for um parêntese fechado, remove o último elemento da pilha, se a pilha estiver 
    vazia, a expressão é válida, se a pilha não estiver vazia, a expressão não é válida,
    A função retorna True se a expressão for válida e False se a expressão não for válida.


    Autor: José Brenon - 02/10/2023
"""
 # Pede para digitar uma expressão
exp = str(input('Digite uma expressão: ')) 
# Cria uma lista vazia para armazenar as aberturas dos parênteses.
pilha = []
# Percorre cada caractere da string 'exp'.
for simb in exp:
    # Se o caractere for um parêntese aberto, adiciona-o à pilha.
    if simb == '(':
        pilha.append('(')
    # Se o caractere for um parêntese fechado, remove o último elemento da pilha.
    elif simb == ')':
        # Se a pilha estiver vazia, a expressão não é válida.
        if len(pilha) > 0:
            pilha.pop()
        # Se a pilha não estiver vazia, remove o último elemento da pilha e continua a execução do loop.
        else:
            pilha.append(')')
            break
# Se a pilha estiver vazia, a expressão é válida.
if len(pilha) == 0:
    print('Sua expressão está válida!')
# Se a pilha não estiver vazia, a expressão não é válida.
else:
    print('Sua expressão não está válida')

