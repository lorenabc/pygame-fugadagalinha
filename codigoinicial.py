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