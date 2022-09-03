from random import randint as ran
from random import choice
import teste
from teste import alimentos
from time import sleep
import gtts
from playsound import playsound
import pyttsx3
import pygame
pygame.init()

class PrimeiraParte(Exception):
    def voz_mercadinho(self):
        falar = pyttsx3.init('sapi5')
        frase = 'bem vindo ao mercadinho mágico'
        falar.say(frase)
        falar.runAndWait()

    def mostrando_bau(self):
        janela = pygame.display.set_mode((700, 565))
        position = (0, 0)
        fundo = pygame.image.load('baueditado.jpg')
        pygame.display.set_caption('baú mágico')
        janela_aberta = True
        while janela_aberta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            janela.blit(fundo, dest=position)
            pygame.display.update()
        pygame.quit()
    def mostrando_demogorgon(self):
        janela = pygame.display.set_mode((700, 690))
        position = (0, 0)
        fundo = pygame.image.load('The_Demogorgon.png')
        pygame.display.set_caption('demogorgon')
        janela_aberta = True
        while janela_aberta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            janela.blit(fundo, dest=position)
            pygame.display.update()
        pygame.quit()


    def personagem01(self):
        janela = pygame.display.set_mode((350, 580))
        fundo = pygame.image.load('personagem.jpg')
        pygame.display.set_caption('personagem 01 Andrey')
        position = (0, 0)
        janela_aberta = True
        while janela_aberta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
            janela.blit(fundo, dest=position)
            pygame.display.update()
        pygame.quit()
    def personagem02(self):
        janela = pygame.display.set_mode((500, 600))
        fundo = pygame.image.load('ARQUEIRA_editado.jpg')
        pygame.display.set_caption('personagem 02 Arfrid')
        position = (0, 0)
        janela_aberta = True
        while janela_aberta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
                janela.blit(fundo, dest=position)
                pygame.display.update()
        pygame.quit()
    def personagem03(self):
        janela = pygame.display.set_mode((400, 500))
        fundo = pygame.image.load('bruxo.webp')
        pygame.display.set_caption('personagemg 03 bruxo')
        position = (0, 0)
        janela_aberta = True
        while janela_aberta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
                janela.blit(fundo, dest=position)
                pygame.display.update()
        pygame.quit()
    def som_do_personagem(self, persona):
        if persona == 'andrey':
            playsound('somdeespada.mp3')
        elif persona == 'arfrid':
            playsound('somdeflecha.mp3')
        elif persona == 'geralt':
            playsound('somdefogo.mp3')
    def manual(self):
        print('''
            ---------------------------------------------------------------------------------------------------------------------------
            |                                  BEM VINDO AO JOGO RPG                                                                  |
            |OBJETIVO:                                                                                                                |
            |       essa fase do jogo é chamada de floresta encantada no qual voçê deverá sobreviver atentando se aos obstáculos      |
            |       no qual durante o jogo os niveis de fome e de sede vão diminuindo, alimente-se e sobreviva durante o jogo         |
            |                                                                                                                         |
            |INFORMAÇÕES IMPORTANTES:                                                                                                 |
            |    se o personagem estiver com fome/sede zerado sua vida zera gradativamente                                            |
            |    o jogo será encerrado caso sua vida seja totalmente zerada                                                           |
            |    o número de casas que será caminhado é um número aleatório                                                           |
            |    a floresta encantada é encerrada ao chegar na casa 100                                                               |
            |    algumas casas possuem especialidades que voçê verá durante o jogo                                                    |
            |    o jogo têm desvios lógicos para permitir a interação e possibilidade estratégica do jogador em seus caminhos         |
            |                                                                                                                         |
            |RECURSOS INICIAIS:                                                                                                       |
            |    1 garrafa de àgua, 1 carne, 1 poção de cura, 1 arma, 50 moedas                                                       |
            |MERCADO:                                                                                                                 |
            |    para acessar o mercado basta digitar 'mercado', lembrando que para a compra de recursos, é necessário ter moedas     |
            |                                                                                                                         |
            |ARENA DE COMBATE:                                                                                                        |
            |     dentro da arena de combate teremos determinado monstro do programa interagindo contra o personagem                  | 
            |                                                                                                                         |
            |INVENTÁRIO:                                                                                                              |
            |   para acessar seu inventário basta escrever mochila no "digite enter cavalheiro" e veja seus recursos disponiveis      |
            |                                                                                                                         |
            |CRISTAL:                                                                                                                 |
            |   a função do cristal é atentar o jogador de determinado oponente que ele enfrentará durante o caminho, para usar escreva|
            |    'cristal' no 'aperte enter cavalheiro' lembrando, o cristal nao começará no seu estoque inicial. obtenha-o           |
            |TROCA:                                                                                                                   |
            |    para trocar um item do seu inventário por moedas basta escrever TROCA e digitar o nome do item que deseja vender     |                                                                                                                   
            |UPAR ARMADURA:                                                                                                           |
            |   ao ter a armadura em seu inventário, para melhorar seu nivel, basta escrever upar armadura que poderá aumentar o nivel|
            ---------------------------------------------------------------------------------------------------------------------------
        ''')

    def __init__(self, nome):
        self.casa = 0
        self.nome = nome
        self.portal = 0
        self.contador_de_fome = 8
        self.contador_de_sede = 8
        self.contador_de_vida = 20
        self.garrafa_de_agua = 'garrafa de agua'
        self.carne = 'carne          '
        self.aditivo_de_cura = 'aditivo de cura'
        self.arma = 'arma           '
        self.moeda = 50
        self.cristal = 'cristal        '
        self.inventario = [self.garrafa_de_agua, self.carne, self.aditivo_de_cura]
        self.revivedor = 'revivedor      '
        self.armadura = 'armadura       '
        self.reparador = 'reparador      '
        self.upador_de_armadura = 'upar armadura  '
        self.acelerador_de_habilidade = 'acelerador ULT '
        self.mercado = {self.garrafa_de_agua: 10, self.carne: 10, self.aditivo_de_cura: 15, self.arma: 20, self.cristal: 25, self.revivedor: 30, self.armadura: 15, self.reparador: 10, self.upador_de_armadura: 15, self.acelerador_de_habilidade: 10}
        self.list_itens_comprados = []
        self.personagem_escolhido = ''
        self.CONTADOR_DE_BATALHA_DEMOGORGON = 0
        self.STATUS = True
        self.escudo_escolhido = [self.armadura]
        self.contador_de_armadura = 12
        self.marcador_de_armadura = teste.escudo * self.contador_de_armadura
        self.opcao_de_armadura = False
        self.STATUS_ARMADURA = False
        self.nivel_de_escudo = 1




    def escolha_de_personagem(self):
        print('''\npersonagem 01 - andrey - caçador assassino
personagem 02 - arfrid - arqueira 
personagem 03 - geralt - bruxo''')
        while True:
            escolha = str(input('escreva o nome do personagem que você deseja: ')).lower()
            if escolha == 'andrey':
                self.personagem_escolhido = 'andrey'
                teste.som_andrey_começo_de_partida()
                break
            elif escolha == 'arfrid':
                self.personagem_escolhido = 'arfrid'
                teste.som_arfrid_comeco_do_jogo()
                break
            elif escolha == 'geralt':
                self.personagem_escolhido = 'geralt'
                teste.som_geralt_comeco_de_partida()
                break
            else:
                print('\033[31mopção de personagem inválida\033[m')
        print(F'personagem escolhido: {self.personagem_escolhido}')
        sleep(3)
    def mercadinho(self):
        print(f'\033[35m \033[1m{"BEM VINDO AO MERCADINHO MÁGICO":^50}\033[m')
        daniel.voz_mercadinho()
        self.codigo_agua = '245'
        self.codigo_carne = '103'
        self.codigo_pocao = '205'
        self.codigo_arma = '934'
        self.codigo_cristal = '534'
        self.codigo_revivedor = '890'
        self.codigo_armadura = '387'
        self.codigo_reparador = '631'
        self.codigo_upador_de_armadura = '027'
        self.codigo_acelerador_de_habilidade = '112'
        self.list_de_codigo = [self.codigo_agua, self.codigo_carne, self.codigo_pocao, self.codigo_arma, self.codigo_cristal, self.codigo_revivedor, self.codigo_armadura, self.codigo_reparador, self.codigo_upador_de_armadura, self.codigo_acelerador_de_habilidade]
        c = 0
        print('\033[31m \033[1m \033[4m')
        print('|CÓDIGO|        |ITEM|          |MOEDAS|\033[m')
        for k, v in self.mercado.items():
            print(f'  {self.list_de_codigo[c]}        {k}       {v}')
            c += 1
        print('\033[1m \033[31m \033[4m-' * 13)
        print('\033[m')
        while True:
            opcao = str(input('comprará algo do mercado mágico? ')).lower()
            if opcao == 'sim':
                daniel.compra_no_mercado()
                break
            elif opcao == 'não' or opcao == 'nao':
                print('fechando mercado')
                break
            else:
                print('\033[31mdigite apenas sim ou não cavalheiro\033[m')
    def escolhendo_e_organizando_armaduras(self):
        if daniel.armadura in daniel.inventario:
            while True:
                self.opcao = str(input('deseja utilizar sua armadura? ')).lower()
                if self.opcao == 'sim':
                    daniel.opcao_de_armadura = True
                    print(' \033[31m \033[4m equipando armadura \033[m')
                    teste.som_equipando_armadura()
                    daniel.inventario.append(daniel.armadura)
                    break
                elif self.opcao == 'não' or self.opcao == 'nao':
                    daniel.opcao_de_armadura = False
                    if daniel.personagem_escolhido == 'arfrid':
                        print(f'inutilização de armadura,{daniel.personagem_escolhido} está desprotegida')
                        break
                    else:
                        print(f'inutilização de armadura,{daniel.personagem_escolhido} está desprotegido')
                        break
                else:
                    print('\033[31m \033[1m apenas sim ou não \033[m')
                    daniel.escolhendo_e_organizando_armaduras()

        else:
            print()





    def compra_no_mercado(self):
        codigo = str(input(f'digite o código do item que deseja comprar {self.nome}: '))
        if codigo == self.codigo_agua:
            if self.moeda >= self.mercado[self.garrafa_de_agua]:
                self.moeda -= self.mercado[self.garrafa_de_agua]
                self.inventario.append(self.garrafa_de_agua)
                self.list_itens_comprados.append(self.garrafa_de_agua)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar a garrafa de àgua')
        elif codigo == self.codigo_carne:
            if self.moeda >= self.mercado[self.carne]:
                self.moeda -= self.mercado[self.carne]
                self.inventario.append(self.carne)
                self.list_itens_comprados.append(self.carne)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar a carne')
        elif codigo == self.codigo_pocao:
            if self.moeda >= self.mercado[self.aditivo_de_cura]:
                self.moeda -= self.mercado[self.aditivo_de_cura]
                self.inventario.append(self.aditivo_de_cura)
                self.list_itens_comprados.append(self.aditivo_de_cura)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar a poção de cura')
        elif codigo == self.codigo_arma:
            if self.moeda >= self.mercado[self.arma]:
                self.moeda -= self.mercado[self.arma]
                self.inventario.append(self.arma)
                self.list_itens_comprados.append(self.arma)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar a arma')
        elif codigo == self.codigo_cristal:
            if self.moeda >= self.mercado[self.cristal]:
                self.moeda -= self.mercado[self.cristal]
                self.inventario.append(self.cristal)
                self.list_itens_comprados.append(self.cristal)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o cristal')
        elif codigo == self.codigo_revivedor:
            if self.moeda >= self.mercado[self.revivedor]:
                self.moeda -= self.mercado[self.revivedor]
                self.inventario.append(self.revivedor)
                self.list_itens_comprados.append(self.revivedor)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o revivedor')

        elif codigo == self.codigo_armadura:
            if self.moeda >= self.mercado[self.armadura]:
                self.moeda -= self.mercado[self.armadura]
                self.inventario.append(self.armadura)
                self.list_itens_comprados.append(self.armadura)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o escudo')
        elif codigo == self.codigo_reparador:
            if self.moeda >= self.mercado[self.reparador]:
                self.moeda -= self.mercado[self.reparador]
                self.inventario.append(self.reparador)
                self.list_itens_comprados.append(self.reparador)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o reparador de escudo')
        elif codigo == self.codigo_upador_de_armadura:
            if self.moeda >= self.mercado[self.upador_de_armadura]:
                self.moeda -= self.mercado[self.upador_de_armadura]
                self.inventario.append(self.upador_de_armadura)
                self.list_itens_comprados.append(self.upador_de_armadura)
                print('item comprado')
            else:
                print('quantidade de moedas insuficientes para comprar o upador de armadura')
        elif codigo == self.codigo_acelerador_de_habilidade:
            if self.moeda >= self.mercado[self.acelerador_de_habilidade]:
                self.moeda -= self.mercado[self.acelerador_de_habilidade]
                self.inventario.append(self.acelerador_de_habilidade)
                self.list_itens_comprados.append(self.acelerador_de_habilidade)
                print('item comprado')
            else:
                print('quantidade de moedas insuficientes para comprar o acelerador de habilidade')
        else:
            print('\033[31m \033[1m             código inserido não corresponde a nenhum produto do mercado mágico \033[m')
            daniel.compra_no_mercado()
        while True:
            opcao = str(input('deseja comprar mais alguma coisa do mercado mágico? ')).lower()
            if opcao == 'sim':
                daniel.compra_no_mercado()
                break
            elif opcao in 'nãonao':
                daniel.mostrando_items_comprados()
                print(f'\n \033[31m \033[4m {"fechando mercado mágico".upper():^60}\033[m')
                break
            else:
                print('\033[31m \033[1m    opção inválida, apenas sim ou não cavalheiro  \033[m')
    def mostrando_items_comprados(self):
        print(f'\033[33m \033[1m \033[4m {"items comprados:".upper():^80} \033[m')
        for item in self.list_itens_comprados:
            print(f'{item:^80}')
        print(f'{"->"* len("items comprados"):^80}')
    def pulando_casas(self, valor):
        self.casa += valor
        self.contador_de_fome -= 1
        self.contador_de_sede -= 1
        if self.contador_de_fome <= 0:
            self.contador_de_fome = 0
            if self.contador_de_fome == 0:
                daniel.alimentar()
                self.contador_de_vida -= 1
        if self.contador_de_sede <= 0:
            self.contador_de_sede = 0
            if self.contador_de_sede == 0:
                daniel.beber_agua()
                self.contador_de_vida -= 1
        if self.contador_de_vida <= 2:
            daniel.recuperar_vida()

        if self.casa == 55:
            daniel.casa55()
        elif self.casa == 11:
            daniel.casa11()
        elif self.casa == 15:
            self.portal += 1
            print('\033[32m prepare-se para aventura no portal \033[m')
            teste.som_de_portal()
            daniel.portal1()
        elif self.casa == 33:
            daniel.casa33()
        elif self.casa == 55:
            daniel.casa52()
        elif self.casa == 35:
            self.portal += 1
            print('\033[32m prepare-se para aventura no portal\033[m')
            teste.som_de_portal()
            daniel.portal2()
        elif self.casa == 50:
            self.portal += 1
            print('\033[32m prepare-se para aventura no portal\033[m')
            teste.som_de_portal()
            daniel.portal3()
        elif self.casa == 60:
            daniel.casa60()
        elif self.casa == 45:
            daniel.casa45()
        elif self.casa == 78:
            daniel.casa78()
        elif self.casa == 95:
            daniel.casa95()
        elif self.casa == 86:
            daniel.casa86()
        elif self.casa == 67:
            daniel.casa67()
        elif self.casa == 60:
            daniel.bau_surpresa()
        elif self.casa == 20:
            daniel.bau_surpresa()
        elif self.casa == 70:
            daniel.bau_surpresa()
        elif 50 > self.casa >= 40:
            self.CONTADOR_DE_BATALHA_DEMOGORGON += 1
            if self.CONTADOR_DE_BATALHA_DEMOGORGON == 1:
                daniel.rota2_floresta_invertida()
        elif self.casa == 80:
            daniel.fruta_envenenada()
        elif self.casa == 68:
            daniel.casa68()

    def leitura_em_voz(self):
        with open('lendoflorestaencantada.py', 'r') as arquivo:
            for linha in arquivo:
                frase = gtts.gTTS(linha, lang='pt-br')
                frase.save('frase.mp3')
                playsound('frase.mp3')

    def alimentar(self):
        while True:
            opcao = str(input('deseja comer? ')).lower()
            if opcao == 'sim':
                if self.carne in daniel.inventario:
                    self.marcador_de_fome += alimentos.carne_para_comer
                    self.contador_de_fome += alimentos.quantidade_de_carne
                    daniel.inventario.remove(self.carne)
                    print(f'aguarde, {self.personagem_escolhido} está se alimentando')
                    teste.som_de_comer()
                    break
                else:
                    print(f'alimento não encontrado na mochila de {self.personagem_escolhido}, obtenha seus recursos')
            elif opcao == 'não' or opcao == 'nao':
                print(f'{daniel.personagem_escolhido} está com fome')
                break
            else:
                print('\033[31m \033[m \033[4m digite apenas sim ou não \033[m')
    def beber_agua(self):
        while True:
            opcao = str(input('deseja beber àgua? ')).lower()
            if opcao == 'sim':
                if self.garrafa_de_agua in daniel.inventario:
                    self.marcador_de_sede += alimentos.garrafa_de_agua_para_beber
                    self.contador_de_sede += alimentos.quantidade_de_agua
                    daniel.inventario.remove(self.garrafa_de_agua)
                    print(f'aguarde, {self.personagem_escolhido} está se hidratando')
                    teste.som_de_beber()
                    break
                else:
                    print(f'garrafa de àgua não encontrada na mochila de {self.personagem_escolhido}, obtenha seus recursos')
                    break
            elif opcao == 'não' or opcao == 'nao':
                print(f'{daniel.personagem_escolhido} está com sede')
                break
            else:
                print('\033[31m \033[m \033[4m digite apenas sim ou não \033[m')


    def recuperar_vida(self):
        opcao = str(input('deseja recuperar sua vida perdida? ')).lower()
        if opcao == 'sim':
            if self.aditivo_de_cura in daniel.inventario:
                self.marcador_de_vida += alimentos.aditivo_de_cura
                self.contador_de_vida += alimentos.quantidade_de_aditivo_de_cura
                daniel.inventario.remove(self.aditivo_de_cura)
                print('vida sendo regenerada, aguarde')
                teste.tomando_pocao()
            else:
                print(f'poção não encontrado na mochila de {self.personagem_escolhido}, obtenha seus recursos')
        elif opcao == 'não' or opcao == 'nao':
            print(f'{daniel.personagem_escolhido} precisa recuperar sua vida')
        else:
            print('\033[31m \033[1m \033[4m digite apenas sim ou não \033[m')
    def inimigos_proximos_pelo_cristal(self):
        if daniel.cristal in daniel.inventario:
            while True:
                opcao = str(input('deseja utilizar o cristal mágico para localizar oponentes? ')).lower()
                if opcao == 'sim':
                    print('utilizando cristal mágico..')
                    daniel.utilizando_cristal()
                    break
                elif opcao == 'não' or opcao == 'nao':
                    print('cristal não utilizado')
                    break
                else:
                    print('\033[31m \033[1m digite apenas sim ou não cavalheiro \03[m')

        else:
            print(f'cristal mágico não encontrado no inventário de {daniel.personagem_escolhido}.')
    def utilizando_cristal(self):
        print(f'''cristal mágico revelando posições..
{sleep(2)}
demogorgon está dentro de uma das rotas alternativas em floresta invertida próximo a casa 40, oponente de nivel médio, dano levemente baixo
capacidade de matar = 40% vida = 30 fraqueza = ataques de fogo, não apresenta resistência mágica ou fisica aos danos que lhe atingem, oponente a altura.''')
        print('\ncristal mágico utilizado')
        daniel.inventario.remove(daniel.cristal)
    def mostrar_casa(self):
        if self.casa <= 100:
            print()
            print(f'voçê está na casa \033[35m {self.casa}\033[m')
            daniel.mostrar_fome()
            daniel.mostrar_sede()
            daniel.mostrar_vida()
            daniel.mostrar_moeda()
            print('')

    def casa22(self):
        self.casa -= 4
        print('\033[1mdeixou cair um item da mochila no percurso, retorne pra buscar\033[m')
        self.moeda -= 5
    def casa68(self):
        print('achou peixes ao lado da cachoeira, coma-os')
        sleep(2)
        daniel.contador_de_fome += 4
    def casa33(self):
        self.casa -= 10
        print('\033[1m escorregou na ponta da montanha e deixou seus recursos cairem, dê a volta pela encosta\033[m')
        self.inventario.clear()
        self.contador_de_vida -= 2
        self.contador_de_sede -= 1
        self.contador_de_fome -= 1
    def casa55(self):
        print(f'\033[1m monstros a sua espreita, volte 8 casas\033[m')
        self.casa -= 8

    def casa11(self):
        print(f'\033[1m achou um atalho da floresta encantada, avançe 9 casas')
        self.casa += 9

    # PORTAIS
    def portal1(self):
        print(f'\033[32m\033[1m \033[4m{"encontrou o primeiro portal da floresta encantada, viaje entre as dimensões para a casa 38".upper():^100}\033[m ')
        print('viajando entre as dimensões..')
        print('encontrou 10 moedas no caminho da viagem interdimensional')
        self.casa = 38
        self.moeda += 10
    def portal2(self):
        print(f'\033[32m \033[1m  \033[4m{"encontrou o segundo portal da floresta encantada, viaje entre as dimensões para a casa 71".upper():^100}\033[m ')
        self.casa = 39
    def portal3(self):
        print(f'\033[32m \033[1m  \033[4m {"encontrou o terceiro portal da floresta encantada, viaje entre as dimensões para a casa 90".upper():^100}\033[m ')
        self.casa = 90
    def recompensa_por_2_portais(self):
        print(f'brilhante {self.nome}, viajou entre 2 portais na floresta encantada, aproveite em breve sua recompensa de sorte')

    def primeira_parte_floresta(self, valor=0):
        floresta_encantada = 'voçê está na primeira parte de sua jornada, entre na floresta encantada'.upper()
        print(f'\033[32m\033[4m \033[1m {floresta_encantada:^100}\033[m')
        teste.som_floresta_encantada()
        teste.mostrando_floresta_encantada()


    # marcadores
    def mostrar_fome(self):
        self.marcador_de_fome = self.contador_de_fome * teste.carne
        print(f'   \033[31m          FOME \033[32m: {self.marcador_de_fome}', end='       ')


    def mostrar_vida(self):
        self.marcador_de_vida = teste.coracao * self.contador_de_vida
        print(f'  \033[1m   VIDA \033[m: {self.marcador_de_vida}', end='       ')


    def mostrar_sede(self):
        self.marcador_de_sede = self.contador_de_sede * teste.garrafa_de_agua
        print(f'  \033[36m   SEDE \033[m: \033[36m{self.marcador_de_sede}\033[m', end='       ')

    def mostrar_moeda(self):
        print(f'  \033[33m   MOEDA\033[m:{self.moeda}{teste.moeda}\033[m')


    #casas especiais
    def casa45(self):
        self.casa += 12
        print('\033[m avançe 12 casas\033[m')
    def casa60(self):
        self.casa -= 10
        print('\033[1m voçê se perdeu no caminho da floresta, retorne pelo caminho correto\033[m')
        self.contador_de_sede -= 2
    def casa78(self):
        self.casa -= 15
        print('\033[1m bateu de frente com animais selvagens, recue 15 casas\033[m')
    def casa95(self):
        self.casa -= 30
        print('\033[1m estava perto de sua chegada, porém foi agarrado e machucado pelas arvores mágicas\033[m')
        self.contador_de_vida -= 4
    def casa67(self):
        self.casa += 5
        print(f'\033[1m aproveitou a correnteza do rio e encheu a garrafinha, avançe {self.personagem_escolhido}\033[m')
        self.contador_de_sede += 3

    def casa52(self):
        print('um animal mágico puxou sua mochila e levou suas moedas')
        self.moeda -= 20
        if self.moeda <= 0:
            self.moeda = 0
    def casa30(self):
        print('encontrou um saquinho de moedas durante o caminho, pegue-as')
        self.moeda += 20
    def casa86(self):
        print('\033[1mcomeu fruto envenenado, se recupere cavalheiro\033[m')
        self.casa -= 2
        self.contador_de_sede -= 3
        self.contador_de_fome -= 3
        self.contador_de_vida -= 3
    def bau_surpresa(self):
        sleep(2)
        print('bem vindo ao baú surpresa, pague o preço do baú e resgate seu prêmio aleatório')
        print('preço do baú = 30 moedas')
        while True:
            opcao = str(input('deseja obter o baú surpresa por 30 moedas? ')).lower()
            if opcao == 'sim':
                if self.moeda >= 30:
                    list = [self.garrafa_de_agua, self.carne, self.aditivo_de_cura, self.arma, self.cristal, self.revivedor, self.armadura, self.reparador, self.upador_de_armadura]
                    bau = []
                    for c in range(0, 4):
                        item = choice(list)
                        bau.append(item)
                    for itens in bau:
                        sleep(1)
                        print(f'item adicionado: {itens}')
                        daniel.inventario.append(itens)
                        sleep(0.9)
                    self.moeda -= 30
                    break
                else:
                    print('\033[1m \033[31m quantidade insuficiente de moedas para abrir o baú surpresa, uma pena')
                    break
            elif opcao == 'não' or opcao == 'nao':
                print('\nignorando báu surpresa, quem sabe na próxima')
                break
            else:
                print(' \033[31m \033[1m \033[4m digite apenas sim ou não para abrir o baú surpresa \033[m')

    def reparando_escudo(self):
        self.STATUS_ARMADURA = False
        print(f'\n \033[31m \033[1m escudo de {daniel.personagem_escolhido} será quebrado em batalha... \033[m')
        if daniel.reparador in daniel.inventario:
            while True:
                sleep(1)
                opcao = str(input('deseja usar seu recuperador de armadura? ')).lower()
                if opcao == 'sim':
                    print('reparando armadura..')
                    teste.som_regenerando_armadura()
                    sleep(0.5)
                    print(f'\033[1m \033[31m {"armadura reparada com sucesso".upper():^40} \033[m')
                    sleep(0.6)
                    daniel.contador_de_armadura += 12
                    daniel.inventario.remove(daniel.reparador)
                    self.STATUS_ARMADURA = True
                    break
                elif opcao == 'não' or opcao == 'nao':
                    print('armadura será destruida')
                    print(f'\033[1m \033[31m {"armadura não será reparada".upper():^40} \033[m')
                    sleep(0.6)
                    self.STATUS_ARMADURA = False
                    break
                else:
                    print('\033[31m \033[1m digite apenas sim ou não \033[m')
        else:
            print(' \033[1m ausência de reparador de armadura  \033[m')
    def troca_de_item_por_moeda(self):
        while True:
            opcao = str(input('deseja fazer a troca do item por moedas?  ')).lower()
            if opcao == 'sim':
                break
            elif opcao == 'não' or opcao == 'nao':
                print('fechando troca de item por moeda')
                sleep(3)
                break
            else:
                print('\033[31mdigite apenas sim ou não cavalheiro\033[m')
        daniel.mostrando_inventario()
        opcao = str(input('digite qual item do inventário você deseja trocar por moedas? ')).lower()
        print('analisando item')
        def tamanho_da_variavel(variavel):
            while len(variavel) != 15:
                variavel += ' '
                if len(variavel) == 15:
                    break
            return variavel
        item = tamanho_da_variavel(opcao)
        if item in daniel.inventario:
            print(f'vendendo item..')
            sleep(2)
            for nome_do_item, preco in daniel.mercado.items():
                if nome_do_item == item:
                    self.item = nome_do_item
                    print(f'preço do item: {preco} moedas')
                    print('item vendido de volta para o mercado mágico')
                    daniel.moeda += preco
                    daniel.inventario.remove(self.item)
        else:
            print('este item não existe ou ele não se encontra em seu inventário, não foi possivel vende-lo, tente novamente')
            daniel.troca_de_item_por_moeda()
        while True:
            a = str(input('deseja trocar mais algo? ')).lower()
            if a == 'sim':
                daniel.troca_de_item_por_moeda()
                break
            elif a == 'não' or a == 'nao':
                break
            else:
                print('\033[31mdigite apenas sim ou não cavalheiro\033[m')






    def upar_armadura(self):
        if daniel.armadura not in daniel.inventario:
            print(f'não é possivel atribuir um nivel a mais para sua armadura pois {daniel.personagem_escolhido} não possui uma armadura')
        if daniel.upador_de_armadura not in daniel.inventario:
            print(f'não será possivel atribuir um nivel a mais para sua armadura pois {daniel.personagem_escolhido} não possui um upador de armadura em sua mochila')
        if daniel.upador_de_armadura and daniel.armadura in daniel.inventario:
            while True:
                opcao = str(input('deseja melhorar o nivel de sua armadura? ')).lower()
                if opcao == 'sim':
                    sleep(1)
                    print('\033[1m escudo sendo melhorado.. \033[m')
                    teste.som_equipando_armadura()
                    daniel.contador_de_armadura += 5
                    sleep(2)
                    print('\033[1m \033[4m \033[36m  ESCUDO MELHORADO - NIVEL AUMENTADO - \033[m')
                    print('\n')
                    self.nivel_de_escudo += 1
                    daniel.inventario.remove(daniel.upador_de_armadura)
                    break
                elif opcao == 'não' or opcao == 'nao':
                    sleep(1)
                    print('armadura permanece da mesma forma')
                    print('\n')
                    break
                else:
                    print('\033[31m \033[1m digite apenas sim ou não \033[m')
                    sleep(1)
    def voz_final_sarcastica_do_personagem(self):
        if daniel.personagem_escolhido == 'andrey':
            teste.som_andrey_final_de_partida()
        elif daniel.personagem_escolhido == 'arfrid':
            teste.som_arfrid_sendo_sarcastica()
        else:
            teste.som_geralt_final_de_partida()


    # ROTAS ALTERNATIVAS
    def rota1_caverna(self):
        pass


    def rota2_floresta_invertida(self):
        class CombateDemogorgon():
            def __init__(self, nome):
                self.nome = nome
                self.contador_de_vida = 30
                self.barra_de_vida_demogorgon = teste.barra_de_vida_demogorgon
                self.STATUS = True
                self.bau = [daniel.garrafa_de_agua, daniel.carne, daniel.aditivo_de_cura, daniel.armadura, daniel.revivedor]
                self.contador_de_ativacao_de_habilidade = 4

                self.dano_demogorgon = 0
            def habilidade_especial(self):
                if self.contador_de_ativacao_de_habilidade <= 0:
                    if daniel.personagem_escolhido == 'andrey':
                        while True:
                            sleep(2)
                            opcao = str(input('deseja ativar habilidade especial de andrey? ')).lower()
                            sleep(1)
                            if opcao == 'sim':
                                sleep(1)
                                teste.corte_duplo_andrey()
                                self.contador_de_ativacao_de_habilidade = 4
                                demogorgon.personagem_jogando()
                                break
                            elif opcao == 'não' or opcao == 'nao':
                                print()
                                break
                            else:
                                print('\033[31m \033[1m \033[4m apenas sim ou não \033[m')
                    if daniel.personagem_escolhido == 'arfrid':
                            while True:
                                sleep(2)
                                opcao = str(input('deseja ativar habilidade especial de arfrid? ')).lower()
                                sleep(1)
                                if opcao == 'sim':
                                    def chuva_de_flechas():
                                        cont = 0
                                        for c in range(0, 5):
                                            cont += 1
                                            dado = ran(0, 3)
                                            if dado == 0:
                                                pass
                                            elif dado == 1:
                                                self.dano_demogorgon += 1
                                            elif dado == 2:
                                                self.dano_demogorgon += 2
                                            else:
                                                self.dano_demogorgon += 3
                                            demogorgon.contador_de_vida -= self.dano_demogorgon
                                            print(f'{cont}° flecha sendo lançada')
                                            sleep(1)
                                    sleep(1)
                                    teste.som_chuva_de_flechas()
                                    chuva_de_flechas()
                                    sleep(2)
                                    print(f'dano total das chuvas de flechas de arfrid: {self.dano_demogorgon}')
                                    self.contador_de_ativacao_de_habilidade = 4
                                    break
                                elif opcao == 'não' or opcao == 'nao':
                                    print()
                                    break
                                else:
                                    print('\033[31m \033[1m \033[4m apenas sim ou não \033[m')
                    if daniel.personagem_escolhido == 'geralt':
                        while True:
                            sleep(2)
                            opcao = str(input('deseja ativar habilidade especial de geralt? ')).lower()
                            sleep(1)
                            if opcao == 'sim':
                                sleep(1)
                                print(' \033[1m RESSUSCITAR \033[m')
                                teste.som_ressuscitar()
                                self.contador_de_ativacao_de_habilidade = 4
                                daniel.contador_de_vida += demogorgon.dano_demogorgon
                                daniel.contador_de_vida += demogorgon.dano_demogorgon
                                if daniel.contador_de_vida > 0:
                                    daniel.STATUS = True
                                break
                            elif opcao == 'não' or opcao == 'nao':
                                print()
                                break
                            else:
                                print('\033[31m \033[1m \033[4m apenas sim ou não \033[m')


            def som_demogorgon_atacando(self):
                playsound('newsom_demogorgon_atacando.mp3')
            def narrando_demogorgon(self):
                falar = pyttsx3.init('sapi5')
                frase = str('demogórgon está se aproximando')
                falar.say(frase)
                falar.runAndWait()
            def demogorgon_aparecendo(self):
                demogorgon.narrando_demogorgon()
                sleep(1)
                daniel.mostrando_demogorgon()

            def mostrar_vida_demogorgon(self):
                sleep(1)
                self.vida_demogorgon = self.barra_de_vida_demogorgon * self.contador_de_vida
                daniel.marcador_de_vida = daniel.contador_de_vida * teste.coracao
                print(f'\033[31m \033[1m{"VIDA DEMOGORGON":^30} ', end='  ')
                if daniel.armadura in daniel.inventario:
                    print(f'\033[34m \033[1m{"VIDA PERSONAGEM":^30}  ', end='  ')
                else:
                    print(f'\033[34m \033[1m{"VIDA PERSONAGEM":^30}  ', end='  ')
                print(f'\033[33m \033[1m{"ARMADURA":^30}')
                print(f'\033[31m \033[1m{self.vida_demogorgon:^30} ', end='  ')
                print(f'\033[34m \033[1m{daniel.marcador_de_vida:^30}\033[m', end='  ')
                if daniel.opcao_de_armadura == True:
                    print(f'\033[1m {daniel.marcador_de_armadura:^30}\033[m')
                else:
                    print('')

            def demogorgon_jogando(self):
                self.dano_demogorgon = 0
                self.dado_demogorgon = ran(0, 12)
                print('demogorgon atacando..')
                demogorgon.som_demogorgon_atacando()
                if self.dado_demogorgon <= 1:
                    self.dano_demogorgon = 0
                    print(f'{daniel.personagem_escolhido} desviou do ataque')
                elif self.dado_demogorgon <= 3:
                    self.dano_demogorgon = 5
                    if daniel.opcao_de_armadura == True:
                        daniel.contador_de_armadura -= 1
                elif self.dado_demogorgon <= 6:
                    self.dano_demogorgon = 6
                    if daniel.opcao_de_armadura == True:
                        daniel.contador_de_armadura -= 3
                elif self.dado_demogorgon <= 9:
                    self.dano_demogorgon = 7
                    if daniel.opcao_de_armadura == True:
                        daniel.contador_de_armadura -= 3

                elif self.dado_demogorgon <= 12:
                    self.dano_demogorgon = 8
                    if daniel.opcao_de_armadura == True:
                        daniel.contador_de_armadura -= 5

                if daniel.opcao_de_armadura == True:
                    self.dano_demogorgon -= 3
                    if self.dano_demogorgon <= 0:
                        self.dano_demogorgon = 0
                    if daniel.nivel_de_escudo >= 2:
                        self.dano_demogorgon -= 2
                        daniel.contador_de_armadura += 1
                print(f'dano imposto por demogorgon: {self.dano_demogorgon}')
                print()
                daniel.contador_de_vida -= self.dano_demogorgon
                if daniel.contador_de_vida <= 0:
                    daniel.STATUS = False
                if demogorgon.STATUS <= 0:
                    demogorgon.STATUS = False
                if daniel.contador_de_armadura <= 0:
                    if daniel.armadura in daniel.inventario:
                        daniel.reparando_escudo()
                        if daniel.contador_de_armadura <= 0:
                            daniel.contador_de_armadura = 0
                        if daniel.contador_de_armadura == 0:
                            daniel.inventario.remove(daniel.armadura)
                            teste.som_armadura_quebrando()
                            print('\033[1m \033[31m o colete está quebrado \033[m')
                daniel.marcador_de_armadura = teste.escudo * daniel.contador_de_armadura

            def ataque_direto(self, numero_do_programa):
                while True:
                    numero = int(input('digite um número entre 0 e 12: '))
                    numero1 = int(input('digite um número entre 0 e 12: '))
                    if 0 <= numero <= 12 and 0 <= numero1 <= 12:
                        break
                    else:
                        print('\033[31m \033[1m apenas números entre 0 e 12. \033[m')
                print(f'{daniel.personagem_escolhido} está atacando demogorgon')
                daniel.som_do_personagem(daniel.personagem_escolhido)
                if numero or numero1 == numero_do_programa:
                    sleep(1)
                    print('\033[1m \033[32m INCRIVEL, golpe acertado em cheio \033[m')
                    sleep(1)
                    daniel.contador_de_fome += 5
                    daniel.contador_de_sede += 5
                    demogorgon.STATUS = False
                else:
                    sleep(1)
                    print(f'{daniel.personagem_escolhido} errou o golpe')
                    sleep(1)
                    print(f'iniciando batalha entre {daniel.personagem_escolhido} e demogorgon')
                    sleep(1)
                    daniel.contador_de_sede -= 3
                    daniel.contador_de_fome -= 3
            def bau_recompensa_demogorgon(self):
                print('\n')
                print('baú mágico a sua espera')
                sleep(2)
                daniel.mostrando_bau()
                print('abrindo báu')
                teste.som_abrindo_bau()
                list_itens_adicionados = []
                for item in demogorgon.bau:
                    list_itens_adicionados.append(item)
                    daniel.inventario.append(item)
                daniel.moeda += 30
                print(f'\033[32m \033[4m \033[1m {"itens adicionados: ".upper():^50} \033[m')
                sleep(1)
                for itens in list_itens_adicionados:
                    print(f'{itens.upper():^50}')
                    sleep(2)
                print(f'{"moedas".upper():^40}')
                print(f'\033[4m \033[1m \033[32m {"-" * len("itens adicionados"):^50} \033[m')
                print('\n \033[32m \033[1m fechando baú de recompensa do demogorgon \033[m')
                sleep(1)


            def personagem_jogando(self):
                self.dano_personagem = 0
                self.dado_personagem = ran(0, 12)
                self.adicional = 0
                print(f'{daniel.personagem_escolhido} está atacando demogorgon..')
                daniel.som_do_personagem(daniel.personagem_escolhido)
                if self.dado_personagem <= 1:
                    self.dano_personagem = 0
                    print(f'{demogorgon.nome} desviou do ataque')
                elif self.dado_personagem <= 3:
                    self.dano_personagem = 3
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano_personagem += 2
                        self.adicional = 2
                elif self.dado_personagem <= 6:
                    self.dano_personagem = 7
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano_personagem += 3
                        self.adicional = 3
                elif self.dado_personagem <= 9:
                    self.dano_personagem = 9
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano_personagem += 3
                        self.adicional = 3
                elif self.dado_personagem <= 12:
                    self.dano_personagem = 8
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano_personagem += 3
                        self.adicional = 3
                print(f'dano imposto por {daniel.personagem_escolhido}: {self.dano_personagem}')
                print(f'dano adcional: {self.adicional}')
                print()
                if daniel.acelerador_de_habilidade in daniel.inventario:
                    opcao = str(input('acelerador de habilidade pronto para ser usado, deseja usar? ')).lower()
                    if opcao == 'sim':
                        print('ativando acelerador de habilidade')
                        daniel.inventario.remove(daniel.acelerador_de_habilidade)
                        sleep(2)
                        print('acelerador de habilidade ativado')
                        self.contador_de_ativacao_de_habilidade -= 2
                    elif opcao == 'não' or opcao == 'nao':
                        print('recusando ativação do acelerador de habilidade')
                    else:
                        print('\033[31m \033[4m \033[1m digite apenas sim ou não \033[m')
                self.contador_de_ativacao_de_habilidade -= 1
                if self.contador_de_ativacao_de_habilidade <= 0:
                    print(f'habilidade especial de {daniel.personagem_escolhido} pronta para ser usada')
                    demogorgon.habilidade_especial()
                else:
                    print('habilidade especial carregando')
                demogorgon.contador_de_vida -= self.dano_personagem
                if demogorgon.contador_de_vida <= 0:
                    demogorgon.STATUS = False
                if daniel.contador_de_vida <= 0:
                    if daniel.nivel_de_escudo >= 2:
                        print('absorvendo dano para armadura, sacrificio de escudo')
                        daniel.contador_de_vida += 6
                        daniel.inventario.remove(daniel.armadura)
                        daniel.contador_de_armadura = 0
                    else:
                        daniel.STATUS = False

        demogorgon = CombateDemogorgon('demogorgon')
        if daniel.CONTADOR_DE_BATALHA_DEMOGORGON == 1:
            daniel.contador_de_armadura = daniel.contador_de_armadura
            sleep(1.4)
            print(f'{daniel.personagem_escolhido} avistou o demogorgon do outro lado da floresta invertida')
            sleep(1)
            teste.som_demogorgon_aparecendo()
            demogorgon.demogorgon_aparecendo()

            daniel.escolhendo_e_organizando_armaduras()
            sleep(1)
            while True:
                opcao = str(input('\033[1m deseja fazer um ataque direto ao demogorgon? \033[m')).lower()
                if opcao == 'sim':
                    demogorgon.ataque_direto(numero_do_programa=ran(0, 12))
                    break
                elif opcao == "não" or opcao == "nao":
                    print(f'inicando batalha entre {daniel.personagem_escolhido} e demogorgon')
                    break
                else:
                    print('\033[1m \033[31m responda apenas sim ou não cavalheiro \033[m')
            while True:
                if demogorgon.STATUS and daniel.STATUS == True:
                    demogorgon.mostrar_vida_demogorgon()
                    sleep(0.9)
                    demogorgon.demogorgon_jogando()
                    sleep(0.9)
                    demogorgon.personagem_jogando()
                    sleep(0.9)
                if demogorgon.STATUS == False and daniel.STATUS == False:
                    print(f'\033[1m \033[31m demogorgon e {daniel.personagem_escolhido} foram mortos em batalha\033[m')
                    break
                if demogorgon.STATUS == False and daniel.STATUS == True:
                    print(f'\033[1m \033[36m demogorgon derrotado por {daniel.personagem_escolhido}\033[m')
                    daniel.voz_final_sarcastica_do_personagem()
                    print(f'prepare-se para sua recompensa')
                    sleep(1)
                    daniel.contador_de_vida += 1
                    demogorgon.bau_recompensa_demogorgon()
                    break
                if demogorgon.STATUS == True and daniel.STATUS == False:
                    print(f'\033[1m \033[31m {daniel.personagem_escolhido} foi morto por demogorgon\033[m')

                    break
                daniel.casa = 42

            daniel.contador_de_sede -= 3
            daniel.contador_de_fome -= 3
            daniel.casa = 42
            executando_floresta_encantada()




    def rota3_alguma_coisa(self):
        pass
    def mostrando_inventario(self):
        print(f'\033[4m\033[35m \033[1m{"INVENTÁRIO":^50}\033[m')
        for itens in daniel.inventario:
            print(f'\033[1m{itens:^50}\033[m')
        print(f'\033[35m \033[1m {"_" * 50:^50}\033[m')
    def pocao_de_reviver(self):
        opcao = str(input('deseja utilizar sua poção de reviver para retornar ao jogo? ')).lower()
        if opcao == 'sim':
            daniel.STATUS = True
            daniel.contador_de_vida += 10
            daniel.inventario.remove(daniel.revivedor)
            daniel.casa -= 20
            executando_floresta_encantada()
        elif opcao == 'não' or opcao == 'nao':
            daniel.STATUS = False
            daniel.contador_de_vida = 0
        else:
            print('\033[1m \033[31m opção inválida, digite apenas sim ou não para tomar a poção de reviver \033[m')
            daniel.pocao_de_reviver()

    def fruta_envenenada(self):
        opcao = str(input('fruta mágica em sua frente, deseja gastar uma garrafa de àgua para molhar ela e ativar sua magia? ')).lower()
        while True:
            if opcao == 'sim':
                if self.garrafa_de_agua in daniel.inventario:
                    print('regando fruta mágica')
                    sleep(1)
                    daniel.inventario.remove(daniel.garrafa_de_agua)
                    print('comendo fruta mágica..')
                    sleep(1)
                    break
                else:
                    while True:
                        opcao_mercado = str(input('você não têm a garrafa de àgua para molhar a fruta mágica, deseja comprar a garrafa no mercado? ')).lower()
                        if opcao_mercado == 'sim':
                            daniel.mercadinho()
                            break

                        elif opcao_mercado == 'não' or opcao_mercado == 'nao':
                            print()
                            break
                        else:
                            print('\033[31m \033[1m apenas sim ou não \033[1m')
                    break
            elif opcao == 'não' or opcao == 'nao':
                print('deixando fruta mágica para trás')
                sleep(1)
                break
            else:
                print('\033[31m \033[1m digite apenas sim ou não \033[m')
        list_opcao_fruta = ['envenenada', 'não envenenada']
        opcao_fruta = choice(list_opcao_fruta)
        if opcao == 'sim':
            if opcao_fruta == 'envenenada':
                self.contador_de_vida -= 4
                print('a fruta estava envenenada')
            elif opcao_fruta == 'não envenenada':
                print('a fruta mágica lhe alimentou')
                self.contador_de_fome += 4
                self.contador_de_sede += 2
            else:
                print()


