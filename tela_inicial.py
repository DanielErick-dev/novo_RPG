import arquivo_suporte
from arquivo_suporte import sons
import pygame
import sys


pygame.init()

# DICIONÁRIO COM CORES
lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0), 'branco': (255, 255, 255),
                  'verde_brilhante': (57, 255, 20)}

# CONFIGURAÇÃO DA TELA
altura = 1400
largura = 700
tela = pygame.display.set_mode((altura, largura))

# CRIANDO TITULO DA TELA
pygame.display.set_caption('Tela Inicial')

# CARREGANDO CENÁRIO
cenario = pygame.image.load('imagens_gerais_cenário/cenario_floresta_seja_bem_vindo.jpg')

foto_esquerda = pygame.image.load('foto_personagens/fada_da_selva.png')

foto_personagem = pygame.transform.flip(foto_esquerda, True, False)
posicao_x_personagem = -30
posicao_y_personagem = 10


# CRIANDO RETÂNGULO DO BOTÃO
botao_pos_x = altura // 2 - 100
botao_pos_y = largura // 2 + 100
largura_do_botao = 200
altura_do_botao = 50


# CONFIGURANDO A FONTE
font = pygame.font.Font(None, 25)
font.set_bold(True)
font.set_italic(True)
# font.set_underline(True)



x = 490
y = 50
fala = 'Bem Vindo A Floresta Encantada, Aqui Começa Sua Primeira Jornada'


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto = font.render(fala, True, lista_de_cores['verde_brilhante'], lista_de_cores['preto'])
    retangulo_do_texto = texto.get_rect()
    retangulo_do_texto.center = (x,y)



    tela.fill((0, 0, 0))
    tela.blit(cenario, (0, 0))

    tela.blit(texto, retangulo_do_texto)

    tela.blit(foto_personagem, (posicao_x_personagem, posicao_y_personagem))
    arquivo_suporte.sons.frase_principal()
    pygame.display.update()
    pygame.display.flip()

