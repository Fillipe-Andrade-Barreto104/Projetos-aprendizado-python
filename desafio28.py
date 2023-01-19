nome= str(input('Digite seu nome '))
n= nome.strip()
n1= n.split()
print('Seu nome sendo {}, o primeiro nome é {} e o último nome {}.'.format(n,n1[0],n1[-1]))