# ===== Inicialização =====
# ----- Importa e inicia pacotes
import random
import pygame
from constantes import WIDTH, HEIGHT

#Classe utilizada na animação na tela inicial
class GalinhaInicio(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 70.5
        self.rect.centery = 200
        self.y = 200    #variavel que guarda o valor y da galinha
        self.speedy = 2

    def update(self):
        # Atualização da posição da galinha
        self.rect.y += self.speedy
        self.y += self.speedy

#Classe que cria a galinha utilizada pelo jogador na tela de jogo
class GalinhaPlayer(pygame.sprite.Sprite):
    def __init__(self, img, som):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.pontos = 0
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 3
        self.rect.bottom = HEIGHT
        self.speedy = 0
        self.som = som

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
    def __init__(self, img, y, direcao):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.direcao = direcao

        #Dependendo da direção a velocidade e posição incial do carro é diferente
        if self.direcao == 'mao':
            self.rect.x = WIDTH + 100
            self.speedx = random.randint(-8, -2)
        if self.direcao == 'contramao':
            self.rect.x = -100
            self.speedx = random.randint(2, 8)

    def update(self, pontos):
        # Atualizando a posição do carro
        #Dependendo do número de pontos que o jogador faz sua velocidade aumenta
        if self.direcao == 'mao':
            self.rect.x += self.speedx - pontos * 2
        if self.direcao == 'contramao':
            self.rect.x += self.speedx + pontos * 2

        # Se o carro passar do final da tela, volta para posição inicial
        if self.rect.right < -20 and self.direcao == 'mao':
            self.rect.x = WIDTH + 100
        if self.rect.left > WIDTH + 20 and self.direcao == 'contramao':
            self.rect.x = -100