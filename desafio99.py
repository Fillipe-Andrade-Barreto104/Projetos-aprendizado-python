from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo*(-1)
    if passo == 0:
        passo = 1
    print('-'*40)
    print(f'Contagem de {inicio:.0f} até {fim:.0f} em {passo:.0f}')
    if fim > inicio:
        print(f'{inicio:.0f}', end = ' ', flush=True)
        sleep(0.5)
        soma = inicio
        while soma <= (fim):
            soma = soma + passo
            if soma > fim:
                break
            print(f'{soma:.0f}', end=' ', flush=True)
            sleep(0.5)
    if inicio > fim: 
        print(f'{inicio:.0f}', end = ' ', flush=True)
        sleep(0.5)
        soma = inicio
        while soma >= (fim):
            soma = soma - passo
            if soma < fim:
                break
            print(f'{soma:.0f}', end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
    print('-'*40)
        
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i = float(input('Inicio: '))
f = float(input('Fim: '))
p = float(input('Passo: '))
contador(i, f, p)

