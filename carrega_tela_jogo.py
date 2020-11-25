# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from assets import load_assets
from classes import GalinhaPlayer, Carro
from constantes import HEIGHT, JOGANDO, ACABANDO, ACABADO, INICIANDO, FPS, AMARELO_CLARO, BORDO, PRETO

#Criando uma função que gera a tela do jogo
def game_screen(window):
    #carrega os assets utilizando a função load_assets
    assets = load_assets()

    #estado inicial
    state = INICIANDO

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #carregando a música do jogo
    pygame.mixer.music.load('assets/sons/background.ogg')
    pygame.mixer.music.set_volume(0.4)

    # ===== Loop principal =====
    while state != ACABADO:
        if state == INICIANDO:
            pygame.mixer.music.play(loops=-1)
            # Criando um grupo de carros
            all_sprites = pygame.sprite.Group()
            all_cars = pygame.sprite.Group()

            # Criando o jogador
            player = GalinhaPlayer(assets)
            all_sprites.add(player)

            # Criando os carros
            #imgs dos carros
            carros_img_mao = [assets['carro1_mao'], assets['carro2_mao'], assets['carro3_mao'], assets['carro4_mao']]
            carros_img_contramao = [assets['carro1_contramao'], assets['carro2_contramao'], assets['carro3_contramao'],
                                    assets['carro4_contramao']]

            #posições em y que coloca os carros nas 6 faixas
            posicoes_y = [53, 102, 155, 237, 285, 337]

            #lista de direções dos carros
            direcoes = ['mao', 'mao', 'mao', 'contramao', 'contramao', 'contramao']

            #for que cria os carros
            for i, direcao in enumerate(direcoes):
                #randomiza a cor do carro
                cor = random.randint(0, 3)
                imagem = None
                if direcao == 'mao':
                    imagem = carros_img_mao[cor]
                if direcao == 'contramao':
                    imagem = carros_img_contramao[cor]
                carro = Carro(imagem, posicoes_y[i], direcao)
                all_sprites.add(carro)
                all_cars.add(carro)