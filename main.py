# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from constantes import WIDTH, HEIGHT, QUIT, INICIO, TRANSICAO, JOGO
from carrega_tela_jogo import game_screen
from carrega_tela_inicial import init_screen
from transicao import transition_screen

#Incicializando o pygame e o mixer
pygame.init()
pygame.mixer.init()

#Estado incial do jogo
state = INICIO

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fuga da Galinha')

#Looping que altera entre as telas do jogo
while state != QUIT:
    if state == INICIO:
        state = init_screen(window)
    if state == TRANSICAO:
        state = transition_screen(window)
    if state == JOGO:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()