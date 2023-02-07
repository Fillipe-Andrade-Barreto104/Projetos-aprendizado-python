n1 = float(input('Digite o primeiro termo de sua PA '))
r = float(input('Digite a razão de sua PA '))
cont = 2
pal = 0
print('Os termos de sua PA são: \n{:.1f}'.format(n1), end = ' ')
while cont <= 10:
    pa = n1 + ((cont-1)*r)
    print('{:.1f}'.format(pa), end = ' ')
    cont = cont + 1
print('\n')



cal = int(input('Digite mais quantos termos você que ver. Quando quiser terminar digite 0. '))
cal2 = 2 
while cal != 0:
    if (cont- 10) <= cal:
        cont = cont + 1
        pa = n1 + ((cont-1)*r)
        print('{:.1f}'.format(pa), end = ' ')
    if(cont- 10) > cal:
        cal2 = int(input('\nSe quiser continuar digite 1, se não digite 0.'))
        if cal2 == 1:
            cal = cal + (int(input('\nVocê quer mais quantos termos?')))
        if cal2 == 0:
            break
