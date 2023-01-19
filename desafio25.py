nome= str(input('Digite o nome de sua cidade '))
n= nome.strip()
n2= n.capitalize()
if 'Santo' in n2:
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')