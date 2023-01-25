v = float(input('Qual o valor da casa que você quer comprar? '))
s = float(input('Qual o seu salário? '))
t = float(input('Em quantos anos você quer pagar a casa? '))
if v <= ((0.3*s)*(t*12)):
    prest = v/(t*12)
    print('O seu financiamento foi aceito, e o valor da sua prestação mensal será de R$ {:.2f}.'.format(prest))
else:
    print('Infelizmente o seu financiamento não foi aprovado')