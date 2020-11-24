# ===== Inicialização =====

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

# ----- Inicia as sprites
class Galinha(pygame.sprite.Sprite):
    def _init_(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.pontos = 0
        self.image = assets['galinha_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 3
        self.rect.bottom = HEIGHT
        self.speedy = 0
        self.som = assets['som_ponto']

    def update(self):
        # Atualização da posição da galinha
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Se pontua volta para o inicio
        if self.rect.top < 5:
            self.som.play()
            self.rect.bottom = HEIGHT
            self.pontos += 1