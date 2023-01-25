nome = str(input('Digite seu nome ')).strip().capitalize()
peso = float(input('Digite seu peso em Kg '))
altura = float(input('DIgite su altura em metros '))
imc = peso/(altura**2)

if imc < 18.5:
    print('{}, com seu imc de {:.1f}, você está abaixo do peso.'.format(nome, imc))
elif 18.5 <= imc < 25:
    print('Parabéns {}, com seu imc de {:.1f} você está com o peso ideal.'.format(nome,imc))
elif 25 <= imc < 30:
    print('Cuidado {}, com seu imc de {:.1f} você se encontra com sobrepeso.'.format(nome,imc))
elif 30 <= imc< 40:
    print('Desculpa lhe informar, mas está na hora de procurar um(a) nutricionista, pois {} com seu imc de {:.1f} você já se encontra com obesidade.'.format(nome,imc))
elif imc >= 40:
    print('Pelo bem de sua saúde {}, seria ideal você buscar ajuda profissional, pois com seu imc de {:.1f} você se encontra com obesidade morbida.'.format(nome,imc))