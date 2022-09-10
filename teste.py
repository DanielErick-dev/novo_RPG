

import gtts
from playsound import playsound
import pyttsx3
import pygame
from time import sleep
pygame.init()

from random import randint as ran

class Sons:
    falar = pyttsx3.init('sapi5')

    # SONS DE ASHE:
    def som_ashe_comeco_do_jogo(self):
        playsound('voz_ashe_arqueira.mp3')
    def som_ashe_final_de_partida(self):
        playsound('voz_ashe_final_de_partida.mp3')
    def som_ashe_atacando(self, volume=0):
        playsound('ashe_enxurrada_de_flechas.mp3')




    # SONS DE ANDREY:
    def som_andrey_começo_de_partida(self):
        playsound('voz_espadachim.mp3')
    def som_andrey_final_de_partida(self):
        playsound('andrey_final_de_partida.mp3')
    def corte_duplo_andrey(self):
        playsound('corte_duplo_andrey.mp3')

    # SONS DE VIEGO:
    def som_viego_final_de_partida(self):
        playsound('som_viego_final_de_partida.mp3')
    def som_viego_comeco_de_partida(self):
        playsound('fala_inicio_viego.mp3')
    def som_ressuscitar(self):
        playsound('som_viego_durante_batalha.mp3')

    # SONS ALEATÓRIOS
    def som_armadura_quebrando(self):
        playsound('armadura_quebrando.mp3')
    def som_equipando_armadura(self):
        playsound('equipando_escudo.mp3')
    def som_de_comer(self):
        playsound('personagemcomendo.mp3')

    def som_de_beber(self):
        playsound('beberagua.mp3')

    def som_de_portal(self):
        playsound('portalmagico.mp3')

    def tomando_pocao(self):
        playsound('pilulamagica.mp3')

    def som_game_over(self):
        playsound('somgameover.mp3')

    def som_abrindo_bau(self):
        playsound('abrindobau.mp3')

    def som_regenerando_armadura(self):
        playsound('regenerando_armadura.mp3')

    def som_demogorgon_aparecendo(self):
        #inicializando demogorgon
        pygame.init()
        pygame.mixer.init()
        som = pygame.mixer.Sound('som_demogorgon_aparecendo.wav')
        som.play()

    def som_floresta_encantada(self, volume=1):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        self.musica_de_fundo_floresta_encantada = pygame.mixer.music.load('som_floresta.mp3')
        pygame.mixer.music.play()

    def som_floresta_invertida(self, volume=1):
        sons.som_floresta_encantada(0)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        self.musica_de_fundo_floresta_invertida = pygame.mixer.music.load('floresta_invertida.mp3')
        pygame.mixer.music.play()
    def som_caverna(self, volume=0.8):
        sons.som_floresta_encantada(0)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        self.musica_de_fundo_caverna = pygame.mixer.music.load('som_de_fundo_caverna.mp3')
        pygame.mixer.music.play()
    def som_flecha_sendo_lancada(self, volume=1):
        playsound('ashe_flecha_sendo_lancada.mp3')

    def som_floresta_de_neve(self, volume=1):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        self.musica_de_fundo_floresta_de_neve = pygame.mixer.music.load('y2meta.com - Sons da Natureza - Vento forte (320 kbps).mp3')
        pygame.mixer.music.play()




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
        sleep(2)
        janela.blit(fundo, dest=position)
        pygame.display.update()
        if contador_de_janela == 10:
            pygame.quit()
            break
    print(f'\033[1m \033[4m \033[36m {"se prepare pra floresta de neve".upper():^100} \033[m')

sons.som_floresta_de_neve(0.5)
mostrando_floresta_de_neve()
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






















