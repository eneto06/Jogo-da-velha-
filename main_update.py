import sys

import pygame
import menu
import logica_do_jogo
pygame.init()


# Configurações da tela

gameDisplay = pygame.display.set_mode((menu.WIDTH, menu.HEIGHT))
pygame.display.set_caption("Jogo da velha com pygame")

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            coluna = mouseX // logica_do_jogo.tamanho_quadrado
            linha = mouseY // logica_do_jogo.tamanho_quadrado

            if logica_do_jogo.tabuleiro[linha][coluna] == "":
                logica_do_jogo.tabuleiro[linha][coluna] = jogador

                if logica_do_jogo.verificar_vitoria():
                    print(f"O jogador {jogador} venceu!")
                    pygame.quit()
                    sys.exit()
                elif logica_do_jogo.verificar_empate():
                    print("Empate!")
                    pygame.quit()
                    sys.exit()

                jogador = "O" if jogador == "X" else "X"

    gameDisplay.fill(menu.WHITE)
    menu.draw_menu()
    logica_do_jogo.desenhar_tabuleiro()
    logica_do_jogo.desenhar_simbolos()

    pygame.display.flip()