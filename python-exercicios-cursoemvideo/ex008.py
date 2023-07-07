"""
    Esse exercício é referente a aula 07 do curso de Python do Curso em vídeo:

    Desafio 008: Escreva um programa que leia um valor em metros e o exiba
    convertido em centímetros e milímetros.

    Esse programa pede para o usuário digitar um valor em metros e mostra esse valor
    convertido em todas as medidas.

    By: José Brenon - 15/04/2023
"""
n = float(input('Digite uma distância em metros: '))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000
print('A medida de {:.1f}m corresponde a: \n'
      '{}km \n{}hm \n{}dam\n{}dm \n{}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, km, hm, dam, dm, n, dm, cm, mm))
