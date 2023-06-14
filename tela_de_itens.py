# import sys
# import pygame
#
# lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0),
#                   'branco': (255, 255, 255)}
# pygame.init()
#
# altura_tela = 700
# largura_tela = 1400
# tela = pygame.display.set_mode((largura_tela, altura_tela))
# pygame.display.set_caption('tela de itens do mercado mágico')
#
#
# quadrado_magico = pygame.image.load('imagens_gerais/quadrado_preto.jpg')
# posicao_x_quadrado_magico = 20
# posicao_y_quadrado_magico = 20
#
#
#
#
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     tela.fill(lista_de_cores['preto'])
#     for linha in range(0, 8):
#         for coluna in range(0, 8):
#             tela.blit(quadrado_magico, (posicao_x_quadrado_magico, posicao_y_quadrado_magico))
#             posicao_x_quadrado_magico += 100
#         posicao_x_quadrado_magico = 20
#         posicao_y_quadrado_magico += 100
#     posicao_x_quadrado_magico = 20
#     pygame.display.flip()
import sys
import pygame

lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0),
                  'branco': (255, 255, 255)}
pygame.init()

altura_tela = 700
largura_tela = 1400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tela de Itens do Mercado Mágico')


garrafa_de_agua = pygame.image.load('imagens_gerais/itens_do_mercado/garrafa_de_agua.png')
posicao_x_garrafa_de_agua = 30
posicao_y_garrafa_de_agua = 40

carregando_carne = pygame.image.load('imagens_gerais/itens_do_mercado/carne.png')
carne = pygame.transform.flip(carregando_carne, True, False)
posicao_x_carne = 210
posicao_y_carne = 30

pocao_de_vida = pygame.image.load('imagens_gerais/itens_do_mercado/pocao_de_vida.png')
posicao_x_pocao_de_vida = 370
posicao_y_pocao_de_vida = 30


quadrado_magico = pygame.image.load('imagens_gerais/quadrado_preto.jpg')
tamanho_quadrado = quadrado_magico.get_size()
posicao_x = 20
posicao_y = 100
espacamento = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(lista_de_cores['preto'])

    for linha in range(0, 8):
        for coluna in range(0, 8):
            tela.blit(quadrado_magico, (posicao_x, posicao_y))
            posicao_x += espacamento + tamanho_quadrado[0]
        posicao_x = 20
        posicao_y += espacamento + tamanho_quadrado[1]

    posicao_x = 20
    posicao_y = 20
    tela.blit(garrafa_de_agua, (posicao_x_garrafa_de_agua, posicao_y_garrafa_de_agua))
    tela.blit(carne, (posicao_x_carne, posicao_y_carne))
    tela.blit(pocao_de_vida, (posicao_x_pocao_de_vida, posicao_y_pocao_de_vida))
    pygame.display.flip()