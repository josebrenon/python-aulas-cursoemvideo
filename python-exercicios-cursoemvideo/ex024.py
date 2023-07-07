"""
    Esse exercício é referente a aula 09 do curso de Python do Curso em vídeo:

    Desafio 024: Crie um programa que leia o nome de uma cidade diga
    se ela começa ou não com o nome “SANTO”.

    Esse programa pede para o usuário digitar o nome de uma cidade e mostra se ela começa
    ou não com "SANTO".

    By: José Brenon - 18/04/2023
"""
cid = str(input('Em que cidade você nasceu? ')).strip()
print('Na cidade que vc nasceu tem santo? {}'.format(cid[:5].upper() == 'SANTO'))
