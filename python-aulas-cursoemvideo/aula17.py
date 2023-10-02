'''num = [2, 5, 9 , 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elemantos.')
'''
'''valores = list()
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c , v in enumerate(valores):
    print(f'Na posição {c} encontrei o número {v}')
print('Cheguei ao final da lista')
'''
a = [0, 1, 2, 3, 4, 5, 6, 7]
b = a[:]
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
