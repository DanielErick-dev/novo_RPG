# PRÓXIMAS MISSÕES:
    # FAZER COM QUE O DEMOGORGON VOLTE AUTOMATICAMENTE DEPOIS DE 3 SEGUNDOS AO SER MORTO
    # CRIAR SOM DO DEMOGORGON JOGANDO A BOLA DE FOGO
    # CRIAR PEQUENO PAINEL DE AÇÕES

from playsound import playsound
import pygame
from time import sleep
import tkinter as tk
from PIL import Image, ImageTk
import sys
from PIL import Image


# imagem_original = Image.open('foto_personagens/ASHE.png')
# nova_largura = 180
# nova_altura = 180
# imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura))
# imagem_redimensionada.save('imagens_gerais_cenário/ASHE.png')



# INICIALIZAÇÃO DO PYGAME
pygame.init()

# CONFIGURAÇÕES DA TELA
largura = 1300
altura = 700
tela = pygame.display.set_mode((largura, altura))


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



# CONFIGURAÇÕES DO PERSONAGEM ASHE
imagem_personagem_ashe = pygame.image.load('foto_personagens/ASHE.png')
personagem_ashe_retangulo = imagem_personagem_ashe.get_rect()
posicao_x_ashe = 30
posicao_y_ashe = 500
posicao_inicial_x_ashe = 30
posicao_inicial_y_ashe = 500
posicao_da_ashe = [posicao_inicial_x_ashe, posicao_inicial_y_ashe]




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
velocidade_personagem_ashe = 2
velocidade_da_flecha = 6
velocidade_do_demogorgon = 2
velocidade_da_bola_de_fogo = 4


# CONFIGURAÇÕES DE CORES
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_verde = (0, 255, 0)
cor_objeto = (0, 255, 0)
cor_fundo = (0, 0, 0)

# VÁRIAVEIS DE CONTROLE BOOLEANA
flecha_movendo = False
demogorgon_atingido = False
permanencia_do_escudo = False
controle_da_letra_s = False
controle_da_bola_de_fogo = False
ashe_atingida = False



limite_superior = 0
limite_inferior = altura - personagem_ashe_retangulo.height
limite_esquerdo = 0
limite_direito = 700
tempo_sem_demogorgon = 0
marcador_de_demogorgon = 0
ultimo_tempo = 0

# DETERMINANDO O CENÁRIO DE FUNDO DA TELA
fundo_imagem = pygame.image.load('imagens_gerais_cenário/FLORESTA.JPG')
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

def desenhar_painel_vida(vida_ashe):
    # DEFINA AS DIMENSÕES E A POSIÇÃO DO PAINEL DE VIDA DA ASHE REPRESENTADO PELO RETANGULO VERMELHO NA TELA
    largura_vida_atual = vida_ashe
    altura_vida = 10
    x_vida_atual = 10
    y_vida = 10

    # DEFINA AS DIMENSÕES E A POSIÇÃO DO RETANGULO CINZA (VIDA PERDIDA)
    largura_vida_perdida = 100 - vida_ashe
    x_vida_perdida = x_vida_atual + largura_vida_atual


    # DESENHANDO O RETANGULO VERMELHO NA TELA (VIDA ATUAL)
    pygame.draw.rect(tela, (255, 0, 0), (x_vida_atual, y_vida, largura_vida_atual, altura_vida))

    # DESENHANDO O RETANGULO CINZA (VIDA PERDIDA)
    pygame.draw.rect(tela, (128, 128, 128),(x_vida_perdida, y_vida, largura_vida_perdida, altura_vida))

while True:
    for event in pygame.event.get():
        # CONDIÇÃO DE ENCERRAMENTO DA TELA
        if ashe_atingida is True:
            sleep(3)
            pygame.quit()
            sys.exit()
        if event.type == pygame.QUIT:
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


            if event.key == pygame.K_u:
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


            if event.key == pygame.K_t:
                controle_da_bola_de_fogo = True
                posicao_x_bola_de_fogo = posicao_x_demogorgon - 20
                posicao_y_bola_de_fogo = posicao_y_demogorgon

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                controle_da_letra_s = False


    # FAZENDO A MOVIMENTAÇÃO LESTE, OESTE NORTE E SUL DO PERSONAGEM
    teclas_pressionadas = pygame.key.get_pressed()
    if teclas_pressionadas[pygame.K_a]:
        if posicao_da_ashe[0] > limite_esquerdo:
            posicao_da_ashe[0] -= velocidade_personagem_ashe
    if teclas_pressionadas[pygame.K_d]:
        if posicao_da_ashe[0] < 1150:
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
                ashe_atingida = True
                posicao_x_ashe = -1000
                posicao_y_ashe = -1000
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
        tela.blit(imagem_da_flecha, (posicao_x_flecha, posicao_y_flecha))


    # INSERINDO ESCUDO DA ASHE NA TELA SE A TECLA "S" ESTIVER SENDO PRESSIONADA
    if controle_da_letra_s:
        tela.blit(imagem_do_escudo, (posicao_x_escudo, posicao_y_escudo))

    # INSERINDO BOLA DE FOGO DO DEMOGORGON NA TELA A DEPENDER DA VÁRIAVEL BOOLEANA
    if controle_da_bola_de_fogo:
        tela.blit(imagem_da_bola_de_fogo, (posicao_x_bola_de_fogo, posicao_y_bola_de_fogo))


    # ATUALIZANDO
    pygame.display.update()
    pygame.display.flip()

    ultimo_tempo = pygame.time.get_ticks()

















