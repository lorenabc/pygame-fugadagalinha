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