import pygame
pygame.init()
def personagens():
    janela = pygame.display.set_mode((500, 600))
    janela_01 = pygame.display.set_mode((200, 300))
    fundo = pygame.image.load('ARQUEIRA_editado.jpg')
    fundo_01 = pygame.image.load('personagem.jpg')
    pygame.display.set_caption('personagem 02 Arfrid')
    position = (0, 0)
    janela_aberta = True
    while janela_aberta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
            janela.blit(fundo, dest=position)
            janela_01.blit(fundo_01, dest=position)
            pygame.display.update()
    pygame.quit()
personagens()