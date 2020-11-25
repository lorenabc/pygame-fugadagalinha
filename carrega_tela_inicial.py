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
    
    clock = pygame.time.Clock()
    FPS = 30

    pygame.mixer.music.play(loops=-1)
    while state != fim:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1, 0
            if state == tela_inicial:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        assets['som_start'].play()
                        state = animacao


        # ----- Gera saídas
        window.fill((0, 0, 0))
        window.blit(background_inicio, (0, 0))
        if state == tela_inicial:
            window.blit(nome_jogo, (90, 50))
            window.blit(comando, (58, 260))
        if state == animacao:
            all_sprites.update()
        if galinha.y > 420:
            state = 1
            return state

        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pygame.display.update()
