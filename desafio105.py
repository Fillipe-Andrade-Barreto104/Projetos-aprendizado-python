def leiaint(txt = ''):
    n = input(f'{txt} ')
    if n.strip() != '':    
        if n[0] == '-':
            while n[1:].isdigit() == False:
                print('Erro, Por favor digite um número inteiro')
                n = input(f'{txt} ')
            return n 
        else:
            while n.isdigit() == False:
                print('Erro, Por favor digite um número inteiro')
                n = input(f'{txt} ')  
            return n
    else:
        while n[1:].isdigit() == False:
            print('Erro, Por favor digite um número inteiro')
            n = input(f'{txt} ')
        return n 
        


n = leiaint('Digite um número ')
print(f'Você acaba de digitar o número {n}')