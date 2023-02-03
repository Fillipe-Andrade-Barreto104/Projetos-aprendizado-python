a = int(input('Digite um número inteiro '))
div = []
for c in range(1,a+1):
    if a % c == 0:
        div.append(c)
if len(div) == 2:
    print('O número {} é um número primo.'.format(a))
else:
    print('O número {} não é um número primo.'.format(a))
