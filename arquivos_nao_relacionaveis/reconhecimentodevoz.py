


import speech_recognition as sr
import pyttsx3
from time import sleep
from datetime import datetime



hora_atual = datetime.now()
hora = hora_atual.strftime("%I")
falar = pyttsx3.init('sapi5')
rec = sr.Recognizer()

a = 'inicializando sistema de reconhecimento de voz..'.upper()
print(f'\033[36m{a:^100}\033[m')
sleep(1)
def bom_dia():
    frase = 'bom dia daniel, como voçê está?'
    falar.say(frase)
    falar.runAndWait()
def boa_tarde():
    frase = 'boa tarde daniel, como voçê está?, o tempo está quente pelo jeito'
    falar.say(frase)
    falar.runAndWait()

def boa_noite():
    frase = f'boa noite daniel, jã são {hora} horas da noite, estava lhe aguardando chegar'
    falar.say(frase)
    falar.runAndWait()
def estou_bem():
    frase = 'fico feliz que esteja bem, também estou bem, executando diversos códigos como sempre'
    falar.say(frase)
    falar.runAndWait()
def demogorgon():
    frase = 'mostrando demogorgon na tela'
    falar.say(frase)
    falar.runAndWait()
    print('dps apareço')

def marina():
    frase = 'marina não gosta de daniel'
    falar.say(frase)
    falar.runAndWait()


with sr.Microphone() as mic:
    while True:
        rec.adjust_for_ambient_noise(mic)
        print("escutando..")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        texto.split()
        texto = ''.join(texto)
        if 'bom dia' in texto:
            bom_dia()
        elif 'ma' or 'marina' in texto:
            marina()
        elif ' tarde' in texto:
            boa_tarde()
        elif ' noite' in texto:
            boa_noite()
        elif 'estou bem' in texto:
            estou_bem()
        elif 'projeto' in texto:
            print('em breve abrirei o projeto')
        elif 'demogor' in texto:
            demogorgon()
        elif 'encerrar' in texto:
            print('\033[1m \033[31m PROGRAMA ENCERRADO')
            break
        else:
            print('não executado')