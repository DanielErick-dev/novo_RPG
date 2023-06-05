def TELA_SECUNDARIA():
    import arquivo_suporte
    import pygame
    import sys


    pygame.init()

    # DICIONÁRIO COM CORES
    lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0), 'branco': (255, 255, 255),
                      'verde_brilhante': (57, 255, 20)}

    # VÁRIAVEIS PARA TRANSIÇÃO
    opacidade_transicao = 355
    velocidade_transicao = 3.8

    # CONFIGURAÇÃO DA TELA
    altura = 1400
    largura = 700
    tela = pygame.display.set_mode((altura, largura))

    # CRIANDO TITULO DA TELA
    pygame.display.set_caption('Tela Inicial')

    # CARREGANDO CENÁRIO
    cenario = pygame.image.load('imagens_gerais_cenário/cenario_floresta_seja_bem_vindo.jpg')

    #  CARREGANDO IMAGEM TEMPORÁRIA
    foto_esquerda = pygame.image.load('foto_personagens/fada_da_selva.png')

    # CONFIGURAÇÕES IMAGEM DA SETA
    imagem_setinha = pygame.image.load('imagens_gerais/seta_verde.png')
    retangulo_da_seta = imagem_setinha.get_rect()
    posicao_x_setinha = 150
    posicao_y_setinha = 120

    # GIRANDO IMAGEM
    foto_personagem = pygame.transform.flip(foto_esquerda, True, False)

    # DEFININDO POSIÇÕES DA PERSONAGEM
    posicao_x_personagem = -30
    posicao_y_personagem = 10


    # CRIANDO RETÂNGULO DO BOTÃO
    botao_pos_x = altura // 2 - 100
    botao_pos_y = largura // 2 + 100
    largura_do_botao = 200
    altura_do_botao = 50


    # CONFIGURANDO A FONTE E POSIÇÕES DA FONTE
    font = pygame.font.Font(None, 25)
    font.set_bold(True)
    font.set_italic(True)
    x = 490
    y = 50

    # CRIANDO VÁRIAVEL FALA
    fala = ['eu me chamo feyre e serei sua companheira em sua caminhada e ajudarei em tudo que puder',
            'sua primeira missão será atravessar a floresta encantada, portanto vamos começar']
    contagem = -1

    def criando_texto():
        texto = font.render(fala[contagem], True,lista_de_cores['verde_brilhante'], lista_de_cores['preto'] )
        retangulo_do_texto = texto.get_rect()
        retangulo_do_texto.center = (x,y)
        tela.blit(texto, retangulo_do_texto)

    texto_ativo = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if retangulo_da_seta.collidepoint(posicao_mouse):
                    texto_ativo = True
                    contagem += 1
                    if contagem < len(arquivo_suporte.lista_de_falas):
                        arquivo_suporte.sons.frase_principal(arquivo_suporte.lista_de_falas[contagem])






        retangulo_da_seta.x = posicao_x_setinha
        retangulo_da_seta.y = posicao_y_setinha

        tela.fill((0, 0, 0))
        tela.blit(cenario, (0, 0))



        # INSERINDO SETINHA NA TELA
        tela.blit(imagem_setinha, (posicao_x_setinha, posicao_y_setinha))

        # INSERINDO PERSONAGEM NA TELA
        tela.blit(foto_personagem, (posicao_x_personagem, posicao_y_personagem))
        if texto_ativo and contagem < len(fala):
            criando_texto()


        tela_transicao = pygame.Surface((largura, altura))
        tela_transicao.fill(lista_de_cores["preto"])
        tela_transicao.set_alpha(opacidade_transicao)
        tela.blit(tela_transicao, (0, 0))

        opacidade_transicao -= velocidade_transicao
        if opacidade_transicao < 0:
            opacidade_transicao = 0
        pygame.display.update()
        pygame.display.flip()


