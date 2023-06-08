#class CirculoPerfeito:
  #  def mostra_cor(self):
    #    return id(self)


#circulo_primeiro = CirculoPerfeito()
#circulo_segundo = CirculoPerfeito()

#print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
#print(id(circulo_segundo), circulo_segundo.mostra_cor())


#print(circulo_primeiro is circulo_segundo)


# class CirculoPerfeito:
#    def __init__(self):
#        self.cor = 'vermelho'
#        self.circunferencia = 4
#        self.material = 'papel'
#
#    def mostra_cor(self):
#        return self.cor
#
#
#    def trocar_cor(self, cor):
#        self.cor = cor


#circulo_primeiro = CirculoPerfeito()
#circulo_segundo = CirculoPerfeito()

#circulo_segundo.trocar_cor('rosa')
#print(f'{circulo_primeiro.cor}\n{circulo_segundo.cor}')
#circulo_primeiro.trocar_cor('azulado')
#print(circulo_primeiro.cor)



# class ControleRemoto:
#     def __init__(self, cor, altura, largura, profundidade, material):
#         self.cor = cor
#         self.altura = altura
#         self.largura = largura
#         self.profundidade = profundidade
#         self.material = material
#
#     def mostrar_canal(self, botão):
#         if botão == '+':
#             print('aumentando volume')
#         if botão == '-':
#             print('diminuindo volume')
#
# controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm', 'plástico')
# controle_remoto.cor = 'branco'
#
# controle_remoto02 = ControleRemoto('cinza', '10cm', '2cm', '2cm', 'plástico')
# print(f'a cor do primeiro controle remoto é: {controle_remoto.cor}')
# print(f'a cor do segundo controle remoto é: {controle_remoto02.cor}')


# email = str(input('digite seu email: '))
# nome = str(input('digite seu nome: '))
# VAMOS CRIAR UMA CLASSE PARA CLIENTES DA NETFLIX

# class Cliente:
#     def __init__(self, nome, email, plano):
#         self.nome = nome
#         self.email = email
#         self.lista_de_planos = ['basic', 'intermediario', 'premium']
#         if plano in self.lista_de_planos:
#             self.plano = plano
#         else:
#             raise Exception('plano inválido')
#
#     def mudar_de_plano(self, novo_plano):
#         if novo_plano in self.lista_de_planos:
#             self.plano = novo_plano
#         else:
#             raise Exception('novo plano inválido')
#
#
#
#     def ver_filme(self, filme, plano_filme):
#         if self.plano == plano_filme:
#             print(f'ver filme: {filme}')
#         elif self.plano == 'premium':
#             print(f'ver filme: {filme}')
#         elif self.plano == 'basic' and plano_filme == 'premium':
#             print(f'filme: {filme} indisponivel para assinantes basic')
#
#         else:
#             print('plano inválido')
#
#
#
#
# cliente = Cliente('Lira', 'Lira@gmail.com', 'basic')
# cliente.ver_filme('harry potter', 'premium')
# cliente.mudar_de_plano('premium')
# cliente.ver_filme('harry potter', 'premium')



#classe modelando quadrado
# class Quadrado:
#     def __init__(self, tamanhol):
#         self.tamanhol = tamanhol
#
#
#     def mudar_valor_do_lado(self):
#         mudar = int(input('qual novo tamanho do lado: '))
#         self.tamanhol = mudar
#
#
#
#     def retornar_valor_do_lado(self):
#         print(f'o lado do quadrado mede: {self.tamanhol}m ',end='')
#         area = self.tamanhol ** 2
#         print(f'e a área vale: {area}m²')
#
#
#
# quadrado01 = Quadrado(60)
#
#
#
# quadrado01.mudar_valor_do_lado()
# quadrado01.retornar_valor_do_lado()



#modelando retângulo

# class Retangulo:
#     def __init__(self):
#         self.comprimento = float(input('comprimento:  '))
#         self.largura = float(input('largura: '))
#
#
#     def retornar_lados(self):
#         print(f'''os lados valem:
# comprimento: {self.comprimento}m
# largura: {self.largura}m''')
#
#
#     def mudar_lados(self):
#         self.comprimento = float(input('novo comprimento: '))
#         self.largura = float(input('nova largura: '))
#
#
#
#     def area_do_retangulo(self):
#         self.area = self.comprimento * self.largura
#         return self.area
#
#
#     def perimetro_do_retangulo(self):
#         self.perimetro = self.comprimento + self.largura
#         return self.perimetro
#
# retangulo = Retangulo()
#
# resp = str(input('deseja alterar os valores? [S/N]? ')).upper()[0]
# if resp == 'S':
#     retangulo.mudar_lados()
#     mostrar = str(input('deseja mostrar os lados? ')).upper()[0]
#     if mostrar == 'S':
#         retangulo.retornar_lados()
#
# else:
#     area = retangulo.area_do_retangulo()
#     perimetro = retangulo.perimetro_do_retangulo()
#     lista = [area, perimetro]
#     newlist = []
#     for valores in lista:
#         valores = f'{valores:.0f}'
#         newlist.append(str(valores))
#     with open('retornando medidas do retangulo.txt.py', 'w') as retorno:
#       retorno.writelines(f'a area vale: {newlist[0]}')
#       retorno.writelines('\n')
#       retorno.writelines(f'o perimetro vale: {newlist[1]}')



# class Pessoa:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura
#
#     def mostrar_valores(self):
#         print(f'nome é: {self.nome}\nidade é: {self.idade} anos\npeso é: {self.peso}kg\naltura é: {self.altura}cm')
#
#     def envelhecer(self):
#         while self.idade < 21:
#             self.altura += 1
#             self.idade += 1
#         print(f'idade = {self.idade} anos  and altura = {self.altura}cm')
# daniel = Pessoa('daniel', 18, 70, 170)
# daniel.mostrar_valores()
# daniel.envelhecer()





