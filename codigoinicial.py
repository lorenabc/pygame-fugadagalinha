# ===== Inicialização =====
#aaa
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galinha')

# ----- Função que carrega os assets
def load_assets():
    assets = {}
    assets['font_pontos'] = pygame.font.Font('assets/PressStart2P.ttf', 15)
    assets['font_gameover'] = pygame.font.Font('assets/PressStart2P.ttf', 30)
    assets['background'] = pygame.image.load('assets/background.jpeg').convert()
    assets['galinha_img'] = pygame.image.load('assets/galinha.png').convert_alpha()
    assets['galinha_img'] = pygame.transform.scale(assets['galinha_img'], (30, 30))
    carro1_mao = pygame.image.load('assets/carros/carro1_mao.png').convert_alpha()
    carro2_mao = pygame.image.load('assets/carros/carro2_mao.png').convert_alpha()
    carro3_mao = pygame.image.load('assets/carros/carro3_mao.png').convert_alpha()
    carro4_mao = pygame.image.load('assets/carros/carro4_mao.png').convert_alpha()
    assets['carro1_mao'] = pygame.transform.scale(carro1_mao, (80, 40))
    assets['carro2_mao'] = pygame.transform.scale(carro2_mao, (80, 40))
    assets['carro3_mao'] = pygame.transform.scale(carro3_mao, (80, 40))
    assets['carro4_mao'] = pygame.transform.scale(carro4_mao, (80, 40))

    carro1_contramao = pygame.image.load('assets/carros/carro1_contramao.png').convert_alpha()
    carro2_contramao = pygame.image.load('assets/carros/carro2_contramao.png').convert_alpha()
    carro3_contramao = pygame.image.load('assets/carros/carro3_contramao.png').convert_alpha()
    carro4_contramao = pygame.image.load('assets/carros/carro4_contramao.png').convert_alpha()
    assets['carro1_contramao'] = pygame.transform.scale(carro1_contramao, (80, 40))
    assets['carro2_contramao'] = pygame.transform.scale(carro2_contramao, (80, 40))
    assets['carro3_contramao'] = pygame.transform.scale(carro3_contramao, (80, 40))
    assets['carro4_contramao'] = pygame.transform.scale(carro4_contramao, (80, 40))

    pygame.mixer.music.load('assets/sons/background.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets['som_ponto'] = pygame.mixer.Sound('assets/sons/ponto.mpeg')
    assets['som_batida'] = pygame.mixer.Sound('assets/sons/batida.mpeg')
    assets['som_fim'] = pygame.mixer.Sound('assets/sons/fatality.mp3')

    return assets