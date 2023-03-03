from time import sleep
def maior(*num):
    t = 0
    print('-'*50)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print(f'foram informamados {t} ao todo')
        print(f'O maior número digitado foi 0')
        print('-'*50)
    else:
        for b in range(0, len(num)):
            if type(num[b]) == list:
                for c in range(0, len(num[b])):
                    print(f'{num[b][c]}', end = ' ', flush=True)  
                    sleep(0.5)
                    t += 1
                    if c == 0:
                        mai = num[b][c]
                    if num[b][c] > mai:
                        mai = num[b][c]      
            else:
                print(f'{num[b]}', end = ' ', flush=True)
                sleep(0.5)
                t +=1
                if b == 0:
                    mai = num[b]
                if num[b] > mai:
                        mai = num[b]
            
        print(f'foram informamados {t} ao todo')      
        print(f'O maior número digitado foi {mai}')
        print('-'*50)

li = list()
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

print('Agora é sua vez!'.center(50).upper())
while True:
    n =int(input('Digite os números que quer determinar qual é maior '))
    li.append(n)
    esc = str(input('Quer adicionar mais algum número? [S/N] ')).upper()[0]
    while esc != 'N' and esc != 'S':
        esc = str(input('Por favor digite S para sim ou N para não')).upper()[0]
    if esc == 'N':
        break

maior(li)