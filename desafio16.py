d= int(input('Quantos dias o carro foi alugado? '))
k= float(input('Quantos Kilometros foram rodados? '))
a= (d*60)+(k*0.15)
print('O valor do aluguel que você deve pagar após rodar por {} dias e {} km, é de: R${:.2f}.'.format(d,k,a))