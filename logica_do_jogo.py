import pygame
import main_update
#from turtle import Screen, screensize

# Definindo as configurações do jogo da velha

LARGURA, ALTURA = 500, 500
tamanho_quadrado = LARGURA // 3
cor_fundo = (255, 255, 255)
cor_linhas = (0, 0, 0)
jogador = "X"
tabuleiro = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    
# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(1, 3):
        pygame.draw.line(main_update.gameDisplay, cor_linhas, (0, linha * tamanho_quadrado), (LARGURA, linha * tamanho_quadrado), 2)
        pygame.draw.line(main_update.gameDisplay, cor_linhas, (linha * tamanho_quadrado, 0), (linha * tamanho_quadrado, ALTURA), 2)

# Função para desenhar os símbolos (X ou O) no tabuleiro
def desenhar_simbolos():
    fonte = pygame.font.SysFont(None, 100)

    for i in range(3):
        for j in range(3):
            texto = fonte.render(tabuleiro[i][j], True, cor_linhas)
            main_update.gameDisplay.blit(texto, (j * tamanho_quadrado + tamanho_quadrado // 4, i * tamanho_quadrado + tamanho_quadrado // 4))

# Função para verificar se alguém venceu o jogo
def verificar_vitoria():
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return True

# Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return True

    return False

# Função para verificar se o tabuleiro está cheio (empate)
def verificar_empate():
    for linha in tabuleiro:
        if "" in linha:
            return False
    return True