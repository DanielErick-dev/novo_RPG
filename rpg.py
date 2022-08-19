from random import randint as ran
import teste
from teste import alimentos
from time import sleep
import gtts
from playsound import playsound
import pyttsx3
import pygame
pygame.init()

class PrimeiraParte(Exception):
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
            |  a função do cristal é atentar o jogador de determinado oponente que ele enfrentará durante o caminho, para usar escreva|
            |    'cristal' no 'aperte enter cavalheiro' lembrando, o cristal nao começará no seu estoque inicial. obtenha-o           |
            |                                                                                                                         |
            ---------------------------------------------------------------------------------------------------------------------------
        ''')

    def __init__(self, nome):
        self.casa = 0
        self.nome = nome
        self.portal = 0
        self.contador_de_fome = 8
        self.contador_de_sede = 8
        self.contador_de_vida = 20
        self.garrafa_de_agua = 'garrafa de àgua'
        self.carne = 'carne          '
        self.aditivo_de_cura = 'aditivo de cura'
        self.arma = 'arma           '
        self.moeda = 50
        self.cristal = 'cristal        '
        self.inventario = [self.garrafa_de_agua, self.carne, self.aditivo_de_cura]
        self.revivedor = 'revivedor      '
        self.escudo1 = 'escudo1        '
        self.escudo2 = 'escudo2        '
        self.escudo3 = 'escudo3        '
        self.mercado = {self.garrafa_de_agua: 10, self.carne: 10, self.aditivo_de_cura: 15, self.arma: 20, self.cristal: 25, self.revivedor: 30, self.escudo1: 5, self.escudo2:20, self.escudo3: 40}
        self.list_itens_comprados = []
        self.personagem_escolhido = ''
        self.CONTADOR_DE_BATALHA_DEMOGORGON = 0
        self.STATUS = True
        self.armadura = 'armadura'
        self.escudo_escolhido = [self.escudo1, self.escudo2, self.escudo3]



    def escolha_de_personagem(self):
        print('''\npersonagem 01 - andrey - caçador assassino
