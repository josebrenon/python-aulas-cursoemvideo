"""
    Esse exercício é referente a aula 19 do curso de Python do Curso em vídeo:

    Desafio 090: Faça um programa que leia nome e média de um aluno, 
    guardando também a situação em um dicionário. No final, 
    mostre o conteúdo da estrutura na tela.

    Autor: José Brenon - 11/12/2023
"""
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] >= 7:
    ficha['situação'] = 'aprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'em recuperação'
else:
    ficha['situação'] = 'reprovado'
print("="*30)
for k, v in ficha.items():
    print(f"- {k} é igual a {v}")
print("="*30)
