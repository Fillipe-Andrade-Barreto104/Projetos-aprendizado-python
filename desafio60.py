n1 = float(input('Digite um número '))
n2 = float(input('Digite outro número '))
esc = 0
soma = ''
mult = ''
maior = ''
while esc != 5:
    esc = int(input('Escolha uma das opções:\n[1] Somar\n[2] Multiplicar\n[3] Saber qual é o maior\n[4] Inserir novos números\n[5] Sair do programa.\n '))
    if esc == 1:
        soma = n1 + n2
        if soma != '':
            print('O resultado da soma foi {:.2f}.\n'.format(soma))
    if esc == 2:
        mult = n1 * n2
        if mult != '':
            print('O resultado da multiplicação foi de {:.2f}.\n'.format(mult))
    elif esc == 3:
        if n1 > n2:
            maior = n1
            if maior != '':
                print('O número maior foi {:.2f}.\n'.format(maior))
        else:
            maior = n2
            if maior != '':
                print('O número maior foi {:.2f}.\n'.format(maior))
    elif esc == 4:
        n1 = float(input('Digite o valor alternativo '))
        n2 = float(input('Digite o outro valor '))
print('Programa finalizado.')