class Sons:

    # SOM GERAL de Personagem
    def sons_gerais(self, nome=None):
        pygame.init()
        pygame.mixer.init()
        som = pygame.mixer.Sound(nome)
        som.play()


    # SONS DE ASHE:
    def som_ashe_comeco_do_jogo(self):
        sons.sons_gerais('vozes_ashe/ashe_começo.mp3')
    def som_ashe_final_de_partida(self):
        sons.sons_gerais('vozes_ashe/ashe_final.mp3')
    def som_ashe_atacando(self, volume=0):
        sons.sons_gerais('vozes_ashe/especial_ashe.mp3')




    # SONS DE ANDREY:
    def som_andrey_começo_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_começo.mp3')
    def som_andrey_meio_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_meio.mp3')
    def som_andrey_final_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_final.mp3')

    # SONS DEMOGORGONS:
    def som_demogorgon_atacando(self):
        sons.sons_gerais('vozes_demogorgon/demogorgon_atacando.mp3')

    def som_demogorgon_aparecendo(self):
        sons.sons_gerais('vozes_demogorgon/som_demogorgon_aparecendo.mp3')

    # SONS DE VIEGO:
    def som_viego_comeco_de_partida(self):
        sons.sons_gerais('vozes_viego/viego_começo.mp3')
    def som_viego_meio_de_partida(self):
        sons.sons_gerais('vozes_viego/viego_meio.mp3')
    def som_viego_final(self):
        sons.sons_gerais('vozes_viego/viego_final.mp3')

    # SONS ALEATÓRIOS
    def som_geral_de_trilha_sonora(self,ponto_stop=False, volume=1, nome=None):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        musica_a_ser_tocada = pygame.mixer.music.load(nome)
        pygame.mixer.music.play()




    def som_armadura_quebrando(self):
        sons.sons_gerais('sons_gerais/')
    def som_equipando_armadura(self):
        sons.sons_gerais('sons_gerais/som_equipando_armadura.mp3')
    def som_de_comer(self):
        sons.sons_gerais('sons_gerais/som_comendo.mp3')

    def som_de_beber(self):
        sons.sons_gerais('sons_gerais/som_bebendo_agua.mp3')

    def som_de_portal(self):
        pass
        #sons.sons_gerais('sons_gerais/')

    def tomando_pocao(self):
        sons.sons_gerais('sons_gerais/som_tomando_pocao.mp3')

    def som_game_over(self):
        sons.sons_gerais('sons_gerais/som_game_over.mp3')

    def som_abrindo_bau(self):
        sons.sons_gerais('sons_gerais/som_abrindo_bau.mp3')

    def som_regenerando_armadura(self):
        sons.sons_gerais('sons_gerais/som_regenerando_armadura.mp3')



    def som_floresta_encantada(self, volume=1):
        sons.som_geral_de_trilha_sonora(volume=1, nome='sons_gerais_cenário/som_floresta.mp3', ponto_stop=False)

    def som_floresta_invertida(self, volume=1):
        sons.som_geral_de_trilha_sonora(volume=1, nome='sons_gerais_cenário/som_floresta_invertida.mp3', ponto_stop=True)
    def som_caverna(self, volume=0.8):
        pass
    def som_flecha_sendo_lancada(self):
        pass


    def som_floresta_de_neve(self, volume=1):
        pass




sons = Sons()














