import pygame
pygame.init()
def demogorgon():
    janela = pygame.display.set_mode((700, 565))
    position = (0, 0)
    fundo = pygame.image.load('baueditado.jpg')
    pygame.display.set_caption('baú mágico')
    janela_aberta = True
    while janela_aberta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        janela.blit(fundo, dest=position)
        pygame.display.update()
    pygame.quit()

demogorgon()