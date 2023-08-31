"""
    Esse exercício é referente a aula 15 do curso de Python do Curso em vídeo:

    Desafio 070: Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar ou não. No final,
    mostre:
    A) qual é o total gasto na compra.

    B) quantos produtos custam mais de R$1000.

    C) qual é o nome do produto mais barato.

    Esse programa lê o nome e o preço de vários produtos pergunta se o usuário
    quer continuar, ele soma todas as compras, vê quantos foram mais de R$1000.00
    e qual foi o mais barato.

    Autor: José Brenon - 31/08/2023
"""
totcompra = maisdemil = menor = cont = 0
barato = ''
print('-'*30)
print(f'{"LOJA BRENON LINDO":^30}')
print('-'*30)
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    totcompra += preço
    if preço >= 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar: [S/N]")).strip().upper()[0]
    if opcao == "N":
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${totcompra:.2f}')
if maisdemil == 0:
    print('Não tivemos nenhum produto com mais de R$1000.00')
elif maisdemil == 1:
    print(f'Temos {maisdemil} produto com mais de R$1000.00')
else:
    print(f'Temos {maisdemil} produtos com mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