# from time import sleep
# class ContaCorrente:
#     def __init__(self, numero, nome, saldo='0'):
#         self.numero = numero
#         self.nome = nome
#         if saldo.isnumeric():
#             self.saldo = int(saldo)
#         else:
#             self.saldo = 0
#
#
#     def mostrar_valores(self):
#         print(f'nome: {self.nome}\nconta: {self.numero}\nsaldo: {self.saldo} reais')
#
#
#
#     def alterar_nome(self, newname):
#        if self.nome == newname:
#             print('novo nome digitado é igual ao anterior, digite novamente: ')
#             while True:
#                 novo_nome = str(input('digite um novo nome: ')).capitalize()
#                 if novo_nome != self.nome:
#                     break
#
#             self.nome = novo_nome
#             print(f'novo nome é: {self.nome}')
#
#
#     def depositar(self, deposito):
#         self.saldo += deposito
#         print(f'seu novo saldo é: {self.saldo}')
#
#
#
#     def saque(self, valor_do_saque):
#         if valor_do_saque > self.saldo:
#             print(f'ERRO, SALDO INDISPONIVEL PARA ESSA QUANTIA DE DINHEIRO')
#         else:
#             print('sacando seu dinheiro....')
#             sleep(1)
#             print('aguarde')
#             sleep(1)
#             print(f'valor sacado: {valor_do_saque} reais')
#             print(f'saldo atual: {self.saldo - valor_do_saque} reais')
#
# conta01 = ContaCorrente(str(input('número da conta: ')), str(input('nome: ')).capitalize(), str(input('saldo: ')))
# conta01.mostrar_valores()
# conta01.depositar(int(input(f'digite quanto deseja depositar:  ')))
# conta01.saque(int(input('digite quanto deseja sacar: ')))






# print(F'{"->"*20}SIMULADOR DE TELEVISÃO{"->"*20}')
#
# class Televisao():
#     def __init__(self, numero, volume):
#         if 0 < numero <= 50:
#             self.numero = numero
#         else:
#             self.numero = 'indisponivel'
#         if 0 <= volume <= 100:
#             self.volume = volume
#             print(f'volume: {self.volume}')
#         else:
#             self.volume = 'volume indisponivel'
#             print(volume)
#
#
#
#     def mostrar_canal(self):
#         print(f'canal: {self.numero}')
#
#
#
#     def mudar_de_canal(self):
#         new_canal = int(input('qual canal: '))
#         if 0 < new_canal <= 50:
#             self.numero = new_canal
#             print(f'canal: {self.numero}')
#         else:
#             self.numero = 'indisponivel'
#             print(self.numero)
#
#     def aumentar_volume(self):
#         volume = int(input('quanto voce deseja aumentar o volume: '))
#         self.volume += volume
#         if self.volume >= 0 and self.volume <= 100:
#             print(f'volume: {self.volume}')
#         else:
#             self.volume = 0
#             print(f'volume: volume inválido')
#
#
#
#     def diminuir_volume(self):
#         volume = int(input('quanto deseja diminuir o volume: '))
#         self.volume -= volume
#         if self.volume >=0 and self.volume <= 100:
#             self.volume = volume
#             print(f'volume: {self.volume}')
#         else:
#             self.volume = 0
#             print(f'volume: volume inválido')
#
#
#
#
# televisao01 = Televisao(int(input('digite o número do canal entre os 50 canais disponiveis: ')), int(input('volume entre 0 e 100: ')))
#
# while True:
#     print('''opções:
# [a] mostrar o canal
# [b] trocar de canal
# [c] aumentar volume
# [d] diminuir volume
# [e] desligar televisão
#     ''')
#     opção = str(input('qual sua opção? ')).lower()
#     if opção == 'a':
#         televisao01.mostrar_canal()
#     elif opção == 'b':
#         televisao01.mudar_de_canal()
#     elif opção == 'c':
#         televisao01.aumentar_volume()
#     elif opção == 'd':
#         televisao01.diminuir_volume()
#     elif opção == 'e':
#         print('desligando televisão')
#         break
#
#
# print('televisão desligada')



# from time import sleep
# class Tamagashi:
#     def __init__(self, nome, fome, saude, idade):
#         self.nome = nome
#         self.fome = fome
#         self.saude = saude
#         self.idade = idade
#         if self.fome > 50 and self.saude > 50:
#             self.humor = 'feliz'
#         elif self.fome < 50 and self.saude < 50:
#             self.humor = 'triste'
#         elif self.fome == 50 and self.saude == 50:
#             self.humor = 'normal'
#         elif self.fome < 50 or self.saude < 50:
#             self.humor = 'normal'
#
#
#     def retornar_valores(self):
#         print(f'nome: {self.nome}\nfome: {self.fome}%\nsaúde: {self.saude}%\nidade: {self.idade} anos\nhumor: {self.humor}')
#
#
#     def alterar_nome(self, nome):
#         self.nome = nome
#
#
#     def alterar_fome(self,fome):
#         self.fome = fome
#
#
#     def alterar_saude(self,saude ):
#         self.saude = saude
#
#
#     def alterar_idade(self,idade):
#         self.idade = idade
#
#
# tamagashi01 = Tamagashi(str(input('nome: ')), int(input('fome entre 0 e 100: ')), int(input('saúde entre 0 e 100: ')), int(input('idade: ')))
#
# def trocar_valores():
#     tamagashi01.alterar_nome(str(input('digite o novo nome: ')))
#     tamagashi01.alterar_idade(int(input('nova idade: ')))
#     tamagashi01.alterar_fome(int(input('nova fome entre 0 e 100: ')))
#     tamagashi01.alterar_saude(int(input('nova saúde entre 0 e 100: ')))
#
#
# resp = str(input('deseja alterar valores? ')).strip().upper()[0]
# if resp == 'S':
#     print(f'alterando valores do {tamagashi01.nome}')
#     sleep(3)
#     trocar_valores()
#     print('retornando valores...')
#     sleep(3)
#
#     tamagashi01.retornar_valores()
# else:
#     print('retornando valores...')
#     sleep(3)
#     tamagashi01.retornar_valores()





