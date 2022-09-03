

import gtts
from playsound import playsound
import pyttsx3
import pygame
from time import sleep


from random import randint as ran


falar = pyttsx3.init('sapi5')

# SONS DE ARFRID:
def som_arfrid_comeco_do_jogo():
    playsound('voz_ashe_arqueira.mp3')
def som_arfrid_sendo_sarcastica():
    playsound('arfrid_sarcasmomp3')
def som_chuva_de_flechas():
    playsound('rajada_de_flechas.mp3')


# SONS DE ANDREY:
def som_andrey_começo_de_partida():
    playsound('voz_espadachim.mp3')
def som_andrey_final_de_partida():
    playsound('andrey_final_de_partida.mp3')
def corte_duplo_andrey():
    playsound('corte_duplo_andrey.mp3')

# SONS DE GERALT:
def som_geralt_final_de_partida():
    playsound('som_final_de_partida_geralt.mp3')
def som_geralt_comeco_de_partida():
    playsound('som_comeco_de_partida_geralt.mp3')
def som_ressuscitar():
    playsound('ressuscitar.mp3')

# SONS ALEATÓRIOS
def som_armadura_quebrando():
    playsound('armadura_quebrando.mp3')
def som_equipando_armadura():
    playsound('equipando_escudo.mp3')
def som_de_comer():
    playsound('personagemcomendo.mp3')

def som_de_beber():
    playsound('beberagua.mp3')

def som_de_portal():
    playsound('portalmagico.mp3')

def tomando_pocao():
    playsound('pilulamagica.mp3')

def som_game_over():
    playsound('somgameover.mp3')

def som_abrindo_bau():
    playsound('abrindobau.mp3')
def som_regenerando_armadura():
    playsound('regenerando_armadura.mp3')

def som_demogorgon_aparecendo():
    #inicializando demogorgon
    pygame.init()
    pygame.mixer.init()
    som = pygame.mixer.Sound('som_demogorgon_aparecendo.wav')
    som.play()

def som_floresta_encantada():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.load('som_floresta.mp3')
    pygame.mixer.music.play()
def mostrando_floresta_encantada():
    janela = pygame.display.set_mode((1400, 700))
    fundo = pygame.image.load('floresta_encantada_editado.jpg')
    contador_de_janela = 0
    position = (0, 0)
    while True:
        contador_de_janela += 1
        sleep(3)
        janela.blit(fundo, dest=position)
        pygame.display.update()
        if contador_de_janela == 4:
            pygame.quit()
            break
    print(f'\033[32m \033[1m {"SIGA EM FRENTE, ATRAVESSE AS ÁRVORES":^100} \033[m')
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






















