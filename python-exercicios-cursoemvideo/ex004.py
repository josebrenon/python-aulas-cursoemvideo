"""
    Esse exercício é referente a aula 06 do curso de Python do Curso em vídeo:

    Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela
    o seu tipo primitivo e todas as informações possíveis sobre ele.

    Esse programa pede para o usuário digitar algo e mostra na tela seu tipo primitivo e todas
    as informações sobre ele.

    By: José Brenon - 15/04/2023
"""
n = input('Digite algo: ')
tp = type(n)
es = n.isspace()
en = n.isnumeric()
an = n.isalnum()
mai = n.isupper()
minu = n.islower()
#cap
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabetico?', n.isalpha())
print('É alfanumerico?', n.isalnum())
print('Esta em maiusculas?', n.isupper())
print('Esta em minusculas?', n.islower())
print('Esta captalizada?', n.istitle())
