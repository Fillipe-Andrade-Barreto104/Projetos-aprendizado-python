v = float(input('Qual a velocidade do seu carro? '))
if v <= 80:
    print('Muito bem, você se encontra na velocidade permitida!')
else:
    m = (v-80)*7
    print('Você ultrapassou a velocidade limite e pagará uma multa de {:.2f} reais.'.format(m))