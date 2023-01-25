import random 
from time import sleep
hu = str(input('Vamos jogar jokenpô, humano? escolha entre pedra, papel e tesoura ')).strip().capitalize()
l = ['Pedra', 'Papel', 'Tesoura']
mac = random.choice(l)
print ('estou decidindo')
sleep(2)
if hu == mac:
    print('Ocorreu um empate.')
elif hu == 'Pedra' and mac == 'Tesoura' or hu == 'Papel' and mac == 'Pedra' or hu == 'Tesoura' and mac == 'Papel':
    print('Parabéns humano, você venceu! Na próxima eu ganho!')
elif hu == 'Pedra' and mac == 'Papel' or hu == 'Papel' and mac == 'Tesoura' or hu == 'Tesoura' and mac == 'Pedra':
    print('Haha humano, eu venci! Boa a sorte na próxima.') 
