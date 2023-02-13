import random
soma = 0
cont = 0
while True:
    n = int(input('Vamos jogar par ou impar. Então primeiro digite um número inteiro de 0 até 10 '))
    while n > 5:
        n = int(input('Por favor digite um número entre 0 e 10'))
    esc = int(input('Você pode escolher: [0] para par ou [1] para impar? '))
    while esc > 1:
        esc = int(input('Por favor digite ou [0] para par ou [1] para impar '))
    nm = random.randint(0,11)
    soma = n + nm
    if esc == 0 and soma % 2 != 0:
        print(f'Você perdeu, pois a máquina escolheu {nm} e a soma deu {soma}.')
        break
    if esc == 1 and soma % 2 == 0:
        print(f'Você perdeu, pois a máquina escolheu {nm} e a soma deu {soma}.') 
        break
    print(f'Você venceu, pois a máquina escolheu {nm} e a soma deu {soma}.')
    print('Vamos jogar novamente')
    cont = cont + 1
print(f'Você perdeu dessa vez, mas ao todo você venceu {cont} vezes.')
