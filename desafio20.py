from random import choice
n1= input('Digite o nome dos seus 4 alunos ')
n2= input('')
n3= input('')
n4= input('')
l= [n1,n2,n3,n4]
esc= choice(l)
print('Quem apagará o quadro dessa vez vai ser {}'.format(esc))