#abrindo arquivo
import pygame
import time


def transition_screen(window):
    font = pygame.font.Font('assets/PressStart2P.ttf', 20)
    frase1 = font.render('A GALINHA FUGIU', False, (255, 255, 255))
    frase2 = font.render('AJUDE ELA A ATRAVESSAR', False, (255, 255, 255))
    frase3 = font.render('A RUA', False, (255, 255, 255))

    clock = pygame.time.Clock()
    FPS = 30
    game = True