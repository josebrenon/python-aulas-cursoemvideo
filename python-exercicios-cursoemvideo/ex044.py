"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto,
    considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto
    à vista no cartão: 5% de desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.

    Esse programa lê o preço das compras, calcula o preço normal conforme a condição de pagamento, se for à vista
    tem 10% de desconto, se for à vista no cartão tem 5% de desconto, se for em até 2x no cartão ele calcula as
    duas parcelas e mostra com o valor normal sem desconto, se for 3x ou mais no cartão ele pergunta em quantas
    parcelas, calcula e mostra o valor normal com 20% de juros.

    Autor: José Brenon - 25/07/2023
"""
print('{:=^40}'.format('LOJAS BRENON'))
preco = float(input('Digite o preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a sua opção? '''))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} á vista no dinheiro/cheque vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} á vista no cartão vai custar R${:.2f}'.format(preco, total))
elif opcao == 3:
    duasvezes = preco / 2
    print('Sua compra de R${:.2f} em 2 parcelas de R${:.2f} '
          'vai custar R${:.2f} no final.'.format(preco, duasvezes, preco))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Em quantas parcelas você quer fazer? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('Opção invalida, tente novamente!')
