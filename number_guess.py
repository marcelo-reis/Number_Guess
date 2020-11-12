# >> Import
from sys import exit
from time import sleep
import pygame as pygame
from pygame.locals import *


# >> Functions
def start_logo_show():
    pygame.display.set_caption('Wilbor Games')
    sleep(.333)
    screen.fill(WHITE)
    screen.blit(logo, (169.5, 108))
    pygame.mixer.music.load('audio/ninito.ogg')
    pygame.mixer.music.play()
    pygame.event.wait()
    pygame.display.update()
    sleep(1.8333)


# >> Variables
# value variable
valor_maximo = 10
valor_medio = 5
valor_minimo = 0
# text variable
text1 = 'NUMBER_GUESS'
text2 = f'De 0 - 10 você pensou em: {valor_medio} ?'
text3 = 'Maior'
text4 = 'Menor'
text5 = 'Correto?'
# screen variable
screenSize = (640, 480)
# image variable
logo_path = 'img/wilborLogo5.png' # Designed by dgim-studio / Freepik
# color variable
# button color
DimGray = (0x69, 0x69, 0x69)
Silver = (0xC0, 0xC0, 0xC0)
# text color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# init
pygame.init()
pygame.font.init()
pygame.mixer.init()

# screen
screen = pygame.display.set_mode(screenSize, 0, 32)
# images
logo = pygame.image.load(logo_path).convert_alpha()
# font
font_60px = pygame.font.SysFont('Retron2000', 60)
font_30px = pygame.font.SysFont('Retron2000', 30)
text1_surface = font_60px.render(text1, False, BLACK)
text2_surface = font_30px.render(text2, False, BLACK)
text3_surface = font_30px.render(text3, False, BLACK)
text4_surface = font_30px.render(text4, False, BLACK)
text5_surface = font_30px.render(text5, False, BLACK)

# function call
start_logo_show()

