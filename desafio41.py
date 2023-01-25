n1 = float(input('Digite sua primeira nota '))
n2 = float(input('Digite sua segunda nota '))
m = (n1+n2)/2

if m < 5:
    print('Você foi reprovado por ter tido média de {:.2f}.'.format(m))
elif 5 < m < 6.9:
    print('Você foi para reprovação por ter tirado média de {:.2f}.'.format(m))
elif m >= 7:
    print('Você foi aprovado com média de {:.2f}.'.format(m))
