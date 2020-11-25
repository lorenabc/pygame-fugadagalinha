# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import time
from constantes import FPS, BRANCO, PRETO

#definindo a função da tela de transição
def transition_screen(window):
    #carregando as fontes e as frases a serem printadas na tela
    font = pygame.font.Font('assets/PressStart2P.ttf', 20)
    frase1 = font.render('A GALINHA FUGIU', False, BRANCO)
    frase2 = font.render('AJUDE ELA A ATRAVESSAR', False, BRANCO)
    frase3 = font.render('A RUA', False, BRANCO)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #variável para o looping principal
    game = True

    #looping principal
    while game:
        #Ajuste da velocidade
        clock.tick(FPS)

        #Verifica se o jogador quer fechar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        #Preenche a tela de preto e escreve as frases
        window.fill(PRETO)
        window.blit(frase1, (90, 50))
        window.blit(frase2, (25, 260))
        window.blit(frase3, (200, 300))

        #Mostra novo frame para o usuário
        pygame.display.update()

        #Espera 3 segundos
        time.sleep(3)

        #Sai da tela de transição
        return 2