#nome =str(input('Qual seu nome '))
#if nome == 'Gustavo':
#    print('Parabéns você tem nome de rei!')
#else:
#    print('Bem vindo a existência reles plebeu.')
#print('--FIM--')

n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
n3 = float(input('Digite a terceira nota '))
m = (n1+n2+n3)/3
if m >= 6:
    print('Parabéns você passou!')
else:
    print('Então, é que assim... Você não passou!')
print('Bom final de semestre, e sua média foi {}'.format(m))
