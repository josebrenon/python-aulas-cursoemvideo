"""
    Esse exercício é referente a aula 12 do curso de Python do Curso em vídeo:

    Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final, conforme a média atingida: média abaixo de 5,0: REPROVADO,
    média entre 5,0 e 6,9: RECUPERAÇÃO, média 7,0 ou superior: APROVADO.

    Esse programa pede ao usuário para digitar duas notas, calcula a média entre elas, verifica
    se ela estiver abaixo de 5,0 mostra que o aluno está reprovado, se estiver entre 5,0 e 6,9
    ele está em recuperação e se estiver acima de 7,0 esse aluno está aprovado.

    Autor: José Brenon - 22/07/2023
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média desse aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno está REPROVADO!')
elif 5 <= media < 7:
    print('O aluno esta em RECUPERAÇÃO!')
elif media >= 7.0:
    print('O aluno está APROVADO!')
