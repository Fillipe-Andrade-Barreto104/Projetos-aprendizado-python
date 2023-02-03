pa = str(input('Digite uma palavra ')).strip().upper()
pa2 = pa.split()
pa3 = ''.join(pa2)
pa4 =''.join(reversed(pa3))
if pa3 == pa4:
    print('O que você escreveu foi: {}. O seu inverso é: {}. Como são iguais, {} é um palíndromo.'.format(pa3, pa4, pa3))
else:
    print('O que você escreveu foi: {}. O seu inverso é {}. Como são difetrentes, {} não é um palíndromo'.format(pa3,pa4,pa3))