# from time import sleep
# def pular_linha():
#     print('->'*50)
#
# class Macaco:
#     def __init__(self, nome, estomago):
#         self.nome = nome
#         self.tedio = ['pouco tédio', 'tédio mediano', 'muito tédio']
#         if 0 <= estomago <= 1000:
#             self.estomago = estomago
#         elif estomago < 0:
#             self.estomago = estomago * -1
#         else:
#             print('calorias acima do limite')
#             self.estomago = 0
#
#
#
#     def comer(self, calorias):
#         print('hmmm ingerindo calorias...')
#         sleep(1)
#         if self.estomago + calorias <= 1000:
#             self.estomago += calorias
#         elif self.estomago + calorias > 1000:
#             print('calorias acima do limite, não consigo comer')
#
#
#
#
#     def ver_estomago(self):
#         sleep(1)
#         if self.estomago > 1000:
#             print('passou do limite do meu estomago, não aceito')
#         else:
#             print(f'o estomago de {self.nome} está com {self.estomago} calorias')
#             if self.estomago > 500:
#                 print('estou satisfeito')
#             elif self.estomago > 900:
#                 print('estou cheio')
#             elif self.estomago > 300:
#                 print('forrou meu estômago')
#             elif self.estomago < 100 and self.estomago != 0:
#                 print('estou com muita fome')
#
#     def canibalismo(self, macaco):
#         print('ingerindo meu amigo...')
#         sleep(5)
#         self.estomago += macaco
#         print('não gostei de ingerir meu amigo, estou me sentindo mal')
#
#
#     def digerir(self):
#         sleep(2)
#         print('digerindo alimento')
#         sleep(2)
#         self.estomago  = 0
#
#
#
#     def medicao_de_tedio(self, horas):
#         if horas >= 3:
#             self.tedio = self.tedio[0]
#         elif 2 <= horas < 3:
#             self.tedio = self.tedio[1]
#         elif horas < 2:
#             self.tedio = self.tedio[2]
#         print(f'tédio: {self.tedio}')
#
#
#
#
#     def brincando(self, horas):
#         calorias = horas * 200
#         if opção == 'B':
#             if self.estomago > calorias:
#                 self.estomago -= calorias
#                 sleep(2)
#                 print('brincandoo ebaa')
#                 sleep(3)
#                 blue.ver_estomago()
#                 blue.medicao_de_tedio(horas)
#             else:
#                 print('seu bichinho não têm energia suficiente para brincar por esse periodo de horas, alimente ele ou reduza o tempo de brincadeira, tá bom? ')
#                 print('opções: \n[a] alimentar mais\n[b] mudar tempo de brincadeira')
#                 choice = str(input('deseja alimentar mais ou mudar o tempo de bricadeira? ')).strip().lower()[0]
#                 if choice in 'aA':
#                     blue.comer(int(input(f'informe quantas calorias deseja dar para o {self.nome}: ')))
#                     brincar_com_blue()
#                 elif choice in 'bB':
#                     brincar_com_blue()
#         if opção == 'D':
#             if self.estomago > calorias:
#                 self.estomago -= calorias
#                 sleep(2)
#                 print('brincandoo ebaa')
#                 sleep(3)
#                 daniel.ver_estomago()
#                 daniel.medicao_de_tedio(horas)
#             else:
#                 print(
#                     'seu bichinho não têm energia suficiente para brincar por esse periodo de horas, alimente ele ou reduza o tempo de brincadeira, tá bom? ')
#                 print('opções: \n[a] alimentar mais\n[b] mudar tempo de brincadeira')
#                 choice = str(input('deseja alimentar mais ou mudar o tempo de bricadeira? ')).strip().lower()[0]
#                 if choice == 'a':
#                     daniel.comer(int(input(f'informe quantas calorias deseja dar para o {self.nome}: ')))
#                     brincar_com_daniel()
#                 elif choice == 'b':
#                     brincar_com_daniel()
#
#
# opção = 'o'
# canibalismo = 'F'
#
# while canibalismo != "S" or opção != 'F':
#     pular_linha()
#     print('para encerrar com os macacos digite fim')
#     pular_linha()
#     opção = 'E'
#     while opção not in 'BD':
#         opção = str(input('qual macaco voçê deseja [BLUE/DANIEL]? ')).strip().upper()[0]
#         if opção == 'F':
#             break
#     if opção == 'B':
#         blue = Macaco('blue', int(input('estomago  entre 0 e 1000 kcal: ')))
#         blue.ver_estomago()
#         alimentar = str(input('deseja se alimentar? ')).upper()[0]
#         if alimentar == 'S':
#             canibalismo = str(input('deseja se alimentar do seu amigo macaco? ')).strip().upper()[0]
#             if canibalismo == 'S':
#                 macaco = 200
#                 blue.canibalismo(macaco)
#                 break
#
#             else:
#                 print('voçê precisa comer 3 refeições, sabendo que seu limite de calorias são 1000kcal')
#                 for c in range(0, 3):
#                     blue.comer(int(input(f'quantas calorias voce está ingerindo nessa {c + 1}° refeição: ')))
#                     blue.ver_estomago()
#             def brincar_com_blue():
#                 brincar = str(input('deseja brincar com o bichinho? ')).lower()[0]
#                 if brincar in 'simSIMsS':
#                     blue.brincando(int(input('quantas horas voçe quer que ele brinque? ')))
#                 else:
#                     print('uma pena que não queira brincar comigo, aff')
#                 digerir = str(input('deseja digerir o alimento? ')).upper()[0]
#                 if digerir == 'S':
#                     blue.digerir()
#                     blue.ver_estomago()
#                 else:
#                     blue.ver_estomago()
#             brincar_com_blue()
#         else:
#             if opção in 'BbblueBLUE':
#                 brincar1 = str(input('deseja brincar com o bichinho? ')).lower()[0]
#                 if brincar1 in 'simSIMsS':
#                     blue.brincando(int(input('quantas horas voçe quer que ele brinque? ')))
#                 else:
#                     print('uma pena que não queira brincar comigo, aff')
#
#
#
#
#
#     elif opção == 'D':
#         daniel = Macaco('daniel', int(input('estomago entre 0 e 1000 kcal: ')))
#         daniel.ver_estomago()
#
#         alimentar = str(input('deseja se alimentar? ')).upper()[0]
#         if alimentar == 'S':
#             canibalismo = str(input('deseja se alimentar do seu amigo macaco? ')).strip().upper()[0]
#
#             if canibalismo == 'S':
#                 macaco = 200
#                 daniel.canibalismo(macaco)
#                 daniel.ver_estomago()
#                 break
#             else:
#                 print('voçê precisa comer 3 refeições, sabendo que seu limite de calorias são 1000kcal')
#                 for c in range(0, 3):
#                     daniel.comer(int(input(f'quantas calorias voce está ingerindo nessa {c + 1}° refeição: ')))
#                     daniel.ver_estomago()
#             def brincar_com_daniel():
#                 brincar = str(input('deseja brincar com o bichinho? ')).lower()[0]
#                 if brincar == 'S':
#                     daniel.brincando(int(input('quantas horas voçe quer que ele brinque? ')))
#                 else:
#                     print('uma pena que não queira brincar comigo, aff')
#                 digerir = str(input('deseja digerir o alimento? ')).upper()[0]
#                 if digerir == 'S':
#                     daniel.digerir()
#                     daniel.ver_estomago()
#                 else:
#                     daniel.ver_estomago()
#             brincar_com_daniel()
#         else:
#             brincar = str(input('deseja brincar com o bichinho? ')).lower()[0]
#             if brincar == 'S':
#                 daniel.brincando(int(input('quantas horas voçe quer que ele brinque? ')))
#             else:
#                 print('uma pena que não queira brincar comigo, aff')
#             daniel.ver_estomago()
#
#
#     elif opção == 'F':
#         break
#
#
# if canibalismo == 'S':
#     pular_linha()
#     print('fechei o programa por voçê matar meu amigo, odeio voçê')
#
# pular_linha()
# print('operação com macacos finalizado')