while True:
    # Preenche a tela com uma cor (Red, Green, Blue)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                # altera o texto 3
                valor_minimo = valor_medio
                valor_medio = (valor_minimo + valor_maximo) / 2
                text3_surface = font_30px.render(text3, False, GREEN)
                # altera o texto 2
                text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                text2_surface = font_30px.render(text2, False, BLACK)
            if event.key == K_DOWN:
                # altera o texto 4
                valor_maximo = valor_medio
                valor_medio = (valor_minimo + valor_maximo) / 2
                text4_surface = font_30px.render(text4, False, RED)
                # altera o texto 2
                text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                text2_surface = font_30px.render(text2, False, BLACK)
            if event.key == K_RETURN:
                if text5 == 'Correto?':
                    # altera o texto 5
                    text5 = 'Reiniciar?'
                    text5_surface = font_30px.render(text5, False, BLUE)
                    # altera o texto 2
                    text2 = f'Eu sabia!!! Você escolheu {round(valor_medio)}'
                    text2_surface = font_30px.render(text2, False, BLACK)
                elif text5== 'Reiniciar?':
                    # retorna as variaveis ao valor original
                    valor_maximo = 10
                    valor_medio = 5
                    valor_minimo = 0
                    # altera o texto 5
                    text5 = 'Correto?'
                    text5_surface = font_30px.render(text5, False, BLACK)
                    # altera o texto 2
                    text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                    text2_surface = font_30px.render(text2, False, BLACK)

        if event.type == KEYUP:
            if event.key == K_UP:
                text3_surface = font_30px.render(text3, False, BLACK)
            if event.key == K_DOWN:
                text4_surface = font_30px.render(text4, False, BLACK)
            if event.key == K_RETURN:
                if text5 == 'Reiniciar?':
                    # mantem a cor do texto 5
                    text5_surface = font_30px.render(text5, False, BLUE)
                    # # altera o texto 2
                    # text2 = f'Eu sabia!!! Você escolheu {valor_medio}'
                    # text2_surface = font_30px.render(text2, False, BLACK)
                elif text5 == 'Correto?':
                    # retorna as variaveis ao valor original
                    valor_maximo = 11
                    valor_medio = 5
                    valor_minimo = 0
                    # altera o texto 5
                    text5 = 'Correto?'
                    text5_surface = font_30px.render(text5, False, BLACK)
                    # altera o texto 2
                    ext2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                    text2_surface = font_30px.render(text2, False, BLACK)

        x, y = pygame.mouse.get_pos()
        # pygame.display.set_caption(f'x = {x} e y = {y}')
        # retangulo maior
        if 240 <= x <= 420 and 211 <= y <= 262:
            if event.type == MOUSEBUTTONDOWN:
                # altera o texto 3
                valor_minimo = valor_medio
                valor_medio = (valor_minimo + valor_maximo) / 2
                text3_surface = font_30px.render(text3, False, GREEN)
                # altera o texto 2
                text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                text2_surface = font_30px.render(text2, False, BLACK)
            if event.type == MOUSEBUTTONUP:
                text3_surface = font_30px.render(text3, False, BLACK)
        # retangulo menor
        if 240 <= x <= 420 and 294 <= y <= 345:
            if event.type == MOUSEBUTTONDOWN:
                # altera o texto 4
                valor_maximo = valor_medio
                valor_medio = (valor_minimo + valor_maximo) / 2
                text4_surface = font_30px.render(text4, False, RED)
                # altera o texto 2
                text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                text2_surface = font_30px.render(text2, False, BLACK)
            if event.type == MOUSEBUTTONUP:
                text4_surface = font_30px.render(text4, False, BLACK)
        # retangulo correto/reiniciar
        if 240 <= x <= 420 and 377 <= y <= 428:
            if event.type == MOUSEBUTTONDOWN:
                if text5 == 'Correto?':
                    # altera o texto 5
                    text5 = 'Reiniciar?'
                    text5_surface = font_30px.render(text5, False, BLUE)
                    # altera o texto 2
                    text2 = f'Eu sabia!!! Você escolheu {round(valor_medio)}'
                    text2_surface = font_30px.render(text2, False, BLACK)
                elif text5 == 'Reiniciar?':
                    # retorna as variaveis ao valor original
                    valor_maximo = 10
                    valor_medio = 5
                    valor_minimo = 0
                    # altera o texto 5
                    text5 = 'Correto?'
                    text5_surface = font_30px.render(text5, False, BLACK)
                    # altera o texto 2
                    text2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                    text2_surface = font_30px.render(text2, False, BLACK)
            if event.type == MOUSEBUTTONUP:
                if text5 == 'Reiniciar?':
                    # mantem a cor do texto 5
                    text5_surface = font_30px.render(text5, False, BLUE)
                    # # altera o texto 2
                    # text2 = f'Eu sabia!!! Você escolheu {valor_medio}'
                    # text2_surface = font_30px.render(text2, False, BLACK)
                elif text5 == 'Correto?':
                    # retorna as variaveis ao valor original
                    valor_maximo = 11
                    valor_medio = 5
                    valor_minimo = 0
                    # altera o texto 5
                    text5 = 'Correto?'
                    text5_surface = font_30px.render(text5, False, BLACK)
                    # altera o texto 2
                    ext2 = f'De 0 - 10 você pensou em: {round(valor_medio)} ?'
                    text2_surface = font_30px.render(text2, False, BLACK)

    screen.blit(text1_surface, (87.5, 23))
    screen.blit(text2_surface, (80, 131))
    pygame.draw.rect(screen, DimGray, (240, 211, 180, 50))
    screen.blit(text3_surface, (277.5, 214))
    pygame.draw.rect(screen, DimGray, (240, 294, 180, 50))
    screen.blit(text4_surface, (271, 297))
    pygame.draw.rect(screen, DimGray, (240, 377, 180, 50))
    screen.blit(text5_surface, (255, 380))

    pygame.display.flip()
