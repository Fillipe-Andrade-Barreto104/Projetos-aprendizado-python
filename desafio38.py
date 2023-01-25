num = int(input('Digite um número interio '))
esc = int(input('Escolha se seu número será trnasformado para \n\033[31m(1) binário\033[m\n\033[33m(2) octal \033[m\n\033[32m(3) hexadecimal\033[m\n '))

if esc == 1:
    b = bin(num)
    print('O número {} em binário fica {}.'.format(num,b))
elif esc == 2:
    o = oct(num)
    print('O número {} em octal fica {}.'.format(num,o))
elif esc == 3:
    h = hex(num)
    print('O número {} em hexadecimal fica {}.'.format(num,h)) 
else:
    print('Na sua próxima tentativa digite, por favor, algo que o conversor possa ler.')