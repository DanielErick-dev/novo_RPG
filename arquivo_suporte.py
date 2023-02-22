

from playsound import playsound
import pygame
from time import sleep
import tkinter as tk
from PIL import Image, ImageTk




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
        sons.sons_gerais('sons_gerais/som_equipando_armadura ')
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






















