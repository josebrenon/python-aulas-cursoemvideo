"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro,
    triplo e raiz quadrada.

    Esse programa pede para o usuário digitar um número e mostra na tela seu dobro,
    triplo e a raiz quadrada.

    By: José Brenon - 15/04/2023
"""
n = int(input('Digite um número: '))
print('O dobro de {} é {}\nO triplo de {} é {} \n'
      'A raiz quadrada de  {} é {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