# class Ponto():
#     def __init__(self, pontox, pontoy):
#         self.pontox = pontox
#         self.pontoy = pontoy
#
#
#
#
#
#     def mostrar_valores(self):
#         print(f'ponto x: {self.pontox}\nponto y: {self.pontoy}')
#
#
# ponto = Ponto(54, 36)
#
#
#
# class Retangulo():
#     def __init__(self, largura, altura, vertice_esquerdo,vertice_direito):
#         self.largura = largura
#         self.altura = altura
#         self.centro = self.largura / 2 + self.altura / 2
#         self.vertice_esquerdo = vertice_esquerdo
#         self.vertice_direito = vertice_direito
#
#
#
#
#
#     def alterar_mostrar_valores(self):
#         self.largura = int(input('nova largura: '))
#         self.altura = int(input('nova altura: '))
#         self.centro = self.largura / 2 + self.altura / 2
#         print(f'seu novo centro é: {self.centro}m')
#
#
#
# retangulo01 = Retangulo(12, 5, ponto.pontox, ponto.pontoy )
# retangulo02 = Retangulo(19, 8, ponto.pontox, ponto.pontoy)
# retangulo03 = Retangulo(10, 20, ponto.pontox, ponto.pontoy)
# retangulo04 = Retangulo(30, 50, ponto.pontox, ponto.pontoy)
#
#
#
# print('''
# r1 = retangulo01
# r2 = retangulo02
# r3 = retangulo03
# r4 = retangulo04''')
# print('escolha um dos 4 retângulos: ')
# erro = 0
# while True:
#     escolha = str(input('qual sua escolha: ')).lower()
#     if escolha not in 'r1r2r3r4':
#         erro += 1
#     if erro == 5:
#         print('seu idiota, voce errou 5 vezes')
#         break
#     if escolha == 'r1':
#         retangulo01.alterar_mostrar_valores()
#     elif escolha == 'r2':
#         retangulo02.alterar_mostrar_valores()
#
#     elif escolha == 'r3':
#         retangulo03.alterar_mostrar_valores()
#
#     elif escolha == 'r4':
#         retangulo04.alterar_mostrar_valores()
#
#     elif escolha not in 'r1r2r3r4':
#         print('escolha inválida')
#
#
#     elif escolha == 'fim':
#         break



# from time import sleep
# cores = {'ciano': '\033[36m', 'stop': '\033[m'}
# cabecalho = ('bem vindo ao nosso posto de combustivel').upper()
# print(f'{"->"*15} {cores["ciano"]}{cabecalho} {cores["stop"]}{"->"*15}')
# lista_total = []
# class BombaCombustivel():
#     def __init__(self, valor, quantidade):
#         self.tipo_de_combustivel = ['alcool', 'etanol', 'gasolina']
#         self.alcool = 5
#         self.gasolina = 7
#         self.etanol = 9
#         self.valor_por_litro = [5, 9, 7]
#         self.quantidade_de_combustivel = quantidade
#         self.type_pagament = ['a vista', 'cartão no débito', 'cartão no crédito', 'pix']
#         self.tanque = 0
#         self.tanque += self.tanque
#
#
#     def types_de_combustiveis(self):
#         print('tipos: ', end='')
#         for types in self.tipo_de_combustivel:
#             print(f'  {types}  ', end='')
#
#     def value_por_litro(self):
#         print('\nvalores: ', end='')
#         for types in self.valor_por_litro:
#             print(f'{types} reais  ', end='')
#
#     def abastece_por_valor(self, type, valor):
#         print('enchendo seu tanque..')
#         sleep(3)
#         if type == 'alcool':
#             capacidade_alcool = valor / self.alcool
#             print(f'com {valor} reais abastece {capacidade_alcool:.1f} litros de alcool do seu tanque')
#             self.tanque += capacidade_alcool
#             lista_total.append(valor)
#
#         elif type == 'gasolina':
#             capacidade_gasolina = valor / self.gasolina
#             print(f'com {valor} reais abastece {capacidade_gasolina:.1f} litros de gasolina no seu tanque')
#             self.tanque += capacidade_gasolina
#             lista_total.append(valor)
#         elif type == 'etanol':
#             capacidade_etanol = valor / self.etanol
#             print(f'com {valor} reais abastece {capacidade_etanol:.1f} litros de etanol no seu tanque ')
#             self.tanque += capacidade_etanol
#             lista_total.append(valor)
#         else:
#             print('tipo de combustivel não identificado')
#
#
#     def abastece_por_litro(self, type, litragem):
#         print('enchendo seu tanque..')
#         sleep(3)
#         self.tanque += litragem
#         if type == 'alcool':
#             preco_alcool = litragem * self.alcool
#             print(f'para encher {litragem} litros do tanque com alcool, vai custar: {preco_alcool} reais')
#             lista_total.append(preco_alcool)
#         elif type == 'gasolina':
#             preco_gasolina = litragem * self.gasolina
#             print(f'para encher {litragem} litros do tanque com gasolina, vai custar: {preco_gasolina} reais')
#             lista_total.append(preco_gasolina)
#         elif type == 'etanol':
#            preco_etanol = litragem * self.etanol
#            print(f'para encher {litragem} litros do tanque com etanol, vai custar: {preco_etanol} reais')
#            lista_total.append(preco_etanol)
#         else:
#             print('tipo de combustivel não identificado')
#
#     def mostrar_tanque(self):
#         print()
#         print(f'preenchimento do tanque: {self.tanque:.1f}l')
#
#
#
#     def linha(self):
#         tamanho = len(self.type_pagament) + 7
#         c = '->'
#         print(f'    {c*tamanho}')
#
#
#
#     def total_gasto(self):
#         print(f'total a ser pago: {sum(lista_total):.1f} reais')
#
#
#
#     def pagamento(self):
#         print()
#         print('contabilizando seu pedido, aguarde...')
#         sleep(2)
#         print(f'preenchimento total do tanque: {self.tanque:.1f}l')
#         bomba.total_gasto()
#         sleep(1)
#         print(f'          {"tipos de pagamento: "}           ')
#         bomba.linha()
#         for indice , types in enumerate(self.type_pagament):
#             print(f'   [{indice+1}] - {types}   ')
#         bomba.linha()
#
#     def final(self):
#         bomba.pagamento()
#
#     def adicionar(self):
#         se = 'p'
#         while se not in 'nãoNÃOnaoNAOnN':
#             se = str(input('deseja adicionar mais? [s/n]? ')).lower()[0]
#             if se == 's':
#                 opções()
#             elif se in 'nãoNÃOnaonN':
#                 bomba.final()
#             else:
#                 print('sim ou não')
#
# bomba = BombaCombustivel(10, 20)
# bomba.types_de_combustiveis()
# bomba.value_por_litro()
#
#
# def opções():
#     print('\n')
#     print('''opções:
# [a] informar quantos litros deseja e ver o preço.
# [b] informar o preço e ver quantos litros enche.''')
#     while True:
#         opcao = str(input('qual opção acima [a/b]? ')).lower()
#         if opcao in 'ab':
#             break
#
#     if opcao == 'a':
#         bomba.abastece_por_litro(
#             str(input('qual tipo de combustivel voce deseja colocar no seu tanque [alcool, etanol, gasolina]? ')),
#             int(input('quantos litros voce deseja encher? ')))
#         bomba.mostrar_tanque()
#         bomba.adicionar()
#     elif opcao == 'b':
#         bomba.abastece_por_valor(
#             str(input('qual tipo de combustivel voce deseja colocar no seu tanque [alcool, etanol, gasolina]? ')),
#             int(input('digite o valor que voce deseja colocar? ')))
#         bomba.mostrar_tanque()
#         bomba.adicionar()
#
#
# opções()








