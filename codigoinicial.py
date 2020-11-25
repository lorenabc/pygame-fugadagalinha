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

class Carro(pygame.sprite.Sprite):
    def __init__(self, img, y, direcao):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.direcao = direcao
        if self.direcao == 'mao':
            self.rect.x = WIDTH + 100
            self.speedx = random.randint(-20, -8)
        if self.direcao == 'contramao':
            self.rect.x = -100
            self.speedx = random.randint(8, 20)

    def update(self):
        # Atualizando a posição do carro
        self.rect.x += self.speedx

        # Se o carro passar do final da tela, volta para trás
        if self.rect.right < -20 and self.direcao == 'mao':
            self.rect.x = WIDTH + 100
        if self.rect.left > WIDTH + 20 and self.direcao == 'contramao':
            self.rect.x = -100
            
def game_screen(window):
    assets = load_assets()

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    # Criando um grupo de carros
    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()

    # Criando o jogador
    player = Galinha(assets)
    all_sprites.add(player)

    # Criando os carros
    carros_img_mao = [assets['carro1_mao'], assets['carro2_mao'], assets['carro3_mao'], assets['carro4_mao']]
    carros_img_contramao = [assets['carro1_contramao'], assets['carro2_contramao'], assets['carro3_contramao'], assets['carro4_contramao']]
    posicoes_y = [53, 102, 155, 237, 285, 337]
    direcoes = ['mao', 'mao', 'mao', 'contramao', 'contramao', 'contramao']

    for i, direcao in enumerate(direcoes):
        cor = random.randint(0, 3)
        imagem = None
        if direcao == 'mao':
            imagem = carros_img_mao[cor]
        if direcao == 'contramao':
            imagem = carros_img_contramao[cor]
        carro = Carro(imagem, posicoes_y[i], direcao)
        all_sprites.add(carro)
        all_cars.add(carro)

    vidas = 3
    #estados do jogo
    ACABADO = 0
    JOGANDO = 1
    ACABANDO = 2
    state = JOGANDO

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != ACABADO:
        clock.tick(FPS)
        ponto = assets['font_pontos'].render(f'Pontos: {player.pontos}', True, (0, 255, 255))
        ponto_gameover = assets['font_pontos'].render(f'Pontos: {player.pontos}', True, (255, 0, 0))
        game_over = assets['font_gameover'].render('GAME OVER', True, (255, 0, 0))

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = ACABADO
            if state == JOGANDO:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_UP:
                        player.speedy -= 6
                    if event.key == pygame.K_DOWN:
                        player.speedy += 6
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_UP:
                        player.speedy += 6
                    if event.key == pygame.K_DOWN:
                        player.speedy -= 6