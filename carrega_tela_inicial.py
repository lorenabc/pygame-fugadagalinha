# ==== Inicialização ====
# ----- Importa e inicia pacotes
import pygame
from assets import load_assets
from classes import GalinhaInicio
def init_screen(window):
    # ===== Loop principal =====
    tela_inicial = 0
    animacao = 1
    fim = 2
    state = tela_inicial
    assets = load_assets()

    pygame.mixer.music.load('assets/sons/background_inicial.wav')
    pygame.mixer.music.set_volume(0.4)

    background_inicio = assets['background_inicio']
    img_galinha = pygame.transform.scale(assets['galinha_img'], (35, 35))
    font_titulo = assets['font_inicio_titulo']
    font_texto = assets['font_inicio_texto']
    nome_jogo = font_titulo.render('FUGA DA GALINHA', False, (255, 255, 255))
    comando = font_texto.render('APERTE ENTER PARA COMEÇAR', False, (0, 0, 0))
    
    all_sprites = pygame.sprite.Group()
    galinha = GalinhaInicio(img_galinha)
    all_sprites.add(galinha)