# from time import sleep
# aviso = 'AVISO: 1litro de gasolina percorre 10km'.upper()
# cores = {'vermelho': '\033[31m', 'stop': '\033[m'}
# print(f'{cores["vermelho"]}{aviso}{cores["stop"]}')
# class Carro():
#     def __init__(self):
#         self.tanque = 0
#         self.km = 0
#         self.consumo = 0
#
#     def retornar_tanque(self):
#         print(f'litros disponiveis no tanque: {self.tanque:.1f} litros')
#
#     def adicionar_combustivel(self):
#         litragem = int(input('quanto litros de gasolina voçê deseja  encher o tanque: '))
#         self.tanque += litragem
#
#     def andar(self):
#         self.km = int(input('quantos km pretende andar? '))
#         self.consumo = self.km / 10
#         if self.tanque >= self.consumo:
#             print('entrando em movimento..')
#             sleep(1)
#             print('realizando o percurso..')
#             sleep(4)
#             print('chegando ao local do percurso..')
#             sleep(2)
#             restante = self.tanque - self.consumo
#             if restante >= 1:
#                 print(f'restou {restante:.1f}l de gasolina restante no tanque após o percurso')
#             else:
#                 restante *= 1000
#                 print(f'restou {restante:.1f} ml de gasolina restante no tanque após o percurso')
#         else:
#             print(f'capacidade indisponivel para percorrer todo este percurso, encha mais o tanque')
#             carro.adicionar_combustivel()
#             carro.retornar_tanque()
#             carro.andar()
#
# carro = Carro()
# carro.retornar_tanque()
# carro.adicionar_combustivel()
# carro.retornar_tanque()
# carro.andar()







# from time import sleep
# lista_de_taxas = []
# lista_de_taxas_convertidas = []
#
# class Banco():
#     def __init__(self):
#         self.saldo = 1000
#         self.juros = 10
#         print(f'saldo inicial: {self.saldo} reais')
#         print(f'juros inicial: {self.juros} reais')
#     def adicionar_juros(self):
#         for c in range(0, 5):
#             taxa = int(input(f'digite a taxa em relação ao saldo de: {self.saldo} reais '))
#             lista_de_taxas.append(taxa)
#         lista_de_taxas.append(self.juros)
#
#     def calculando_juros_no_saldo(self):
#         for c in lista_de_taxas:
#             lista_de_taxas_convertidas.append(c * self.saldo / 100)
#
#
#     def mostrando_taxas(self):
#         print('convertendo taxas...')
#         sleep(3)
#         print('mostrando as taxas convertidas obtemos: ', end='')
#         for c in lista_de_taxas_convertidas:
#             sleep(0.9)
#             print(f'  {c:.0f}  ', end='')
#         print(f'\nsomando as taxas de juros convertidas temos: {sum(lista_de_taxas_convertidas):.0f}')
#
#     def mostrando_saldo_junto_com_as_taxas(self):
#         sleep(4)
#         total = self.saldo + sum(lista_de_taxas_convertidas)
#         print(f'somando as taxas juntamente com o saldo daria um total de {total:.0f} reais')
#         print(f'saldo final: {total:.0f} reais')
#
# banco = Banco()
# banco.adicionar_juros()
# banco.calculando_juros_no_saldo()
# banco.mostrando_taxas()
# banco.mostrando_saldo_junto_com_as_taxas()


# class Funcionario():
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario
#
#     def mostrar_valores(self):
#         print(f'o nome é: {self.nome} \no salário é: {self.salario:.1f} reais')
#
#
#     def aumentar_salario(self, taxa):
#         aumento = taxa * self.salario / 100
#         print(f'o novo salário com um aumento de {taxa}% é de: {self.salario + aumento} reais')
#
#
# funcionario = Funcionario(str(input('nome: ')), int(input('salário: ')))
# funcionario.mostrar_valores()
# funcionario.aumentar_salario(int(input('qual porcentagem de aumento de salário: ')))












