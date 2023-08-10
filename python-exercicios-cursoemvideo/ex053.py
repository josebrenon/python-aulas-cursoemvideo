"""
    Esse exercício é referente a aula 13 do curso de Python do Curso em vídeo:

    Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela
    é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
    APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
    ANOTARAM A DATA DA MARATONA.

    Esse programa lê uma frase, tira os espaços da frente e de trás, coloca
    tudo em maiusculo, separa as palavras, junta todas as palavras sem os espaços
    do meio e usa o for para inverter a frase pegando da primeira letra até a ultima
    mostrando de trás para frente, depois mostra como ficou as duas frases (normal e invertida)
    e verifica se o inverso é igual ao junto se for mostra que é um palíndromo senão mostra
    que não é.

    Autor: José Brenon - 09/08/2023
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
