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
posicao_x_comerciante = 280
posicao_y_comerciante = 240


carregando_imagem_ichigo = pygame.image.load('foto_personagens/ichigo.png')
imagem_ichigo = pygame.transform.flip(carregando_imagem_ichigo, True, False)
posicao_x_personagem = 1150
posicao_y_personagem = 220



carregando_caixa_magica = pygame.image.load('imagens_gerais/caixa.png')
caixa_magica = pygame.transform.flip(carregando_caixa_magica, True, False)
posicao_x_caixa = 430
posicao_y_caixa = 228



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.blit(cenario, (0, 0))
    tela.blit(comerciante, (posicao_x_comerciante, posicao_y_comerciante))
    tela.blit(imagem_ichigo, (posicao_x_personagem, posicao_y_personagem))
    tela.blit(caixa_magica, (posicao_x_caixa, posicao_y_caixa))
    pygame.display.flip()
    pygame.display.update()