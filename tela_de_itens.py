import sys
import pygame

lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0),
                  'branco': (255, 255, 255)}
pygame.init()

altura_tela = 700
largura_tela = 1400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('tela de itens do mercado mágico')


circulo_magico = pygame.image.load('imagens_gerais/circulo_magico.png')
posicao_x_circulo_magico = 20
posicao_y_circulo_magico = 20

posicao_xq = 100
posicao_yq = 100
altura_quadrado = 100
largura_quadrado = 100



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(lista_de_cores['preto'])
    # tela.blit(circulo_magico, (posicao_x_circulo_magico, posicao_y_circulo_magico))
    for _ in range(0, 8):
        pygame.draw.rect(tela, lista_de_cores['verde'], pygame.Rect(posicao_xq, posicao_yq, altura_quadrado, largura_quadrado))
        posicao_xq += largura_quadrado + 10
        if posicao_xq + largura_quadrado > largura_tela:
            posicao_xq = 100
            posicao_yq += altura_quadrado + 10
    posicao_xq = 100
    posicao_yq = 100
    pygame.display.flip()
