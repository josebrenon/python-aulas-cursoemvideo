"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros,
    calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
    litro de tinta pinta uma área de 2 metros quadrados.

    Esse programa pede para o usuário digitar a largura e a altura de um parede em metros
    calcula a área e a quantidade de tinta necessária para pintá-la, e mostra os resultados.

    By: José Brenon - 15/04/2023
"""
largura = float(input('Qual a largura da sua parede: '))
altura = float(input('Qual a altura da sua parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar sua parede vais precisar de {}l de tinta.'.format(tinta))