# from time import sleep
#
# def s():
#     sleep(2)
# def linha_personalizada():
#     print('>=' * 20)
# cores = {'ciano': '\033[36m', 'vermelho': '\033[31m', 'stop': '\033[m', 'magenta': '\033[35m', 'azul': '\033[34m'}
# class BichinhoFazenda():
#     def __init__(self, nome):
#         self.nome = nome
#         self.tedio = ['pouco tédio', 'tédio mediano', 'muito tédio']
#         self.fome = ['pouca fome', 'fome mediana', 'muita fome']
#         self.armazenamento = 0
#         self.calorias = 0
#         self.horas = 0
#
#
#
#     def alimentar_bichinhos(self):
#         linha_personalizada()
#         print('limite aceitável de calorias = 1000kcal')
#         linha_personalizada()
#
#         calorias = int(input(f'quantas calorias voçê deseja dar para o bichinho {self.nome}? '))
#         self.calorias = calorias
#         if calorias <= 1000 and calorias > 0:
#             print(f'{cores["ciano"]}ebaaaa comendo, que delicia  {cores["stop"]}')
#             self.armazenamento = self.calorias
#             if calorias >= 600:
#                 self.fome = self.fome[0]
#             elif 300 <= calorias < 600:
#                 self.fome = self.fome[1]
#             elif calorias < 300:
#                 self.fome = self.fome[2]
#             sleep(2)
#
#         else:
#             if calorias > 1000:
#                 print('calorias acima do limite')
#             if calorias <= 0:
#                 print('calorias inaceitáveis, seu bichinho precisa comer')
#             BichinhoFazenda.alimentar_bichinhos(self)
#             print()
#
#
#
#     def brincar(self):
#         print()
#         linha_personalizada()
#         aviso = (f'{cores["vermelho"]}AVISO: brincando 1 hora queima 100 calorias, lembre - se que sem calorias seu bichinho não pode brincar{cores["stop"]}').upper()
#
#         print(aviso)
#         linha_personalizada()
#         print()
#         horas = float(input('quantas horas voçê deseja brincar? '))
#         self.horas = horas
#         cálculo_kcal = self.armazenamento / 100
#         gasto_energético = self.horas * 100
#         self.gasto_energético = gasto_energético
#         if horas <= 0:
#             print(f'uma pena que voçê não queira brincar comigo, {cores["vermelho"]}estou de mal {cores["stop"]}')
#             self.tedio = self.tedio[2]
#         if horas > 0:
#             if cálculo_kcal >= self.horas:
#                 sleep(1)
#                 print(f'{cores["ciano"]}ebaaaa, estava doido para brincar, uhuu {cores["stop"]}')
#                 sleep(2)
#                 print(f'{cores["ciano"]}brincandoo {cores["stop"]}')
#                 sleep(2)
#                 if self.horas >= 4.5:
#                     self.tedio = self.tedio[0]
#                 elif 2 <= self.horas < 4.5:
#                     self.tedio = self.tedio[1]
#                 elif self.horas < 2:
#                     self.tedio = self.tedio[2]
#             else:
#                 print(f'energia indisponivel para brincar durante {self.horas} horas, alimente ele ou diminua a quantidade de horas')
#                 op = str(input('opções: \n[a] diminuir quantidade de horas\n[b] alimentar mais \n[a/b]: ')).lower()[0]
#                 if op in 'aA':
#                     BichinhoFazenda.brincar(self)
#                 elif op in 'bB':
#                     BichinhoFazenda.alimentar_bichinhos(self)
#                     BichinhoFazenda.brincar(self)
#
#     def mostrando_fome_tédio_armazenamento(self):
#         print(f'{cores["magenta"]}horas brincadas: {self.horas} horas')
#         s()
#         print(f'{cores["magenta"]}total de calorias inicial: {self.calorias} kcal')
#         s()
#         print(f'{cores["magenta"]}total de calorias final: {self.armazenamento - self.gasto_energético} kcal')
#         s()
#         print(f'{cores["magenta"]}fome: {self.fome}{cores["stop"]}')
#         s()
#         print(f'{cores["magenta"]}tédio: {self.tedio} {cores["stop"]}')
#
# bichinho01 = BichinhoFazenda('blue')
# bichinho02 = BichinhoFazenda('daniel')
# bichinho03 = BichinhoFazenda('marina')
# bichinho04 = BichinhoFazenda('matheus')
# bichinho05 = BichinhoFazenda('sophia')
#
# def cuidando_de_todos_os_bichinhos():
#     bichinho01.alimentar_bichinhos()
#     bichinho01.brincar()
#     bichinho01.mostrando_fome_tédio_armazenamento()
#
#     bichinho02.alimentar_bichinhos()
#     bichinho02.brincar()
#     bichinho02.mostrando_fome_tédio_armazenamento()
#
#
#     bichinho03.alimentar_bichinhos()
#     bichinho03.brincar()
#     bichinho03.mostrando_fome_tédio_armazenamento()
#
#     bichinho04.alimentar_bichinhos()
#     bichinho04.brincar()
#     bichinho04.mostrando_fome_tédio_armazenamento()
#
#     bichinho05.alimentar_bichinhos()
#     bichinho05.brincar()
#     bichinho05.mostrando_fome_tédio_armazenamento()
#     print(f'{cores["azul"]}joguiho de bichinhos encerrado {cores["stop"]}')
# cuidando_de_todos_os_bichinhos()



# from time import sleep
# dict_of_situation = {}
# list = []
# class Estudant():
#     def __init__(self):
#         self.name = str(input('type your name: ')).capitalize()
#         self.age = int(input('type your age:  '))
#         for c in range(1, 5):
#             note = float(input(f'type {self.name} is {c}° note: '))
#             list.append(note)
#         self.note1 = list[0]
#         self.note2 = list[1]
#         self.note3 = list[2]
#         self.note4 = list[3]
#
#     def return_average(self):
#         self.average = int(sum(list) / len(list))
#         print('returnin your average, hold up! ')
#         sleep(2)
#         print(f'your average is: {self.average}')
#
#
#     def situation(self):
#         print('analyzing your situation, wait! ')
#         sleep(2)
#         if self.average >= 7:
#             dict_of_situation['situation'] = ('approved')
#
#
#         elif 6 <= self.average < 7:
#             dict_of_situation['situation'] = ('recovery')
#
#         else:
#            dict_of_situation['situation'] = ('disapproved')
#
#         for k, v in dict_of_situation.items():
#             print(f'{k} is: {v}')
#
#
#
#
# daniel = Estudant()
# daniel.return_average()
# daniel.situation()

