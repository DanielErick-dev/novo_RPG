
import time
from datetime import datetime
from time import sleep
import pyttsx3
from threading import Thread
from playsound import playsound
import pygame
import gtts

falar = pyttsx3.init('sapi5') #inicializando a engine

while True:
   f = input('type a text: ')
   falar.say(f)
   falar.runAndWait()

def tocando_alarme():
    with open('comandodevoz.py', 'r') as arquivo:
        for linha in arquivo:
            frase = gtts.gTTS(linha, lang='pt-br')
            frase.save('frase.mp3')
            playsound('frase;mp3')

hora_atual = datetime.now()
print(hora_atual)
def alarme():
    while True:
        control = 1
        h_alarme = '01'
        m_alarme = '09'
        p_alarme = 'PM'.upper()
        hora_atual = datetime.now()
        hora = hora_atual.strftime("%I")
        minuto = hora_atual.strftime("%M")
        periodo = hora_atual.strftime("%p")
        if control == 1:
            if p_alarme == periodo:
                if h_alarme == hora:
                    if m_alarme == minuto:
                        tocar_alarme()
                        control += 1
        sleep(15)
        if control == 1:
            t1 = Thread(target=alarme)
            t1.start()
        if control > 1:
            break
alarme()
f = 'foi pego pelo python rafael'.upper()
print(f'\033[1m \033[31m {f:^100}\033[m')