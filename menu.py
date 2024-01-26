from turtle import Screen
import pygame
import main_update


WIDTH, HEIGHT = 800, 600

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Função para desenhar o menu
def draw_menu():
    Screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Jogo da Velha", True, BLACK)
    main_update.gameDisplay.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

    start_text = font.render("Pressione 'S' para iniciar o jogo", True, BLACK)
    exit_text = font.render("Pressione 'Q' para sair", True, BLACK)

    main_update.gameDisplay.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    main_update.gameDisplay.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 50))

# Variável para controlar a tela atual
current_screen = "menu"