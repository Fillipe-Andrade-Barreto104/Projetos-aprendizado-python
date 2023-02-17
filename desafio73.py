numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trese', 'quatorse', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    print('-'*30)
    n = int(input('Digite um número inteiro entre 0 e 20 '))
    while n <= 0 or n > 20:
        n = int(input('Tente novamente. Digite um número inteiro entre 0 e 20 '))
    print(f'Você digitou {numeros[n]}')
    esc = str(input('Você quer continuar? [S] para sim e [N] para não. ')).upper()[0]
    print('-'*30)
    if esc == 'N':
        break
print('FIM')
print('-'*30)
