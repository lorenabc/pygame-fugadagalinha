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

class Carro(pygame.sprite.Sprite):
    def _init_(self, img, y, direcao):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.direcao = direcao
        if self.direcao == 'mao':
            self.rect.x = WIDTH + 100
            self.speedx = random.randint(-8, -2)
        if self.direcao == 'contramao':
            self.rect.x = -100
            self.speedx = random.randint(2, 8)

    def update(self, pontos):
        # Atualizando a posição do carro
        if self.direcao == 'mao':
            self.rect.x += self.speedx - pontos * 2
        if self.direcao == 'contramao':
            self.rect.x += self.speedx + pontos * 2

        # Se o carro passar do final da tela, volta para trás.S
        if self.rect.right < -20 and self.direcao == 'mao':
            self.rect.x = WIDTH + 100
        if self.rect.left > WIDTH + 20 and self.direcao == 'contramao':
            self.rect.x = -100