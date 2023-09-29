"""
    Esse exercício é referente a aula 16 do curso de Python do Curso em vídeo:

    Desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da 
    Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
    Depois mostre:
    a) Os 5 primeiros times. b) Os últimos 4 colocados.
    c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

    Esse programa cria uma tupla com os vinte primeiros colocados da tabela do 
    campeonato brasileiro, depois mostra quais são os 5 primeiros colocados, depois
    os 4 últimos colocados, organiza eles em ordem alfabética e por fim mostra em que
    posição está o time da Chapecoense.

    Autor: José Brenon - 27/09/2023
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
        'Atlético-PR', 'Bahia','São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória','Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=-' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('=-' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('=-' * 15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('=-' * 15)
print(f'O time da Chapecoense está na posição: {times.index("Chapecoense")+1}')
print('=-' * 15)