daniel = PrimeiraParte('castiel')

def executando_floresta_encantada():
    #executando floresta encantada
    print()
    if daniel.casa == 0:
        print(f'{"mostrando manual do jogo, LEIA".upper():^100}')
        sleep(2)
        daniel.manual()
        sleep(1)
        print('''amostra de personagens
    aperte em fechar para continuar: ''')
        sleep(1.2)
        print('primeiro personagem: ')
        daniel.personagem01()
        print('segundo personagem: ')
        daniel.personagem02()
        print('terceiro personagem: ')
        daniel.personagem03()
        daniel.escolha_de_personagem()
        a = 'inicializando floresta encantada'.upper()
        print(f'\033[36m \033[1m {a}\033[m')
        daniel.primeira_parte_floresta()
        daniel.leitura_em_voz()
    while True:
        if daniel.casa >= 100:
            break
        elif daniel.contador_de_vida <= 0:
            daniel.STATUS = False
            if daniel.STATUS == False:
                break
        def inicializando_jogo(iniciar):
            if daniel.casa < 100:
                if iniciar == 'mercado':
                    daniel.list_itens_comprados = []
                    daniel.mercadinho()
                elif iniciar == 'mochila':
                    daniel.mostrando_inventario()
                elif iniciar == 'troca':
                    daniel.troca_de_item_por_moeda()
                elif iniciar == 'cristal':
                    daniel.inimigos_proximos_pelo_cristal()
                elif iniciar == 'upar armadura':
                    daniel.upar_armadura()
                elif iniciar != '':
                    print('\033[31maperte apenas enter cavalheiro\033[m')
                elif iniciar == '':
                    valor = ran(1, 6)
                    print(f'prepare {daniel.personagem_escolhido} para andar:\033[34m {valor} casas \033[m')
                    daniel.pulando_casas(valor)
                    daniel.mostrar_casa()
        if daniel.casa < 100:
            inicializando_jogo(iniciar=str(input(f'\naperte enter cavalheiro: ')).lower())
    if daniel.STATUS == True:
        print(f'\033[33m {"parabêns sobrevivente, ultrapassou a floresta encantada":^40}\033[m')

