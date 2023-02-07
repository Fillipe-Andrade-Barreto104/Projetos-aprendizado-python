from math import log
n2 = int(input('Qual a quantidade de componentes você vai querer na sequência? '))
cont = 1
fn = 0
fn1 = 0
fn2 = 0
while cont <= n2:
    if cont == 1:
        fn = 1
        fn1 = 1
    if cont == 2:
        fn = 1
        fn2 = 1
    if cont == 3:
        fn = fn1 + fn2
    if cont > 3:
        if cont % 2 != 0:
            fn1 = fn
            fn = fn1 + fn2
        else:
            fn2 = fn
            fn = fn1 + fn2     
    if cont < (n2):
        print('{} ->'.format(fn), end = ' ')
    else:
        print('{}.'.format(fn))
    cont = cont +1
    
   