n1 = int(input('Digite um número para eu calcular seu fatorial '))
i = n1 - 1
fat = n1
print('{}! = {} x '.format(n1, n1),end='')
while i > 0 :
    fat = fat * i
    print('{} '.format(i), end = '')
    i = i - 1
    if i >= 1:
        print('x ',end = '')
print('= {}'.format(fat))