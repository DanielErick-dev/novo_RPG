# PRÓXIMAS MISSÕES:
    # FAZER UMA BREVE ANIMAÇÃO EXPLOSIVA AO TER O CONTATO ENTRE A BOLA DE FOGO E O ESCUDO DA ASHE
    # FAZER COM QUE O DEMOGORGON VOLTE AUTOMATICAMENTE DEPOIS DE 3 SEGUNDOS AO SER MORTO
    # CRIAR SOM DO DEMOGORGON JOGANDO A BOLA DE FOGO
    # CRIAR PEQUENO PAINEL DE AÇÕES
    # ENCONTRAR IMAGENS ONDE A ASHE ESTÁ COM A FLECHA APONTADA PARA FRENTE PARA INSERIR A TELA
    # INCREMENTAR OUTRAS IDEIAS DO JOGO
def TELA_PRINCIPAL():
    import pygame
    import sys


    # INICIALIZAÇÃO DO PYGAME
    pygame.init()

    # CONFIGURAÇÕES DA TELA
    largura = 1400
    altura = 700
    tela = pygame.display.set_mode((largura, altura))

    # DICIONÁRIO COM CORES EM RGB
    lista_de_cores = {'verde': (0, 100, 0), 'verde_escuro': (0, 39, 0), 'preto': (0, 0, 0), 'branco': (255, 255, 255)}

    mapa = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]


    # CONFIGURAÇÕES DO DEMOGORGON
    imagem_demogorgon = pygame.image.load('foto_personagens/demogorgon.png')
    demogorgon_retangulo = imagem_demogorgon.get_rect()
    posicao_x_demogorgon = 1000
    posicao_y_demogorgon = 500
    posicao_inicial_y_demogorgon = posicao_y_demogorgon
    posicao_inicial_x_demogorgon = posicao_x_demogorgon



    # CONFIGURAÇÕES DA PERSONAGEM ASHE
    imagem_personagem_ashe = pygame.image.load('foto_personagens/ASHE.png')
    personagem_ashe_retangulo = imagem_personagem_ashe.get_rect()
    posicao_x_ashe = 30
    posicao_y_ashe = 500
    posicao_inicial_x_ashe = 30
    posicao_inicial_y_ashe = 500
    posicao_da_ashe = [posicao_inicial_x_ashe, posicao_inicial_y_ashe]

    # VÁRIAVEIS PARA TRANSIÇÃO
    opacidade_transicao = 355
    velocidade_transicao = 3.8
    trocar_tela = False
    transicao_iniciada = False


    # CONFIGURAÇÕES DO PORTAL
    imagem_portal = pygame.image.load('imagens_gerais_cenário/portal_entrada.png')
    portal_retangulo = imagem_portal.get_rect()
    posicao_x_portal = 700
    posicao_y_portal = 450
    posicao_portal = ((posicao_x_portal, posicao_y_portal))


    # CONFIGURAÇÕES DA FLECHA DA ASHE
    imagem_da_flecha = pygame.image.load('imagens_gerais/Enxurrada_de_flechas.jpeg')
    flecha_retangulo = imagem_da_flecha.get_rect()
    posicao_x_flecha = posicao_x_ashe + 50
    posicao_y_flecha = posicao_y_ashe
    posicao_inicial_x_flecha = posicao_x_ashe + 50
    posicao_inicial_y_flecha = posicao_y_ashe


    # CONFIGURAÇÃO DA BOLA DE FOGO
    imagem_da_bola_de_fogo = pygame.image.load('imagens_gerais/bolao_de_fogo.png')
    bola_de_fogo_retangulo = imagem_da_bola_de_fogo.get_rect()
    posicao_x_bola_de_fogo = posicao_x_demogorgon - 20
    posicao_y_bola_de_fogo = posicao_y_demogorgon
    posicao_inicial_x_bola_de_fogo = posicao_x_demogorgon - 20
    posicao_inicial_y_bola_de_fogo = posicao_y_demogorgon


    # CONFIGURAÇÃO DO ESCUDO DA ASHE
    imagem_do_escudo = pygame.image.load('imagens_gerais/escudo.png')
    escudo_retangulo = imagem_do_escudo.get_rect()
    posicao_x_escudo = posicao_x_ashe + 70
    posicao_y_escudo = posicao_y_ashe
    posicao_inicial_x_escudo = posicao_x_ashe + 50
    posicao_inicial_y_escudo = posicao_y_ashe


    # CONFIGURAÇÕES DE VELOCIDADE DE MOVIMENTO
    velocidade_personagem_ashe = 4
    velocidade_da_flecha = 10
    velocidade_do_demogorgon = 2
    velocidade_da_bola_de_fogo = 4


    # CONFIGURAÇÕES DE CORES
    cor_branca = (255, 255, 255)
    cor_preta = (0, 0, 0)
    cor_verde = (0, 255, 0)
    cor_objeto = (0, 255, 0)
    cor_fundo = (0, 0, 0)
    cor_vermelha = (255, 0, 0)
    cor_cinza = (125, 125, 125)

    # VÁRIAVEIS DE CONTROLE BOOLEANA
    flecha_movendo = False
    demogorgon_atingido = False
    permanencia_do_escudo = False
    controle_da_letra_s = False
    controle_da_bola_de_fogo = False
    ashe_atingida = False
    ashe_vida = 100
    demogorgon_vida = 100
    ashe_fora_do_mapa = False


    # DEFININDO LIMITES DA TELA
    limite_superior = 0
    limite_inferior = altura - personagem_ashe_retangulo.height
    limite_esquerdo = 0
    limite_direito = 700


    tempo_sem_demogorgon = 0
    marcador_de_demogorgon = 0
    ultimo_tempo = 0

    # DETERMINANDO O CENÁRIO DE FUNDO DA TELA
    fundo_imagem = pygame.image.load('imagens_gerais_cenário/floresta.JPG')

    # DETERMINANDO FONTE E TAMANHO DA LETRA
    fonte = pygame.font.Font(None, 20)
    tamanho_objeto = 32

    # DETERMINANDO AS POSIÇÕES INICIAIS DA FLECHA GLOBALMENTE
    def determinando_posicoes_flecha():
        global posicao_x_flecha
        global posicao_y_flecha
        posicao_x_flecha = posicao_x_ashe + 50
        posicao_y_flecha = posicao_y_ashe

    def determinando_posicoes_escudo():
        global posicao_x_escudo
        global posicao_y_escudo
        posicao_x_escudo = posicao_x_ashe + 70
        posicao_y_escudo = posicao_y_ashe

    def determinando_posicoes_bola_de_fogo():
        global posicao_x_bola_de_fogo
        global posicao_y_bola_de_fogo
        posicao_x_bola_de_fogo = posicao_inicial_x_bola_de_fogo
        posicao_y_bola_de_fogo = posicao_inicial_y_bola_de_fogo



    def desenhar_mapa(mapa):
        pass
        # for linha in range(len(mapa)):
        #     for coluna in range(len(mapa[linha])):
        #         if mapa[coluna][linha] ==1:
        #             pygame.draw.rect(tela,cor_objeto,(coluna*tamanho_objeto, linha*tamanho_objeto, tamanho_objeto, tamanho_objeto))

    def desenhar_painel_vida_ashe(vida_ashe):
        # DEFINA AS DIMENSÕES E A POSIÇÃO DO PAINEL DE VIDA DA ASHE REPRESENTADO PELO RETANGULO VERMELHO NA TELA
        largura_vida_atual = vida_ashe
        altura_vida = 20
        x_vida_atual = 100
        y_vida = 110

        # DEFINA AS DIMENSÕES E A POSIÇÃO DO RETANGULO CINZA (VIDA PERDIDA)
        largura_vida_perdida = 100 - vida_ashe
        x_vida_perdida = x_vida_atual + largura_vida_atual


        # DESENHANDO O RETANGULO VERMELHO NA TELA (VIDA ATUAL)
        pygame.draw.rect(tela, (255, 0, 0), (x_vida_atual, y_vida, largura_vida_atual, altura_vida))
        pygame.draw.rect(tela, cor_preta, (x_vida_atual, y_vida, largura_vida_atual, altura_vida), 2)

        # DESENHANDO O RETANGULO CINZA (VIDA PERDIDA)
        pygame.draw.rect(tela, (128, 128, 128),(x_vida_perdida, y_vida, largura_vida_perdida, altura_vida))
        pygame.draw.rect(tela, cor_preta, (x_vida_atual, y_vida, largura_vida_atual, altura_vida), 2)

        # DESENHANDO O TEXTO
        texto = fonte.render(f"VIDA: {vida_ashe}%", True, cor_branca)

        # INSERINDO TEXTO NA TELA COM SUA DETERMINADA POSIÇÃO
        tela.blit(texto, (x_vida_atual + 10, y_vida - 16))

    def desenhar_painel_vida_demogorgon(vida_demogorgon):
        largura_vida_atual = vida_demogorgon
        altura_vida = 20
        x_vida_atual = 1000
        y_vida = 110

        # DEFINA AS DIMENSÕES E A POSIÇÃO DO RETANGULO CINZA (VIDA PERDIDA)
        largura_vida_perdida = 100 - vida_demogorgon
        x_vida_perdida = x_vida_atual + largura_vida_atual

        # DESENHANDO O RETANGULO PRETO NA TELA (VIDA ATUAL)
        pygame.draw.rect(tela, (cor_preta), (x_vida_atual, y_vida, largura_vida_atual, altura_vida))
        pygame.draw.rect(tela, cor_branca, (x_vida_atual, y_vida, largura_vida_atual, altura_vida), 2)

        # DESENHANDO O RETANGULO CINZA DA VIDA PERDIDA NA TELA (VIDA PERDIDA)
        pygame.draw.rect(tela, (125, 125, 125), (x_vida_perdida, y_vida, largura_vida_perdida, altura_vida))
        pygame.draw.rect(tela, (255,0 , 0), (x_vida_atual, y_vida, largura_vida_atual, altura_vida), 2)

        # DESENHANDO O TEXTO
        texto = fonte.render(f"VIDA: {vida_demogorgon}%", True, cor_branca)

        # INSERINDO TEXTO NA TELA
        tela.blit(texto, (x_vida_atual + 10, y_vida - 16))

    while True:
        desenhar_painel_vida_ashe(vida_ashe=ashe_vida)
        desenhar_painel_vida_demogorgon(vida_demogorgon=demogorgon_vida)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ashe_vida == 0:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    # CONDIÇÃO DE REAÇÃO PARA O TOQUE NO TECLADO NA LETRA "S"
                    permanencia_do_escudo = True
                    controle_da_letra_s = True

                    # ALINHANDO A POSIÇÃO DO ESCUDO JUNTO COM A ASHE
                    posicao_x_escudo = posicao_da_ashe[0] + 100
                    posicao_y_escudo = posicao_da_ashe[1]
                else:
                    controle_da_letra_s = False


                if event.key == pygame.K_u:
                    if ashe_fora_do_mapa:
                        pass
                    else:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load('vozes_ashe/especial_ashe.mp3')
                        pygame.mixer.music.play()
                        # CONDIÇÕES DE REAÇÕES PARA O TOQUE NO TECLADO "A"
                        flecha_movendo = True
                        # ALINHANDO A POSIÇÃO DA FLECHA JUNTAMENTE COM A POSIÇÃO DA PERSONAGEM
                        posicao_x_flecha = posicao_da_ashe[0] + 50
                        posicao_y_flecha = posicao_da_ashe[1]


                if event.key == pygame.K_r:
                    # UTILIZANDO LETRA R PARA RETOMADA DO DEMOGORGON A TELA
                    posicao_y_demogorgon = posicao_inicial_y_demogorgon
                    posicao_x_demogorgon = posicao_inicial_x_demogorgon
                if event.key == pygame.K_m:
                    # UTILIZANDO LETRA M PARA RETOMADA DO PERSONAGEM ASHE A TELA
                    if ashe_fora_do_mapa is True:
                        posicao_da_ashe[0] = posicao_inicial_x_ashe
                        posicao_da_ashe[1] = posicao_inicial_y_ashe
                        ashe_atingida = False
                        ashe_fora_do_mapa = False

                if event.key == pygame.K_t:
                    controle_da_bola_de_fogo = True
                    posicao_x_bola_de_fogo = posicao_x_demogorgon - 20
                    posicao_y_bola_de_fogo = posicao_y_demogorgon

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    controle_da_letra_s = False



        # FAZENDO A MOVIMENTAÇÃO LESTE E OESTE DO PERSONAGEM
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_a]:
            if posicao_da_ashe[0] > limite_esquerdo:
                if controle_da_letra_s:
                    pass
                else:
                    posicao_da_ashe[0] -= velocidade_personagem_ashe
        if teclas_pressionadas[pygame.K_d]:
            if posicao_da_ashe[0] < 1150:
                if controle_da_letra_s:
                    pass
                else:
                    posicao_da_ashe[0] += velocidade_personagem_ashe
        # if teclas_pressionadas[pygame.K_DOWN]:
        #     posicao_da_ashe[1] += velocidade_personagem_ashe
        # if teclas_pressionadas[pygame.K_UP]:
        #     posicao_da_ashe[1] -= velocidade_personagem_ashe



        # REALIZANDO A MOVIMENTAÇÃO DA FLECHA E ATUALIZANDO RETANGULO DA FLECHA
        if flecha_movendo:
            posicao_x_flecha += velocidade_da_flecha
            flecha_retangulo.topleft = (posicao_x_flecha, posicao_y_flecha)


            # CONDICIONANDO A COLISÃO DA FLECHA COM O DEMOGORGON
            if flecha_retangulo.colliderect(demogorgon_retangulo):
                demogorgon_vida -= 20
                demogorgon_atingido = True
                posicao_y_demogorgon = -1000
                posicao_x_demogorgon = -1000
                flecha_movendo = False
        if demogorgon_atingido:
            marcador_de_demogorgon = 1
            demogorgon_atingido = False
        if not demogorgon_atingido:
            if marcador_de_demogorgon == 2:
                posicao_x_demogorgon = posicao_inicial_x_demogorgon
                posicao_y_demogorgon = posicao_inicial_y_demogorgon
                marcador_de_demogorgon = 0
            else:
                tempo_sem_demogorgon += pygame.time.get_ticks() - ultimo_tempo

        # CRIANDO O RETANGULO DO ESCUDO
        if controle_da_letra_s:
            escudo_retangulo.topleft = (posicao_x_escudo, posicao_y_escudo)
        if not controle_da_letra_s:
            escudo_retangulo.move_ip(-1000, -1000)

        # CRIANDO O RETANGULO DA BOLA DE FOGO
        if controle_da_bola_de_fogo:
            posicao_x_bola_de_fogo -= velocidade_da_bola_de_fogo
            bola_de_fogo_retangulo.topleft = (posicao_x_bola_de_fogo, posicao_y_bola_de_fogo)




            # CONDICIONANDO A COLISÃO DA BOLA DE FOGO COM O ESCUDO DA ASHE
            if bola_de_fogo_retangulo.colliderect(escudo_retangulo):
                ashe_atingida = False
                posicao_x_bola_de_fogo = -1000
                posicao_y_bola_de_fogo = -1000
            else:
                # CONDICIONANDO A COLISÃO DA BOLA DE FOGO COM A ASHE
                if bola_de_fogo_retangulo.colliderect(personagem_ashe_retangulo):
                    ashe_vida -= 20
                    ashe_atingida = True
                    ashe_fora_do_mapa = True
                    # posicao_x_ashe = -1000
                    # posicao_y_ashe = -1000
                    posicao_da_ashe[0] = -1000
                    posicao_da_ashe[1] = -1000
                    controle_da_bola_de_fogo = False

        # DEFININDO POSIÇÕES INICIAIS DA FLECHA SE A FLECHA NÃO ESTIVER MAIS EM MOVIMENTO
        if not flecha_movendo:
            posicao_x_flecha = posicao_da_ashe[0] + 50
            posicao_y_flecha = posicao_da_ashe[1]
            flecha_retangulo.topleft = (posicao_x_flecha, posicao_y_flecha)



        # ATUALIZANDO RETANGULO DO DEMOGORGON
        demogorgon_retangulo.topleft = (posicao_x_demogorgon, posicao_y_demogorgon)


        # ATUALIZANDO RETANGULO DA ASHE
        personagem_ashe_retangulo.topleft = (posicao_x_ashe, posicao_y_ashe)

        # ATUALIZANDO RETANGULO DO ESCUDO
        escudo_retangulo.topleft = (posicao_x_escudo, posicao_y_escudo)


        # INSERINDO NA TELA TODAS AS IMAGENS NECESSÁRIAS
        tela.blit(fundo_imagem, (0, 0))
        if not ashe_atingida:
            tela.blit(imagem_personagem_ashe, posicao_da_ashe)


        #tela.blit(imagem_portal, posicao_portal)
        tela.blit(imagem_demogorgon, (posicao_x_demogorgon, posicao_y_demogorgon))


        # INSERINDO FLECHA NA TELA SE ELA ESTIVER EM MOVIMENTO
        if flecha_movendo:
            if ashe_fora_do_mapa:
                pass
            else:
                tela.blit(imagem_da_flecha, (posicao_x_flecha, posicao_y_flecha))


        # INSERINDO ESCUDO DA ASHE NA TELA SE A TECLA "S" ESTIVER SENDO PRESSIONADA
        if controle_da_letra_s:
            tela.blit(imagem_do_escudo, (posicao_x_escudo, posicao_y_escudo))

        # INSERINDO BOLA DE FOGO DO DEMOGORGON NA TELA A DEPENDER DA VÁRIAVEL BOOLEANA
        if controle_da_bola_de_fogo:
            tela.blit(imagem_da_bola_de_fogo, (posicao_x_bola_de_fogo, posicao_y_bola_de_fogo))

        desenhar_painel_vida_ashe(vida_ashe=ashe_vida)
        desenhar_painel_vida_demogorgon(vida_demogorgon=demogorgon_vida)

        #
        tela_transicao = pygame.Surface((largura, altura))
        tela_transicao.fill(lista_de_cores["preto"])
        tela_transicao.set_alpha(opacidade_transicao)
        tela.blit(tela_transicao, (0, 0))

        opacidade_transicao -= velocidade_transicao
        if opacidade_transicao < 0:
            opacidade_transicao = 0
        # ATUALIZANDO
        pygame.display.update()
        pygame.display.flip()

        ultimo_tempo = pygame.time.get_ticks()


TELA_PRINCIPAL()




