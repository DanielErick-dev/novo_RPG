

from playsound import playsound
import pygame
from time import sleep




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
        playsound('voz_ashe_final_de_partida.mp3')
    def som_ashe_atacando(self, volume=0):
        playsound('enxurrada_de_flechas_ashe.mp3')




    # SONS DE ANDREY:
    def som_andrey_começo_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_começo.mp3')
    def som_andrey_meio_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_meio.mp3')
    def som_andrey_final_de_partida(self):
        sons.sons_gerais('vozes_andrey/andrey_final.mp3')



    # SONS DE VIEGO:
    def som_viego_comeco_de_partida(self):
        sons.sons_gerais('vozes_viego/viego_começo.mp3')
    def som_viego_meio_de_partida(self):
        sons.sons_gerais('vozes_viego/viego_meio.mp3')
    def som_viego_final(self):
        sons.sons_gerais('vozes_viego/viego_final.mp3')

    # SONS ALEATÓRIOS
    def som_geral_de_trilha_sonora(self, volume=1, nome=None):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        musica_a_ser_tocada = pygame.mixer.music.load(nome)
        pygame.mixer.music.play()
    def som_armadura_quebrando(self):
        pass
    def som_equipando_armadura(self):
        pass
    def som_de_comer(self):


    def som_de_beber(self):


    def som_de_portal(self):


    def tomando_pocao(self):


    def som_game_over(self):


    def som_abrindo_bau(self):


    def som_regenerando_armadura(self):


    def som_demogorgon_aparecendo(self):


    def som_floresta_encantada(self, volume=1):
        sons.som_geral_de_trilha_sonora(volume=1, nome='sons_gerais/som_floresta.mp3')

    def som_floresta_invertida(self, volume=1):

    def som_caverna(self, volume=0.8):

    def som_flecha_sendo_lancada(self):



    def som_floresta_de_neve(self, volume=1):





sons = Sons()















def mostrando_floresta_encantada():
    janela = pygame.display.set_mode((1400, 540))
    fundo = pygame.image.load('floresta_encantada_editado.jpg')
    contador_de_janela = 0
    position = (0, 0)
    while True:
        contador_de_janela += 1
        sleep(2)
        janela.blit(fundo, dest=position)
        pygame.display.update()
        if contador_de_janela == 4:
            pygame.quit()
            break
    print(f'\033[32m \033[1m {"SIGA EM FRENTE, ATRAVESSE AS ÁRVORES":^100} \033[m')
def mostrando_floresta_de_neve():
    janela = pygame.display.set_mode((1300, 700))
    fundo = pygame.image.load('floresta_de_neve_editado.png')
    contador_de_janela = 0
    position = (0, 0)
    while True:
        contador_de_janela += 1
        sleep(0.2)
        janela.blit(fundo, dest=position)
        pygame.display.update()
        if contador_de_janela == 10:
            pygame.quit()
            break
    print(f'\033[1m \033[4m \033[36m {"se prepare pra floresta de neve".upper():^100} \033[m')


def mostrando_floresta_invertida():
    janela = pygame.display.set_mode((1672, 700))
    fundo = pygame.image.load('floresta_invertida_editado.jpg')
    contador_de_janela = 0
    position = (0, 0)
    while True:
        contador_de_janela += 1
        sleep(2)
        janela.blit(fundo, dest=position)
        pygame.display.update()
        if contador_de_janela == 3:
            pygame.quit()
            break
    print(f'\033[1m \033[4m \033[35m {"siga seu caminho entre as àrvores da floresta invertida".upper():^100} \033[m')


def mostrando_caverna():
    janela = pygame.display.set_mode((1200, 675))
    fundo = pygame.image.load('caverna_mágica.jpg')
    contador_de_janela = 0
    position = (0, 0)
    while True:
        janela.blit(fundo, dest=position)
        pygame.display.update()
        sons.som_caverna(1.5)
        sleep(6)
        contador_de_janela += 1
        if contador_de_janela == 1:
            pygame.quit()
            break
    print(f'\033[1m \033[4m \033[32m {"suba as escadas e entre na caverna mágica".upper():^100} \033[m')



# marcadores
agua = '\U0001f4a7'
coracao = '♥'
carne = '🥩'
moeda = '\033[33m💰'
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






