executando_floresta_encantada()

if daniel.contador_de_vida <= 0:
    if daniel.revivedor in daniel.inventario:
        print('\033[1m \033[31m vida zerada \033[m')
        daniel.pocao_de_reviver()
if daniel.STATUS == False:
    teste.som_game_over()
    print(f'\033[31m \033[1m \033[2m {"GAME ENCERRADO, VIDA DO PERSONAGEM ZERADA":^100}\033[m')

# #começando segunda parte - deserto de sangue
# class SegundaParte(PrimeiraParte):
#     def __init__(self, nome):
#         self.nome = nome
#         self.casa = 0
#         self.portal = 0
#         self.vida = 200
#         self.contador_de_fome = 8
#         self.contador_de_sede = 8
#         self.contador_de_vida = 8
#         self.garrafa_de_agua = 'garrafa de àgua'
#         self.carne = 'carne'
#         self.aditivo_de_cura = 'aditivo de cura'
#         self.arma = 'arma'
#         self.moeda = 50
#         self.inventario = [self.garrafa_de_agua, self.carne, self.aditivo_de_cura]
#         self.mercado = {self.garrafa_de_agua: 10, self.carne: 10, self.aditivo_de_cura: 15, self.arma: 20}
#         self.list_itens_comprados = []
#     def pulando_casas(self, valor):
#         self.casa += valor
#         self.contador_de_fome -= 1
#         self.contador_de_sede -= 1
#         if self.contador_de_fome <= 0:
#             self.contador_de_fome = 0
#             if self.contador_de_fome == 0:
#                 daniel.alimentar()
#                 self.contador_de_vida -= 1
#         if self.contador_de_sede <= 0:
#             self.contador_de_sede = 0
#             if self.contador_de_sede == 0:
#                 daniel.beber_agua()
#                 self.contador_de_vida -= 1
#         if self.contador_de_vida <= 2:
#             daniel.recuperar_vida()
#
#     def segunda_parte_deserto(self):
#         enunciado = 'bem vindo ao deserto de sangue, prepare-se para o perigo e a seca'.upper()
#         print(f'\033[33m{enunciado:^100}\033[m')
#
#
# if daniel.contador_de_vida > 0:
#     daniel = SegundaParte('castiel')
#     daniel.casa = 0
#     if daniel.casa == 0:
#         daniel.segunda_parte_deserto()
#     while True:
#         if daniel.casa >= 100 or daniel.contador_de_vida <= 0:
#             break
#
#         def inicializando_jogo(iniciar):
#             if iniciar != '':
#                 print('\033[31m \033[1maperte apenas enter cavalheiro\033[m')
#             elif iniciar == '':
#                 valor = ran(1, 6)
#                 print(f'prepare-se para andar:\033[34m {valor} casas \033[m')
#                 daniel.pulando_casas(valor)
#                 if daniel.casa <= 100:
#                     daniel.mostrar_casa()
#         if daniel.casa <= 100:
#             inicializando_jogo(iniciar=str(input(f'aperte enter cavalheiro: ')))
#     if daniel.contador_de_vida <= 0:
#         if daniel.revivedor in daniel.inventario:
#             daniel.pocao_de_reviver()
#         else:
#             teste.som_game_over()
#             print(f'\033[31m \033[1m \033[2m {"GAME ENCERRADO, VIDA DO PERSONAGEM ZERADA":^100}\033[m')
#     else:
#         print(f'\033[33m{"parabêns sobrevivente, ultrapassou o deserto de sangue, encerrado":^70}\033[m')
# elif daniel.contador_de_vida <= 0:
#     if daniel.revivedor in daniel.inventario:
#         print('\033[1m \033[31m vida zerada \033[m')
#         daniel.pocao_de_reviver()
#     else:
#         teste.som_game_over()
#         print(f'\033[31m \033[1m \033[2m {"GAME ENCERRADO, VIDA DO PERSONAGEM ZERADA":^100}\033[m')
#




