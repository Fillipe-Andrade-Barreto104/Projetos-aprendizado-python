from random import sample
n1= input('Qual o nome dos 4 alunos para o sorteio da ordem? ')
n2= input('')
n3= input('')
n4= input('')
l= [n1,n2,n3,n4]
esc = sample(l,4)
print('A ordem de apresentação vai ser: {}'.format(esc))