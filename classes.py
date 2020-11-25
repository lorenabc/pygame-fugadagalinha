import random
import pygame
from constantes import WIDTH, HEIGHT

class GalinhaInicio(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.pontos = 0
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 70.5
        self.rect.centery = 200
        self.y = 200
        self.speedy = 2

    def update(self):
        # Atualização da posição da galinha
        self.rect.y += self.speedy
        self.y += self.speedy
    
    class GalinhaPlayer(pygame.sprite.Sprite):
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
        # Atualização da posição da nave
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Se pontua volta para o inicio
        if self.rect.top < 5:
            self.som.play()
            self.rect.bottom = HEIGHT
            self.pontos += 1

