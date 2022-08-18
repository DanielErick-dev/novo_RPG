
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

garrafa_de_agua = f'\033[36m{agua}'
alimento_de_carne = carne
cura = coracao

# classe organizacional
class Alimentos():
    def __init__(self):
        self.quantidade_de_agua = 10
        self.quantidade_de_carne = 10
        self.quantidade_de_aditivo_de_cura = 10
        self.garrafa_de_agua_para_beber = garrafa_de_agua * self.quantidade_de_agua
        self.carne_para_comer = alimento_de_carne * self.quantidade_de_carne
        self.aditivo_de_cura = coracao * self.quantidade_de_aditivo_de_cura


    def lendo_mercadinho(self):
        with open('mercadinho.py') as mercadinho:
            for linha in mercadinho:
                frase = gtts.gTTS(linha, lang='pt-br')
                frase.save('frase.mp3')
                playsound('frase.mp3')

alimentos = Alimentos()


barra_de_vida_demogorgon = '━'
#classe de combate com demogorgon
class Combate_Demogorgon():
    def __init__(self, nome):
        self.nome = nome
        self.vida = None
        self.contador_de_vida = 30
        self.dano = 0
    def voz(self):
        frase = str('demogorgon se aproxima')
        falar.say(frase)
        falar.runAndWait()

    def som_demogorgon_atacando(self):
        playsound('somdemogorgon_atacando.mp3')
    def mostrar_vida(self):
        self.vida_demogorgon = barra_de_vida_demogorgon * self.contador_de_vida
        print(f'\033[31m \033[1m{"VIDA DEMOGORGON":^100}\033[m')
        print(f'\033[31m \033[1m{self.vida_demogorgon:^100}\033[m')

    def demogorgon_jogando(self):
        self.dado_demogorgon = ran(1, 12)
        print('demogorgon atacando..')
        if self.dado_demogorgon <= 3:
            self.dano = 2
        elif self.dado_demogorgon <= 6:
            self.dano = 5
        elif self.dado_demogorgon <= 9:
            self.dano = 7
        elif self.dado_demogorgon <= 12:
            self.dano = 7
        print(f'dano imposto por demogorgon: {self.dano}')
        daniel.contador_de_vida -= self.dano

    def personagem_jogando(self):
        self.dado_personagem = ran(1, 12)
        print('personagem está atacando..')
        if self.dado_personagem <= 3:
            self.dano = 2
        elif self.dado_personagem <= 6:
            self.dano = 5
        elif self.dado_personagem <= 9:
            self.dano = 7
        elif self.dado_personagem <= 12:
            self.dano = 7
        print(f'dano imposto por personagem: {self.dano}')
        demogorgon.contador_de_vida -= self.dano

demogorgon = Combate_Demogorgon('demogorgon')






