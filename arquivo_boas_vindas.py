import time
import pygame
import sys
import arquivo_suporte
import tela_ashe_e_demogorgon
import tela_inicial

pygame.init()

# DICIONÁRIO COM CORES
lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0), 'branco': (255, 255, 255),
                  'verde_brilhante': (57, 255, 20)}

# CONFIGURAÇÃO DA TELA
altura = 1400
largura = 700
tela = pygame.display.set_mode((altura, largura))

# CRIANDO TITULO DA TELA
pygame.display.set_caption('TELA DE BOAS VINDAS')

# CARREGANDO CENÁRIO
cenario = pygame.image.load('imagens_gerais_cenário/cenario_floresta_seja_bem_vindo.jpg')

# INSERINDO SOM DA FLORESTA ENCANTADA
arquivo_suporte.sons.som_floresta_encantada(volume=1, ponto_stop=False)



# CRIANDO RETÂNGULO DO BOTÃO
botao_pos_x = altura // 2 - 100
botao_pos_y = largura // 2 + 100
largura_do_botao = 200
altura_do_botao = 50


# CONFIGURANDO A FONTE
font = pygame.font.Font(None, 50)
font.set_bold(True)
font.set_italic(True)
font.set_underline(True)
text_color = lista_de_cores['verde']

# CRIANDO VÁRIAVEL COM O TEXTO
texto = "SEJA BEM VINDO AO RPG"
texto_iniciar = "INICIAR JOGO"



clock = pygame.time.Clock()
tempo_inicial = time.time()

# CONFIGURAÇÃO DE TRANSIÇÃO DA TELA (OPACIDADE E VÁRIAVEL BOOLEANA)
opacidade_transicao = 255
velocidade_transicao = 5
trocar_tela = False
transicao_iniciada = False

# CONIGURANDO VÁRIAVEIS DE PERSONALIZAÇÃO DO TEXTO
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

def iniciar_segunda_tela(troca_de_tela=False, opacidade_transicao=0):
    arquivo_suporte.sons.som_floresta_encantada(ponto_stop=True)
    # tela_ashe_e_demogorgon.TELA_PRINCIPAL()
    tela_inicial.TELA_SECUNDARIA()





while True:
    for event in pygame.event.get():
        # CONDICIONANDO FECHAMENTO DA TELA
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # CONDICIONANDO TOQUE DO MOUSE NO BOTÃO INICIAR JOGO
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = pygame.mouse.get_pos()
            if retangulo_iniciar.collidepoint(posicao_mouse):
                iniciar_segunda_tela()
    # CONDIÇÕES DE PERSONALIZAÇÃO DE BRILHO DA MENSAGEM DE BEM VINDO
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultimo_piscar >= tempo_piscar:
        tempo_ultimo_piscar = tempo_atual
        brilho += brilho_incremento
        if brilho > brilho_maximo or brilho < brilho_minimo:
            brilho_incremento *= -1
            if brilho == brilho_minimo:
                brilho += brilho_incremento + 5

    # RENDERIZANDO SUPERFICIE DE TEXTO
    superficie_texto = font.render(texto, True, lista_de_cores['verde_escuro'])
    largura_texto, altura_texto = superficie_texto.get_size()


    # CRIANDO SUPERFICIE DE BRILHO
    superficie_brilho = pygame.Surface((largura_texto, altura_texto), pygame.SRCALPHA)
    superficie_brilho.fill((255, 255, 255, max(0, min(brilho, 255))))
    superficie_brilho.blit(superficie_texto, (0, 0))


    tela.fill((0, 0, 0))


    # DESENHANDO CENÁRIO
    tela.blit(cenario, (0, 0))

    # UTILIZANDO A FUNÇÃO DESENHANDO_TEXTO
    desenhando_texto(texto, altura // 2, largura // 2 - 200, text_color, lista_de_cores['verde_escuro'])

    # RENDERIZANDO O TEXTO INICIAR_JOGO
    texto_iniciar_tela = font.render(texto_iniciar, True, lista_de_cores['verde_brilhante'])

    # CRIANDO O RETANGULO DO TEXTO INICIAR_JOGO
    retangulo_iniciar = texto_iniciar_tela.get_rect()

    # DETERMINANDO AS DIREÇÕES DO TEXTO INICIAR_JOGO
    retangulo_iniciar.center = (botao_pos_x + largura_do_botao // 2 + 500, botao_pos_y + altura_do_botao // 2 + 180)

    # DESENHANDO O TEXTO RENDERIZADO COM O RETANGULO DO TEXTO
    tela.blit(texto_iniciar_tela, retangulo_iniciar)

    # DESENHANDO A SUPERFICIE DO TEXTO
    tela.blit(superficie_texto, (altura // 2 - 256, largura // 2 - 215))

    # DESENHANDO A SUPERFICIE DE BRILHO DO TEXTO
    tela.blit(superficie_brilho, (altura // 2 - 256, largura // 2 - 215))


    # CONFIGURAÇÃO DAS TRANSIÇÕES DA PRIMEIRA TELA
    tela_transicao = pygame.Surface((largura, altura))
    tela_transicao.fill(lista_de_cores["preto"])
    tela_transicao.set_alpha(opacidade_transicao)
    tela.blit(tela_transicao, (0, 0))

    # MUDANDO OPACIDADE DA TRANSIÇÃO
    opacidade_transicao -= velocidade_transicao
    if opacidade_transicao < 0:
        opacidade_transicao = 0

    # ATUALIZANDO
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)




