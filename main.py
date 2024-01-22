import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('JOGO DA VELHA')


black = (0, 0 ,0)
white = (255, 255, 255)

jogoDaVelhaImg = pygame.image.load()

clock = pygame.time.Clock()
crashed = False

def jogo_da_velha(x, y):
    gameDisplay.blit(jogoDaVelhaImg, (x, y))

x =  (display_width * 0.30)
y = (display_height * 0.10)
    

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    gameDisplay.fill(white)
    jogo_da_velha(x,y)
            

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()