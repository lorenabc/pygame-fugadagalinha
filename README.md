# pygame-fugadagalinha
import pygame
from constantes import WIDTH_CARRINHO, HEIGHT_CARRINHO, WIDTH_GALINHA, HEIGHT_GALINHA
def load_assets():
    assets = {}
    assets['font_pontos'] = pygame.font.Font('assets/PressStart2P.ttf', 15)
    assets['font_gameover'] = pygame.font.Font('assets/PressStart2P.ttf', 30)
    assets['font_gameover_texto'] = pygame.font.Font('assets/PressStart2P.ttf', 10)
    assets['font_inicio_titulo'] = pygame.font.Font('assets/PressStart2P.ttf', 20)
    assets['font_inicio_texto'] = pygame.font.Font('assets/PressStart2P.ttf', 15)
    assets['background'] = pygame.image.load('assets/background.jpeg').convert()
    assets['background_inicio'] = pygame.image.load('assets/background_inicio.png').convert()
    assets['galinha_img'] = pygame.image.load('assets/galinha.png').convert_alpha()
    assets['galinha_img'] = pygame.transform.scale(assets['galinha_img'], (WIDTH_GALINHA, HEIGHT_GALINHA))