# def personalyzed_line():
#     print('->' * 10)
#
# colors = {'cyan': '\033[36m', 'stop': '\033[m', 'red': '\033[31m', 'bold': '\033[1m'}
# print(f'{colors["cyan"]} {"WELCOME TO OUR SUPERMARKET":^100} {colors["stop"]} ')
# class Foods():
#     def __init__(self):
#         self.banana = 3
#         self.apple = 4
#         self.orange = 5
#         self.raspberry = 3
#         self.price = 0
#         self.price_of_fruits = [self.banana, self.apple, self.orange, self.raspberry]
#
#     def fruits(self):
#         list_of_fruits = ['banana', 'apple', 'orange', 'raspberry']
#         personalyzed_line()
#         print(f'{"  available fruits: ":^15}')
#         for price, fruit in enumerate(list_of_fruits):
#             print(f'- {fruit} = {self.price_of_fruits[price]} dollars')
#         personalyzed_line()
#
#         while True:
#             option = str(input('which fruit do  you want? ')).lower()
#             if option == 'banana':
#                 amount = int(input('how many bananas? '))
#                 self.price += self.banana * amount
#             elif option == 'apple':
#                 amount = int(input('how many apples? '))
#                 self.price += self.apple * amount
#             elif option == 'orange':
#                 amount = int(input('how many oranges? '))
#                 self.price += self.orange * amount
#             elif option == 'raspberry':
#                 amount = int(input('how many raspberrys? '))
#                 self.price += self.raspberry * amount
#             else:
#                 print('option not available, try again')
#             food.return_price()
#             while True:
#                 option_more = str(input('do you want to buy some more fruit? ')).lower()
#                 if option_more in 'yessimSIM':
#                     break
#                 elif option_more in 'notnãoNAOnãoNOT':
#                     break
#                 else:
#                     print(f'{colors["bold"]}{colors["red"]}option not available, type yes or not !!{colors["stop"]}')
#             if option_more in 'notnãoNAOnãoNOT':
#                 print('completed fruit purchase')
#                 break
#     def return_price(self):
#         personalyzed_line()
#         print(f'the total price until now is: {self.price} dollars')
#         personalyzed_line()
#
#
#     def meats(self):
#         list_of_meats = ['chicken', 'pork', 'tilapia', 'beef']
#         personalyzed_line()
#         print(f'{" available meats: ":^15}')
#         for meat in list_of_meats:
#             print(f'- {meat}')
#         personalyzed_line()
#         print(end='')
#     def drinks(self):
#         list_of_drinks = ['soda', 'juice', 'tang', 'fruit of juice', 'beer']
#         personalyzed_line()
#         print(f'{" available drinks: ":^15}')
#         for drink in list_of_drinks:
#             print(f'- {drink}')
#         personalyzed_line()
#
# food = Foods()
#
#
# print(f'choice options: ')
# personalyzed_line()
# print('''
#        drinks
#        meats
#        fruits ''')
#
# personalyzed_line()
# option = str(input('what do you want to visualize between the options above? ')).lower()
# if option in 'fruits':
#     food.fruits()
# elif option in 'meats':
#     food.meats()
# elif option in 'drinks':
#     food.drinks()
# else:
#     print('options not available')



# print(f'\033[34m{"what is the best operational server for use on servers?":^60}\033[m ')
# print('''the possibles answers are:
#  1 - windows
#  2 - unix
#  3 - linux
#  4 - netware
#  5 - mac os
#  6 - outro
#  ''')
#
#
# cont = 0
# list_windows = []
# list_unix = []
# list_linux = []
# list_netware = []
# list_mac_os = []
# list_outro = []
#
#
# def l(tamanho):
#     print('--' * tamanho, end='        ')
#
#
# while True:
#     choice = str(input('choice one server: [0 to finish the program]: ')).strip().lower()
#     if choice == '1':
#         cont += 1
#         list_windows.append(cont)
#
#     elif choice == '2':
#         cont += 1
#         list_unix.append(cont)
#
#     elif choice == '3':
#         cont += 1
#         list_linux.append(cont)
#
#     elif choice == '4':
#         cont += 1
#         list_netware.append(cont)
#
#     elif choice == '5':
#         cont += 1
#         list_mac_os.append(cont)
#
#     elif choice == '6':
#         cont += 1
#         list_outro.append(cont)
#     elif choice == '0':
#         break
#     else:
#         print(f'\033[31m ERROR, CHOICE ONE APPLICABLE OPTION\033[m')
#
#
# print(f'operational sistem ', end='           ')
# print(f'{"wishes"} ', end='          ')
# print(f'{"%"}')
#
#
# l(len('operational sistem') - 9)
# l(len('wishes'))
# l(len('%'))
#
# print()
#
#
# print('Windows server', end='                 ')
# print(f'{len(list_windows)}', end='          ')
#
# print('\nUnix', end='                           ')
# print(f'{len(list_unix)}', end='          ')
#
# print('\nLinux', end='                          ')
# print(f'{len(list_linux)}', end='          ')
#
# print('\nNetware', end='                        ')
# print(f'{len(list_netware)}', end='          ')
#
# print('\nMac os', end='                         ')
# print(f'{len(list_mac_os)}', end='          ')
#
# print('\nOutro', end='                          ')
# print(f'{len(list_outro)}', end='          ')
#
# print('\n')
#
# l(len('totallllo'))
# total = len(list_windows) + len(list_unix) + len(list_linux) + len(list_netware) + len(list_mac_os) + len(list_outro)
# print(f'\ntotal: {total:0} votos')
#
# list = []
# list.append(len(list_linux))
# list.append(len(list_netware))
# list.append(len(list_outro))
# list.append(len(list_mac_os))
# list.append(len(list_unix))
# list.append(len(list_windows))
#
# tamanhow = len(list_windows)
# tamanhol = len(list_linux)
# tamanhon = len(list_netware)
# tamanhoo = len(list_outro)
# tamanhom = len(list_mac_os)
# tamanhou = len(list_unix)
#
#
# maior = 'ninguem'
# valor = 0
# if tamanhow > tamanhou and tamanhow > tamanhol and tamanhow > tamanhon and tamanhow> tamanhoo and tamanhow > tamanhom:
#     maior = 'servidor windows'
#     valor = tamanhow
# elif tamanhol > tamanhow and tamanhol > tamanhon and tamanhol > tamanhoo and tamanhol > tamanhom and tamanhol > tamanhou:
#     maior = 'servidor linux'
#     valor = tamanhol
# elif tamanhon > tamanhow and tamanhon > tamanhol and tamanhon > tamanhoo and tamanhon > tamanhom and tamanhon > tamanhou:
#     maior = 'servidor netware'
#     valor = tamanhon
# elif tamanhoo > tamanhow and tamanhoo > tamanhol and tamanhoo > tamanhou and tamanhoo > tamanhom and tamanhoo > tamanhon:
#     maior = 'outros servidores'
#     valor = tamanhoo
#
# elif tamanhom > tamanhow and tamanhom > tamanhon and tamanhom > tamanhoo and tamanhom > tamanhon and tamanhom > tamanhou:
#     maior = 'servidor mac OS'
#     valor = tamanhom
#
# elif tamanhou > tamanhow and tamanhou > tamanhon and tamanhou > tamanhoo and tamanhou > tamanhom and tamanhou > tamanhol:
#     maior = 'servidor unix'
#     valor = tamanhou
# print(f'o servidor mais votado foi {maior} com {valor} votos')
#





