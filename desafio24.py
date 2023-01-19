n= input('Digite um número inteiro de 0 à 9999 ')

while n=='' or len(n)>4:
    n= input('Digite algum número, que corresponda ao exigido por favor. ')
if len(n)==1:
    print('O número {} \ntem como unidade {}.'.format(n,n))
elif len(n)==2:
    print('O número {} \ntem como dezena {} \ne como unidade {}.'.format(n,n[0],n[1]))
elif len(n)==3:
    print('O número {} \ntem como centana {}\ncomo dezena {}\ne como unidade {}.'.format(n,n[0],n[1],n[2]))
elif len(n)==4:
    print('O número {} \ntem como milhar {}\ncomo centena {} \ncomo dezena {} \ne como unidade {}.'.format(n,n[0],n[1],n[2],n[3]))