personagem 02 - arfrid - arqueira 
personagem 03 - geralt - bruxo''')
        while True:
            escolha = str(input('escreva o nome do personagem que você deseja: ')).lower()
            if escolha == 'andrey':
                self.personagem_escolhido = 'andrey'
                break
            elif escolha == 'arfrid':
                self.personagem_escolhido = 'arfrid'
                break
            elif escolha == 'geralt':
                self.personagem_escolhido = 'geralt'
                break
            else:
                print('\033[31mopção de personagem inválida\033[m')
        print(F'personagem escolhido: {self.personagem_escolhido}')
        sleep(3)
    def mercadinho(self):
        print(f'\033[35m \033[1m{"BEM VINDO AO MERCADINHO MÁGICO":^50}\033[m')
        self.codigo_agua = '245'
        self.codigo_carne = '103'
        self.codigo_pocao = '205'
        self.codigo_arma = '934'
        self.codigo_cristal = '534'
        self.codigo_revivedor = '890'
        self.codigo_escudo1 = '387'
        self.codigo_escudo2 = '496'
        self.codigo_escudo3 = '052'
        self.list_de_codigo = [self.codigo_agua, self.codigo_carne, self.codigo_pocao, self.codigo_arma, self.codigo_cristal, self.codigo_revivedor, self.codigo_escudo1, self.codigo_escudo2, self.codigo_escudo3 ]
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
    def escolhendo_e_organizando_escudos(self):
        self.contador_de_escudo1 = 3
        self.contador_de_escudo2 = 5
        self.contador_de_escudo3 = 7
        self.escudo_escolhido = ''
        if daniel.escudo1 or daniel.escudo2 or daniel.escudo3 in daniel.inventario:
            self.marcador_de_escudo = ''
            while True:
                opcao = str(input('deseja utilizar seu escudo? ')).lower()

                if opcao == 'sim':
                    daniel.mostrando_inventario()
                    option = str(input('qual escudo voçê deseja utilizar? ')).lower()
                    if option == 'escudo1':
                        if daniel.escudo1 in daniel.inventario:
                            print('equipando escudo de nivel 1')
                            daniel.escudo_escolhido = daniel.escudo1
                            daniel.marcador_de_escudo = daniel.contador_de_escudo1 * teste.escudo1
                            break
                        else:
                            print(f'escudo não encontrado no inventário de {daniel.personagem_escolhido}')
                    elif option == 'escudo2':
                        if daniel.escudo2 in daniel.inventario:
                            print('equipando escudo de nivel 2')
                            daniel.escudo_escolhido = daniel.escudo2
                            daniel.marcador_de_escudo = daniel.contador_de_escudo2 * teste.escudo2
                            break
                        else:
                            print(f'escudo não encontrado no inventário de {daniel.personagem_escolhido}')

                    elif option == 'escudo3':
                        if daniel.escudo3 in daniel.inventario:
                            print('equipando escudo de nivel 3')
                            daniel.escudo_escolhido = daniel.escudo3
                            daniel.marcador_de_escudo = daniel.contador_de_escudo3 * teste.escudo3
                            break
                        else:
                            print(f'escudo não encontrado no inventário de {daniel.personagem_escolhido}')
                    else:
                        print('\033[31m \033[1m             digite apenas escudo1 escudo2 ou escudo3 sem separar a letra do número, tente novamente \033[m')



                elif opcao == 'não' or opcao == 'nao':
                    if daniel.personagem_escolhido == 'arfrid':
                        print(f'inutilização de escudos,{daniel.personagem_escolhido} está desprotegida')
                        break
                    else:
                        print(f'inutilização de escudos,{daniel.personagem_escolhido} está desprotegido')
                        break
                else:
                    print('\033[31m \033[1m apenas sim ou não \033[m')
                    daniel.escolhendo_e_organizando_escudos()

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

        elif codigo == self.codigo_escudo1:
            if self.moeda >= self.mercado[self.escudo1]:
                self.moeda -= self.mercado[self.escudo1]
                self.inventario.append(self.escudo1)
                self.list_itens_comprados.append(self.escudo1)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o escudo nivel 1')
        elif codigo == self.codigo_escudo2:
            if self.moeda >= self.mercado[self.escudo2]:
                self.moeda -= self.mercado[self.escudo2]
                self.inventario.append(self.escudo2)
                self.list_itens_comprados.append(self.escudo2)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o escudo nivel 2')
        elif codigo == self.codigo_escudo3:
            if self.moeda >= self.mercado[self.escudo3]:
                self.moeda -= self.mercado[self.escudo3]
                self.inventario.append(self.escudo3)
                self.list_itens_comprados.append(self.escudo3)
                print('item comprado')
            else:
                print('quantidade de moedas insuficiente para comprar o escudo nivel 3')
        else:
            print('\033[31m \0331m               código inserido não corresponde a nenhum produto do mercado mágico \033[m')
            daniel.compra_no_mercado()
        while True:
            opcao = str(input('deseja comprar mais alguma coisa do mercado mágico? ')).lower()
            if opcao == 'sim':
                daniel.compra_no_mercado()
                break
            elif opcao in 'nãonao':
                daniel.mostrando_items_comprados()
                print(f'\n \033[31m {"fechando mercado mágico":^60}\033[m')
                break
            else:
                print('\033[31m \033[1m    opção inválida, apenas sim ou não cavalheiro  \033[m')
    def mostrando_items_comprados(self):
        print(f'\033[33m \033[1m{"items comprados:":^80} \033[m')
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
        elif 50 > self.casa >= 40:
            self.CONTADOR_DE_BATALHA_DEMOGORGON += 1
            if self.CONTADOR_DE_BATALHA_DEMOGORGON == 1:
                daniel.rota2_floresta_invertida()

    def leitura_em_voz(self):
        with open('lendoflorestaencantada.py', 'r') as arquivo:
            for linha in arquivo:
                frase = gtts.gTTS(linha, lang='pt-br')
                frase.save('frase.mp3')
                playsound('frase.mp3')

    def alimentar(self):
        opcao = str(input('deseja comer? ')).lower()
        if opcao == 'sim':
            if self.carne in daniel.inventario:
                self.marcador_de_fome += alimentos.carne_para_comer
                self.contador_de_fome += alimentos.quantidade_de_carne
                daniel.inventario.remove(self.carne)
                print(f'aguarde, {self.personagem_escolhido} está se alimentando')
                teste.som_de_comer()
            else:
                print(f'alimento não encontrado na mochila de {self.personagem_escolhido}, obtenha seus recursos')
    def beber_agua(self):
        opcao = str(input('deseja beber àgua? ')).lower()
        if opcao == 'sim':
            if self.garrafa_de_agua in daniel.inventario:
                self.marcador_de_sede += alimentos.garrafa_de_agua_para_beber
                self.contador_de_sede += alimentos.quantidade_de_agua
                daniel.inventario.remove(self.garrafa_de_agua)
                print(f'aguarde, {self.personagem_escolhido} está se hidratando')
                teste.som_de_beber()
            else:
                print(f'garrafa de àgua não encontrada na mochila de {self.personagem_escolhido}, obtenha seus recursos')

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
    def casa33(self):
        self.casa -= 10
        print('\033[1mcaminho bloqueado por montanha, dê a volta pela encosta\033[m')
    def casa55(self):
        print(f'\033[1m monstros a sua espreita, volte 8 casas\033[m')
        self.casa -= 8

    def casa11(self):
        print(f'\033[1m achou um atalho da floresta encantada, avançe 9 casas')
        self.casa += 9

    # PORTAIS
    def portal1(self):
        print(f'\033[32m\033[1m                 encontrou o primeiro portal da floresta encantada, viaje entre as dimensões para a casa 38\033[m ')
        self.casa = 38
    def portal2(self):
        print(f'\033[32m \033[1m                encontrou o segundo portal da floresta encantada, viaje entre as dimensões para a casa 71\033[m ')
        self.casa = 39
    def portal3(self):
        print(f'\033[32m \033[1m                encontrou o terceiro portal da floresta encantada, viaje entre as dimensões para a casa 90\033[m ')
        self.casa = 90
    def recompensa_por_2_portais(self):
        print(f'brilhante {self.nome}, viajou entre 2 portais na floresta encantada, aproveite em breve sua recompensa de sorte')

    def primeira_parte_floresta(self, valor=0):
        floresta_encantada = 'voçê está na primeira parte de sua jornada, entre na floresta encantada'.upper()
        print(f'\033[32m\033[4m \033[1m {floresta_encantada:^100}\033[m')


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
    def casa86(self):
        print('\033[1mcomeu fruto envenenado, se recupere cavalheiro\033[m')
        self.casa -= 2
        self.contador_de_sede -= 3
        self.contador_de_fome -= 3
        self.contador_de_vida -= 3

    # ROTAS ALTERNATIVAS
    def rota1_caverna(self):
        pass



    def rota2_floresta_invertida(self):
        class CombateDemogorgon():
            def __init__(self, nome):
                self.nome = nome
                self.vida = None
                self.contador_de_vida = 30
                self.barra_de_vida_demogorgon = teste.barra_de_vida_demogorgon
                self.STATUS = True
                self.bau = [daniel.garrafa_de_agua, daniel.carne, daniel.aditivo_de_cura, daniel.armadura]

            def som_demogorgon_atacando(self):
                playsound('somdemogorgon_atacando.mp3')
            def narrando_demogorgon(self):
                falar = pyttsx3.init('sapi5')
                frase = str('demogórgon aproxima-se')
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
                print(f'\033[31m \033[1m{"VIDA DEMOGORGON":^40} ', end ='  ')
                print(f'\033[34m \033[1m{"VIDA PERSONAGEM":^40}  ', end='  ')
                print(f'\033[33m \033[1m{"ESCUDO":^40}')
                print(f'\033[31m \033[1m{self.vida_demogorgon:^40} ', end='  ')
                print(f'\033[34m \033[1m{daniel.marcador_de_vida:^40}\033[m', end='  ')
                if daniel.escudo1 or daniel.escudo2 or daniel.escudo3 in daniel.inventario:
                    print(f'\033[1m {daniel.marcador_de_escudo:^40}\033[m')
                else:
                    print('')

            def demogorgon_jogando(self):
                self.dano = 0
                self.dado_demogorgon = ran(0, 12)
                print('demogorgon atacando..')
                demogorgon.som_demogorgon_atacando()
                if self.dado_demogorgon <= 1:
                    self.dano = 0
                    print(f'{daniel.personagem_escolhido} desviou do ataque')
                elif self.dado_demogorgon <= 3:
                    self.dano = 4
                elif self.dado_demogorgon <= 6:
                    self.dano = 6
                elif self.dado_demogorgon <= 9:
                    self.dano = 4
                elif self.dado_demogorgon <= 12:
                    self.dano = 2
                print(f'dano imposto por demogorgon: {self.dano}')
                print()
                daniel.contador_de_vida -= self.dano
                if daniel.contador_de_vida <= 0:
                    daniel.STATUS = False
                if demogorgon.STATUS <= 0:
                    demogorgon.STATUS = False

            def ataque_direto(self, numero_do_programa):
                while True:
                    numero = int(input('digite um número entre 0 e 12: '))
                    if 0 <= numero <= 12:
                        break
                    else:
                        print('\033[31m \033[1m apenas números entre 0 e 12. \033[m')
                print(f'{daniel.personagem_escolhido} está atacando demogorgon')
                daniel.som_do_personagem(daniel.personagem_escolhido)
                if numero == numero_do_programa:
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
                print('baú mágico a sua espera')
                sleep(2)
                daniel.mostrando_bau()
                list_itens_adicionados = []
                while True:
                    opcao = str(input('\naperte enter para abrir o baú. ')).lower()
                    if opcao == '':
                        sleep(1)
                        print('\033[1m \033[4m \033[36m baú mágico sendo aberto.. \033[m')
                        teste.som_abrindo_bau()
                        break
                    else:
                        print(f'\033[31m \033[1m aperte apenas enter cavalheiro \033[m')
                for item in demogorgon.bau:
                    list_itens_adicionados.append(item)
                    daniel.inventario.append(item)
                daniel.moeda += 30
                sleep(1)
                print(f'\033[32m \033[4m \033[1m {"itens adicionados: ".upper():^50} \033[m')
                sleep(1)
                for itens in list_itens_adicionados:
                    print(f'{itens.upper():^50}')
                    sleep(1.2)
                print(f'{"moedas".upper():^50}')
                print(f'\033[4m \033[1m \033[32m {"-" * 50:^50} \033[m')
                print('\n fechando baú de recompensa do demogorgon')
                sleep(1)



            def personagem_jogando(self):
                self.dano = 0
                self.dado_personagem = ran(0, 12)
                self.adicional = 0
                print(f'{daniel.personagem_escolhido} está atacando demogorgon..')
                daniel.som_do_personagem(daniel.personagem_escolhido)
                if self.dado_demogorgon <= 1:
                    self.dano = 0
                    print(f'{demogorgon.nome} desviou do ataque')
                elif self.dado_personagem <= 3:
                    self.dano = 3
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano += 2
                        self.adicional = 2
                elif self.dado_personagem <= 6:
                    self.dano = 7
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano += 3
                        self.adicional = 3
                elif self.dado_personagem <= 9:
                    self.dano = 10
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano += 3
                        self.adicional = 3
                elif self.dado_personagem <= 12:
                    self.dano = 9
                    if daniel.personagem_escolhido == 'geralt':
                        self.dano += 4
                        self.adicional = 4
                print(f'dano imposto por {daniel.personagem_escolhido}: {self.dano}')
                print(f'dano adcional: {self.adicional}')
                print()
                demogorgon.contador_de_vida -= self.dano
                if demogorgon.contador_de_vida <= 0:
                    demogorgon.STATUS = False
                if daniel.contador_de_vida <= 0:
                    daniel.STATUS = False

        demogorgon = CombateDemogorgon('demogorgon')
        if daniel.CONTADOR_DE_BATALHA_DEMOGORGON == 1:
            sleep(1.4)
            print(f'{daniel.personagem_escolhido} avistou o demogorgon do outro lado da floresta invertida')
            sleep(1)
            demogorgon.demogorgon_aparecendo()
            daniel.escolhendo_e_organizando_escudos()
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


    def rota3_alguma_coisa(self):
        pass
    def mostrando_inventario(self):
        print(f'\033[4m\033[35m \033[1m{"INVENTÁRIO":^50}\033[m')
        for itens in daniel.inventario:
            print(f'\033[1m{itens:^50}\033[m')
        print(f'\033[35m \033[1m {"_" * 50:^50}\033[m')
    def pocao_de_reviver(self):
        opcao = str(input('deseja utilizar sua poção de reviver para retornar ao jogo? '))
        if opcao == 'sim':
            daniel.STATUS = True
            daniel.contador_de_vida += 10
            daniel.inventario.remove(daniel.revivedor)
            daniel.casa -= 20
            executando_floresta_encantada()
        else:
            daniel.STATUS = False
            daniel.contador_de_vida = 0



daniel = PrimeiraParte('castiel')

def executando_floresta_encantada():
    #executando floresta encantada
    print()
    if daniel.casa == 0:
        print(f'{"mostrando manual do jogo, LEIA".upper():^100}')
        sleep(2)
        daniel.manual()
        sleep(5)
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
                elif iniciar == 'cristal':
                    daniel.inimigos_proximos_pelo_cristal()
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
    else:
        teste.som_game_over()
        print(f'\033[31m \033[1m \033[2m {"GAME ENCERRADO, VIDA DO PERSONAGEM ZERADA":^100}\033[m')
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