def linha_cabecalho():
    print(f'{"--"* 17:^50}')


# print(f'\033[34m{"SALARY AND ALLOWANCE PROJECTION":^50}\033[m')
# linha_cabecalho()
#
# list = []
# list_allowance = []
# cont_minimum = 0
# while True:
#     salary = int(input('salary: '))
#     value = 'salary'
#     if salary != 0:
#         list.append(salary)
#     if salary == 0:
#         break
#     allowance = 20 * salary / 100
#     if allowance <= 100:
#         allowance = 100
#         cont_minimum += 1
#     list_allowance.append(allowance)
#
#
# def l(tamanho):
#     print('--' * tamanho, end='')
#     print('--' * tamanho, end='')
#     print('--' * tamanho)
# print()
# print('\n')
# print(f'{"salary":^20} {"allowance":^20}')
# l(len('salary'))
# for cont, v in enumerate(list):
#     print(f'  R$ {v:.2f}      -      R$ {list_allowance[cont]:.2f}')
#
#
# print('\n')
# print(f'total number employers: \033[35m {len(list)} \033[m')
# print(f'total amound  paid of allowance:\033[35m {sum(list_allowance)} \033[m  ')
# print(f'minimum value paid to \033[35m{cont_minimum} \033[m employees')
# print(f'higher allowance value: \033[35m {max(list_allowance)} \033[m ')




# print(f'\033[36m {"COMPARATIVE OF FUEL CONSUPTION BETWEEN 5 CARS":^50}\033[m')
# print('\n')
# list = []
# list_fuel = []
# for car in range(0, 5):
#     print('->' * 10)
#     print(f'vehicle {car + 1}:')
#     name_car = str(input('name of car: '))
#     while name_car in list:
#         print('\033[31mcar already stored, choose another!\033[m')
#         name_car = str(input('name of car: '))
#     if name_car not in list:
#         km_for_liter = float(input('km for liter: '))
#         if km_for_liter <= 0:
#             km_for_liter = 1
#         list.append(name_car)
#         list_fuel.append(km_for_liter)
#     else:
#         print('\033[31mcar already stored, choose another!\033[m')
#
#
# print()
# print('\033[33m FINAL REPORT: \033[m')
# print('\033[35m')
# print(f'{"vehicle":^10}  -  {"name of car":^10} -  {"km for liter":^10}    -    {" liter for 100 km":^10}      -    {"value to be paid":^10} \033[m ')
# list_1000km = []
# list_price = []
# price_gasoline = 2.25
# for c in list_fuel:
#     liter_1000km = 1000 / c
#     list_1000km.append(liter_1000km)
#
# for c in list_1000km:
#     total_price = price_gasoline * c
#     list_price.append(total_price)
#
# for v, k in enumerate(list):
#     print(f'{v + 1:^10}  - {k:^10}    -  {list_fuel[v]:^10}   -           {list_1000km[v]:^10.2f}       -     {list_price[v]:^10.2f}')
#
# maior = 0
# for v, km in enumerate(list_fuel):
#     valor = km
#     maior = list[v]
#     if km > valor:
#         maior = list[v + 1]
#         maior.upper()
#
#
# print('\n')
# print(f'\033[32m THE MOST ECNOMICAL CAR IS:  {maior} \033[m')


# def l():
#     print('\033[32m-----------------------')
#
#
# print(f'\033[35m{"MOUSE SCRAP COLLECTION":^70}\033[m')
# list_razer = []
# list_tradicional = []
# list_logitech = []
# list_goldentec = []
# list_options_of_mouse = ['razer'.upper(), 'tradicional'.upper(), 'logitech'.upper(), 'goldentec'.upper()]
# list_defects_options = ['need ball     '.upper(), 'needs cleaning'.upper(), 'needs cable   '.upper(), 'need conserts '.upper()]
# print('mouse options: ')
#
# list_need_ball = []
# list_needs_cleaning = []
# list_needs_cable_or_connector = []
# list_broken = []
#
#
#
# l()
# for c, mouses in enumerate(list_options_of_mouse):
#     print(f'\033[32m{c+1} : {mouses:^20}')
# l()
# print()
# print('\033[mmouse problems option:')
# l()
#
# for c, defects in enumerate(list_defects_options):
#     print(f'\033[32m{c + 1} : {defects:^20}')
# l()
#
# while True:
#     id = str(input('\033[mtype the mouse identification: '))
#     if id == '0':
#         break
#     if id in '1234':
#         if id == '1':
#             list_razer.append(1)
#         elif id == '2':
#             list_tradicional.append(1)
#         elif id == '3':
#             list_logitech.append(1)
#         elif id == '4':
#             list_goldentec.append(1)
#         defect = str(input('type the mouse defect: '))
#         if defect in '1234':
#             if defect == '1':
#                 list_need_ball.append(1)
#             elif defect == '2':
#                 list_needs_cleaning.append(1)
#             elif defect == '3':
#                 list_needs_cable_or_connector.append(1)
#             elif defect == '4':
#                 list_broken.append(1)
#         else:
#             print('\033[31m incorret option, choose 1,2,3 or 4 \033[m')
#
#     else:
#         print('\033[31mincorret option, choose 1,2,3 or 4\033[m')
# list = [len(list_razer), len(list_tradicional), len(list_logitech), len(list_goldentec)]
# list_geral = [len(list_need_ball), len(list_needs_cleaning), len(list_needs_cable_or_connector), len(list_broken)]
# print()
# print(f'\033[35m       {"situation"}                         {"amount":^20}                    {"percentual"}\033[m')
# for c, v in enumerate(list_geral):
#     print(f'{c+1:^} - {list_defects_options[c]:^}                        {list_geral[c]:^20}                      {list_geral[c]:}%')
#
#
# maior = 'nenhum'
# if max(list) == len(list_razer):
#     maior = 'razer'
# elif max(list) == len(list_tradicional):
#     maior = 'tradicional'
# elif max(list) == len(list_logitech):
#     maior = 'logitech'
# elif max(list) == len(list_goldentec):
#     maior = 'goldentec'
#
#
# print(f'the most found mouse was: \033[34m{maior.upper()}\033[m')
#