class Mapas():
    def amostra_geral_na_tela(self, primeiro_valor, segundo_valor, diretorio_da_imagem, nome_do_mapa, mensagem=None):
        janela = pygame.display.set_mode((primeiro_valor, segundo_valor))
        fundo = pygame.image.load(diretorio_da_imagem)
        pygame.display.set_caption(nome_do_mapa)
        contador_de_janela = 0
        position = (0, 0)
        janela_aberta = True
        while janela_aberta:
            contador_de_janela += 1
            sleep(1)
            janela.blit(fundo, dest=position)
            pygame.display.update()
            if contador_de_janela == 4:
                pygame.quit()
                break
            janela.blit(fundo, dest=position)
            pygame.display.update()
        pygame.quit()
        print(mensagem)
    def mostrando_floresta_encantada(self):
        daniel.amostra_geral_na_tela(primeiro_valor=1400,
                                     segundo_valor=540,
                                     diretorio_da_imagem='imagens_gerais_cenário/floresta_encantada.jpg',
                                     nome_do_mapa='Floresta Encantada',
                                     mensagem=f'\033[32m \033[1m {"SIGA EM FRENTE, ATRAVESSE AS ÁRVORES":^100} \033[m')



    def mostrando_floresta_de_neve(self):
        daniel.amostra_geral_na_tela(primeiro_valor=1300,
                                     segundo_valor=700,
                                     diretorio_da_imagem='floresta_de_neve_editado.png',
                                     nome_do_mapa='Floresta de Neve',
                                     mensagem=f'\033[1m \033[4m \033[36m {"se prepare pra floresta de neve".upper():^100} \033[m')


    def mostrando_floresta_invertida(self):
        daniel.amostra_geral_na_tela(primeiro_valor=1672,
                                     segundo_valor=700,
                                     diretorio_da_imagem='imagens_gerais_cenário/floresta_invertida.jpg',
                                     nome_do_mapa='Floresta Invertida',
                                     mensagem=f'\033[1m \033[4m \033[35m {"siga seu caminho entre as àrvores da floresta invertida".upper():^100} \033[m')



    def mostrando_caverna(self):
        daniel.amostra_geral_na_tela(primeiro_valor=1200,
                                     segundo_valor=675,
                                     diretorio_da_imagem='imagens_gerais_cenário/floresta_de_neve.png',
                                     nome_do_mapa='Caverna Mágica',
                                     mensagem=f'\033[1m \033[4m \033[32m {"suba as escadas e entre na caverna mágica".upper():^100} \033[m')
    def mostrando_demogorgon(self):
        global gif, contador, label, reiniciar_btn
        root = tk.Tk()

        def atualizar_gif():
            global gif, contador, label
            try:
                frame = gif.tell()
                gif.seek(frame + 1)
                img = ImageTk.PhotoImage(gif.convert("RGBA"))
                label.config(image=img)
                label.image = img
                contador.set(contador.get() + 1)
                root.after(50, atualizar_gif)
            except EOFError:
                # exibe a última imagem do GIF
                img = ImageTk.PhotoImage(gif.convert("RGBA"))
                label.config(image=img)
                label.image = img
                reiniciar_btn.config(state=tk.NORMAL)
            except AttributeError as e:
                print("Erro ao abrir o arquivo de gif:", e)

        def reiniciar_gif():
            global gif, contador
            # retorna ao primeiro frame do GIF e reinicia o loop
            gif.seek(0)
            contador.set(0)
            reiniciar_btn.config(state=tk.DISABLED)
            atualizar_gif()

        contador = tk.IntVar()
        try:
            gif = Image.open("foto_personagens/demogorgon.gif")
        except FileNotFoundError as e:
            print("Arquivo de gif não encontrado:", e)
            gif = None
        label = tk.Label(root)
        label.pack()
        atualizar_gif()
        reiniciar_btn = tk.Button(root, text="Reiniciar", command=reiniciar_gif, state=tk.DISABLED)
        reiniciar_btn.pack()

        root.mainloop()

daniel = Mapas()


# marcadores
agua = '\U0001f4a7'
coracao = '♥'
carne = '🥩'
moeda = '\033[33m 💰'
escudo = '🛡️'
barra_de_vida_demogorgon = '━'
floco_de_gelo =  ['❄', '']
floco = floco_de_gelo[0]
garrafa_de_agua = f'\033[36m{agua}'
alimento_de_carne = carne
cura = coracao

# classe organizacional
class Alimentos():
    def __init__(self):

        self.quantidade_de_agua = 10
        self.quantidade_de_carne = 10
        self.quantidade_de_aditivo_de_cura = 10
        self.quantidade_de_escudo  = 8

        self.garrafa_de_agua_para_beber = garrafa_de_agua * self.quantidade_de_agua
        self.carne_para_comer = alimento_de_carne * self.quantidade_de_carne
        self.aditivo_de_cura = coracao * self.quantidade_de_aditivo_de_cura
        self.escudo_para_usar = escudo * self.quantidade_de_escudo



    def lendo_mercadinho(self):
        with open('vozmercadinho.py', 'r') as mercadinho:
            for linha in mercadinho:
                frase = gtts.gTTS(linha, lang='pt-br')
                frase.save('frase.mp3')
                playsound('frase.mp3')


alimentos = Alimentos()






















