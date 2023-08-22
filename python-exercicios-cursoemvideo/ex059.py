"""
    Esse exercício é referente a aula 14 do curso de Python do Curso em vídeo:

    Desafio 059: Crie um programa que leia dois valores e mostre um menu na tela:
    1 somar, 2 multiplicar 3 maior 4 novos números 5 sair do programa.
    Seu programa deverá realizar a operação solicitada em cada caso

    Esse programa lê dois valores e mostra um menu na tela perguntando qual a opção
    desejada, depois verifica enquanto for diferente de 5 ele mostra o menu e verifica
    qual foi a opção escolhida, se foi 1 ele soma os dois números e mostra o resultado,
    se foi 2 multiplica os dois, se for 3 mostra qual é o maior, se for quatro pede
    novos números e se for 5 ele finaliza o programa, se nenhuma das opções forem digitadas
    ele mostra que a opção foi invalida e mostra o menu novamente.
        
    Autor: José Brenon - 22/08/2023
"""
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input("Digite o segundo valor: "))

opcao = 0

while opcao != 5:
    print(f'Com os valores {n1} e {n2} qual a sua opção?')
    opcao = int(input("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>> Qual a sua opção: """))
    if opcao == 1:
        soma = n1 + n2 
        print(f"A soma entre {n1} e {n2} é = {soma}")

    elif opcao == 2:
        mult = n1 * n2
        
        print(f"A multiplicação entre {n1} e {n2} é = {mult}")

    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2   
        print(f"Entre {n1} e {n2} o maior é o {maior}")

    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input("Digite o segundo valor: "))

    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção invalida!, tente novamente.")
    print("=-" * 20)
    sleep(2)

print('Fim do programa, volte sempre!')
