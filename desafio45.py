valor = float(input('Digite o valor que será pago '))
forma = int(input('Digite a forma de pagamento que deseja usar:\n(1) Em dinheiro ou cheque\n(2) À vista no cartão\n(3) em até 2x no cartão\n(4) 3x ou mais no cartão\n '))

if forma == 1:
    v = valor*0.9
    print('O valor que você trá de pagar ao todo será de {:.2f}.'.format(v))
elif forma == 2:
    v1 = valor*0.95
    print('O valor total a ser pago será de {:.2f}.'.format(v1))
elif forma == 3:
    print('O valor total a ser pago será de {:.2f}.'.format(valor))
elif forma == 4:
    v2 = valor*1.2
    print('O valor total a ser pago vai ser de {:.2f}.'.format(v2))