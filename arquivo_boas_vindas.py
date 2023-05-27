import pygame
import sys


pygame.init()

# DICIONÁRIO COM CORES
lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0)}

# CONFIGURAÇÃO DA TELA
altura = 1400
largura = 700
tela = pygame.display.set_mode((altura, largura))

# CARREGANDO CENÁRIO
cenario = pygame.image.load('imagens_gerais_cenário/cenario_floresta_seja_bem_vindo.jpg')


# CONFIGURANDO A FONTE
font = pygame.font.Font(None, 50)
font.set_bold(True)
font.set_italic(True)
font.set_underline(True)
text_color = lista_de_cores['verde']

texto = "SEJA BEM VINDO AO RPG"
clock = pygame.time.Clock()

brilho= 0
brilho_incremento= 5
brilho_minimo= 0
brilho_maximo= 255
tempo_piscar = 500
tempo_ultimo_piscar = pygame.time.get_ticks()
def desenhando_texto(text, x, y, cor, cor_de_fundo):
    # RENDERIZANDO O TEXTO
    texto = font.render(text, True, cor, cor_de_fundo)

    # CRIANDO O RETANGULO DO TEXTO
    retangulo_do_texto = texto.get_rect()

    # CENTRALIZANDO O RETANGULO
    retangulo_do_texto.center = (x, y)

    # DESENHANDO RETANGULO NA TELA
    tela.blit(texto, retangulo_do_texto)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultimo_piscar >= tempo_piscar:
        tempo_ultimo_piscar = tempo_atual
        brilho += brilho_incremento
        if brilho > brilho_maximo or brilho < brilho_minimo:
            brilho_incremento *= -1
            if brilho == brilho_minimo:
                brilho += brilho_incremento + 5


    superficie_texto = font.render(texto, True, lista_de_cores['verde_escuro'])
    largura_texto, altura_texto = superficie_texto.get_size()


    superficie_brilho = pygame.Surface((largura_texto, altura_texto), pygame.SRCALPHA)
    superficie_brilho.fill((255, 255, 255, max(0, min(brilho, 255))))
    superficie_brilho.blit(superficie_texto, (0, 0))

    tela.fill((0, 0, 0))

    tela.blit(cenario, (0, 0))

    desenhando_texto(texto, altura // 2, largura // 2 - 200, text_color, lista_de_cores['verde_escuro'])

    tela.blit(superficie_texto, (altura // 2 - 256, largura // 2 - 215))

    tela.blit(superficie_brilho, (altura // 2 - 256, largura // 2 - 215))


    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)




