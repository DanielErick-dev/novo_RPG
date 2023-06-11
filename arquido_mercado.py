import sys
import pygame
import arquivo_suporte

pygame.init()

altura = 1400
largura = 700
tela = pygame.display.set_mode((altura, largura))
cenario= pygame.image.load('imagens_gerais_cenário/cenario_mercado.jpg')

carregando_imagem_do_comerciante = pygame.image.load('foto_personagens/velho.png')
comerciante = pygame.transform.flip(carregando_imagem_do_comerciante, True, False)

#livro_magico = pygame.image.load('imagens_gerais/')
posicao_x_comerciante = 280
posicao_y_comerciante = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.blit(cenario, (0, 0))
    tela.blit(comerciante, (posicao_x_comerciante, posicao_y_comerciante))
    pygame.display.flip()
    pygame.display.update()