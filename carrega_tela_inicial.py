# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from assets import load_assets
from classes import GalinhaInicio
from constantes import TELA_INICIAL, ANIMACAO, FIM, FPS, BRANCO, PRETO


#Define a função que carrega a tela inicial
def init_screen(window):
    #Define o primeiro estado da tela inicial
    state = TELA_INICIAL

    #Carrega os assets
    assets = load_assets()

    #Carrega a música da tela inicial
    pygame.mixer.music.load('assets/sons/background_inicial.wav')
    pygame.mixer.music.set_volume(0.4)

    #Transforma os assets em variaveis e define os textos que vão ser imprimidos na tela
    background_inicio = assets['background_inicio']
    img_galinha = pygame.transform.scale(assets['galinha_img'], (35, 35))
    font_titulo = assets['font_inicio_titulo']
    font_texto = assets['font_inicio_texto']
    nome_jogo = font_titulo.render('FUGA DA GALINHA', False, BRANCO)
    comando = font_texto.render('APERTE ENTER PARA COMEÇAR', False, PRETO)

    #Cria um objeto da galinha inicial e adiciona a um grupo
    all_sprites = pygame.sprite.Group()
    galinha = GalinhaInicio(img_galinha)
    all_sprites.add(galinha)

    #Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #Loop inicial
    pygame.mixer.music.play(loops=-1)
    while state != FIM:
        # Ajusta a velocidade para o número de FPS
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if state == TELA_INICIAL:
                if event.type == pygame.KEYDOWN:
                    #Se o jogador apertar espaço inicia a animação da galinha
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        assets['som_start'].play()
                        state = ANIMACAO


        # ----- Gera saídas

        #Preenche a tela com o background
        window.fill(PRETO)
        window.blit(background_inicio, (0, 0))
        if state == TELA_INICIAL:
            window.blit(nome_jogo, (90, 50))
            window.blit(comando, (58, 260))

        #Se a animação estiver ocorrendo atualiza a posição da sprite
        if state == ANIMACAO:
            all_sprites.update()

        #Se a galinha passou do fim da tela sai da tela inicial
        if galinha.y > 420:
            state = 1
            return state

        #Desenha a sprite na tela
        all_sprites.draw(window)

        # Mostra o novo frame para o jogador
        pygame.display.update()