#importando a biblioteca pygame
import pygame

#Fazendo o mixer do pygame começar
pygame.mixer.init()

#fazendo o mixer do pygame carregar a musica
pygame.mixer.music.load('01 Nightmare.mp3')

#escolhendo o volume da musica. Ps: cuidado pois 1 é 100%
pygame.mixer.music.set_volume(0.4)

#para começar a musica
pygame.mixer.music.play()

#um loop sempre começa como verdadeiro, e nse não o tiver para analisar o que a pessoa quer, a musica começa e para no mesmo milisegundo 
while True:

#é dada as opções ao usuário e o que ele digitar é armazenado em uma váriavel
    pa=input('digite p para pausar, v para voltar ou s para sair ')


#então vem as condicionais em caso de a de music.stop() seja usada o script para de rodar, como ele normalmente faria
    if pa == 'p':
        pygame.mixer.music.pause()
    elif pa == 'v':
        pygame.mixer.music.unpause()
    elif pa == 's':
        pygame.mixer.music.stop()
        break
#a musica vai tocar uma vez, então parar, depois para fazer o sript parar tem que parar o loop

