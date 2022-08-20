
import gtts
from playsound import playsound
import pyttsx3
from random import randint as ran

falar = pyttsx3.init('sapi5')

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
        with open('mercadinho.py') as mercadinho:
            for linha in mercadinho:
                frase = gtts.gTTS(linha, lang='pt-br')
                frase.save('frase.mp3')
                playsound('frase.mp3')


alimentos = Alimentos()

















