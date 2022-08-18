# def contar_caracteres(string):
#     caracteres_ordenados = sorted(string)
#     caracter_anterior = caracteres_ordenados[0]
#     contagem = 1
#     print(f'contando caracteres do nome: {string}')
#     for caracter in caracteres_ordenados[1: ]:
#         if caracter == caracter_anterior:
#             contagem += 1
#         else:
#             print(f'{caracter_anterior}: {contagem}')
#             caracter_anterior = caracter
#             contagem = 1
#     print(f'{caracter_anterior}: {contagem}')
#
# if __name__ == '__main__':
#     contar_caracteres('silvina')
#     print()
#     contar_caracteres('daniel')


# def contar_caracteres(string):
#     print()
#     resultado = {}
#     print(string)
#     for caracter in string:
#        resultado[caracter] = resultado.get(caracter, 0) + 1
#
#     for k, v in resultado.items():
#         print(f'{k} têm: {v} caracteres')
#
#
# if __name__ == '__main__':
#     print(contar_caracteres('daniel'))
#
#     print(contar_caracteres('silvina'))
#
#     print(contar_caracteres('rafael'))


# print('''available operations:
#  + = sum
#  - = minus
#  * = multiplication
#  / = division''')
#
#
# number = int(input('type a number: '))
# number2 = int(input('type a number: '))
# list = [number, number2]
# division = number / number2
# multiplication = number * number2
# sum = number + number2
# minus = number - number2
# option = str(input('what option do you want [/*-+]? ')).lower()
# if option == '/':
#     print(f'the results of dividing the numbers {number} / {number2} is: {division} ',end='')
#     if division == int(division):
#         print(f'\nand this number is integer')
#     else:
#         print(f'\nand this number is not integer')
#
# elif option == '*':
#     print(f'the results of  the multiplication the numbers {number} * {number2} is: {multiplication} ',end='')
#     if multiplication == int(multiplication):
#         print(f'\nand this number is integer')
#     else:
#         print(f'\nand this number is not integer')
# elif option == '+':
#     print(f'the results of sum the numbers {number} + {number2} is: {sum} ',end='')
#     if sum == int(sum):
#         print(f'\nand this number is integer')
#     else:
#         print(f'\nand this number is not integer')
# elif option == '-':
#     print(f'the results of subtraction the numbers {number} - {number2} is: {minus} ', end='')
#     if minus == int(minus):
#         print(f'\nand this number is integer')
#     else:
#         print(f'\nand this number is not integer')
# else:
#     print('invalid option, try again')
#
#
# if multiplication or minus or sum or division >= 0:
#     print('\nand this number is positive  ')
# else:
#     print('\nand this number is negative')
#
# if multiplication or minus or sum or division % 2 == 0:
#     print('\nand this number is pair  ')
# else:
#     print('\nand this number is odd  ')
#

# contador = 0
# print('MURDERED VICTIM ANALYSIS')
# print('questioning now')
# while True:
#     question1 = str(input('did you call the victim [yes/not]? ')).lower()
#     if question1 == 'yes':
#         contador += 1
#     if question1 in 'yessimnãonaonot':
#         break
#     else:
#         print('answer just with yes or not, answer again')
# while True:
#     question2 = str(input('were you at the crime scene [yes/not]? ')).lower()
#     if question1 == 'yes':
#         contador += 1
#     if question2 in 'yessimnãonaonot':
#         break
#     else:
#         print('answer just with yes or not, answer again')
# while True:
#     question3 = str(input('do you live near the victim [yes/not]? ')).lower()
#     if question3 == 'yes':
#         contador += 1
#     if question3 in 'yessimnãonaonot':
#         break
#     else:
#         print('answer just with yes or not, answer again')
# while True:
#     question4 = str(input('did you owe the victim [yes/not]? ')).lower()
#     if question4 == 'yes':
#         contador += 1
#     if question4 in 'yessimnãonaonot':
#         break
#     else:
#         print('answer just with yes or not, answer again')
# while True:
#     question5 = str(input('did you work with the victim [yes/not]? ')).lower()
#     if question5 == 'yes':
#         contador += 1
#     if question5 in 'yessimnãonaonot':
#         break
#     else:
#         print('answer just with yes or not, answer again')
#
# if contador == 2:
#     print('you are suspect')
#
# elif contador == 3 or contador == 4:
#     print('you are accomplice')
#
# elif contador == 5:
#     print('you are the killer/assassin')
#
# else:
#     print('you are inocent, you can go')

# def personalyzed_line():
#     print('->' * 30)
#
#
# print('DISCOUNT GAS STATION HERE, ENJOY AND FILL THE TANK')
# print(f' {"gasoline":^30} {"alcohol":^30}')
# print(f' {"R$ 2,50":^30} {"R$ 1,90":^30}')
# print(f'{"above 20 dollars, 4% descount":^30}      {"above 20 dollars, 3% descount":^30}')
# print(f'{"below 20 dollars, 2% descount":^30}      {"above 20 dollars, 2% descount":^30}')
# personalyzed_line()
# gasoline = 2.5
# alcohol = 1.9
#
#
#
# def filling_tank(type_of_fuel,liters_to_be_filled):
#     if type_of_fuel == 'alcohol':
#         if liters_to_be_filled <= 20:
#             total_descount = 2
#             price_for_liter = liters_to_be_filled * alcohol
#             descount_of_total_price = total_descount * price_for_liter / 100
#             price_with_descount = price_for_liter - descount_of_total_price
#             print(f'you are taking {liters_to_be_filled} liters of alcohol,it will cost {price_with_descount:.1f} dollars about {total_descount}% of descount')
#
#         elif liters_to_be_filled > 20:
#             total_descount = 3
#             price_for_liter = liters_to_be_filled * alcohol
#             descount_of_total_price = total_descount * price_for_liter / 100
#             price_with_descount = price_for_liter - descount_of_total_price
#             print(f'you are taking {liters_to_be_filled} liters of alcohol,it will cost {price_with_descount:.1f} dollars about {total_descount}% of descount')
#     elif type_of_fuel == 'gasoline':
#         if liters_to_be_filled <= 20:
#             total_descount = 2
#             price_for_liter = liters_to_be_filled * gasoline
#             descount_of_total_price = total_descount * price_for_liter / 100
#             price_with_descount = price_for_liter - descount_of_total_price
#             print(
#                 f'you are taking {liters_to_be_filled} liters of gasoline,it will cost {price_with_descount:.1f} dollars about {total_descount}% of descount')
#
#         elif liters_to_be_filled > 20:
#             total_descount = 4
#             price_for_liter = liters_to_be_filled * gasoline
#             descount_of_total_price = total_descount * price_for_liter / 100
#             price_with_descount = price_for_liter - descount_of_total_price
#             print(
#                 f'you are taking {liters_to_be_filled} liters of gasoline,it will cost {price_with_descount:.1f} dollars about {total_descount}% of descount')
#     else:
#         print('\033[31mtype of fuel not found, try again\033[m')
#         personalyzed_line()
#         print()
#         filling_the_tank()
#
# def filling_the_tank():
#     filling_tank(str(input('do you want alcohol or gasoline? ')).lower(), float(input('how many liters do you wanna fill? ')))
#
# filling_the_tank()
#
#
# print('finished program, thanks')

# from time import sleep
# print('\033[36m')
# print(f'{"WELCOME TO FRUITS SUPERMARKET":^50}')
# print(f'{"until 5kg":^37}    {"above 5kg":^1}')
# print(f'strawberry:  {"2,50 for kg":^12} {"2,20 for kg":^40}')
# print(f'apple:       {"1,80 for kg":^12} {"1,50 for kg":^40}')
# print('\033[m')
#
# def total_price(fruit):
#     total_price = fruit * kg
#     if total_price > 25 or kg > 8:
#         sleep(1)
#         print('calculating 10% descount..')
#         sleep(2)
#         descount = 10 * total_price / 100
#         total_price -= descount
#     print(f'the total price of purchase is: {total_price:.1f} dollars')
#
# apple = 0
# strawberry = 0
#
#
# option = str(input('what do you want? strawberry or apple? ')).strip().lower()[0]
# if option == 's':
#     kg = float(input('how many kg do you wanna take of strawberry? '))
#     if kg <= 5:
#         strawberry = 2.50
#     elif kg > 5:
#         strawberry = 2.20
#     total_price(strawberry)
# elif option == 'a':
#     kg = float(input('how many kg do you wanna take of apple? '))
#     if kg <= 5:
#         apple = 1.80
#     elif kg > 5:
#        apple = 1.50
#     total_price(apple)




# print(f'{"SIMPLE INTEREST CALCULATOR":^50}')
# class Fees():
#     def __init__(self):
#         self.capital = int(input('type the capital: '))
#         while True:
#             self.month_or_year = str(input('time in years or months? [years/months]? ')).lower()
#             if self.month_or_year in "yearyearsmonthmonthsmy":
#                 break
#             else:
#                 print('type month or year, please')
#         if self.month_or_year in "yearyearsy":
#             self.time = int(input(f'type the time in {self.month_or_year}: '))
#             self.time = self.time * 12
#         elif self.month_or_year in 'monthmonthsm':
#             self.time = int(input(f'type the time in {self.month_or_year}: '))
#         self.taxe = float(input('type the taxe: '))
#         self.taxe = self.taxe / 100
#         self.fees_ = self.capital * self.taxe * self.time
#
#     def interest_simple(self):
#         print('the formule is: ', end='')
#         print('J = C * I * T')
#         print(f'\nfees = {self.capital} * {self.taxe} * {self.time}')
#         gross_total_amount = self.capital + self.fees_
#         print(f'the total fees is: {self.fees_:.1f} reais')
#         print(f'the amount is: {gross_total_amount:.1f} reais')
#
#
#     def compound_interest(self):
#         amount = self.capital * (1 + self.taxe) ** self.time
#         print(f'the compound interest is: {amount:.1f} reais')
# fees = Fees()
# fees.interest_simple()
# fees.compound_interest()






# cores = {'magenta': '\033[35m', 'stop': '\033[m'}
# from time import sleep
#
# class Hipermarket():
#
#     def __init__(self):
#         print()
#         print('\033[36m')
#         print(f'{"WELCOME TO HYPERMARKET":^50}')
#         print(f'{"until 5kg":^37}    {"above 5kg":^1}')
#         print(f'double file:   {"4,90 for kg":^12} {"5,80 for kg":^40}')
#         print(f'rump:          {"5,90 for kg":^12} {"6,80 for kg":^40}')
#         print(f'rump steak:    {"6,90 for kg":^12} {"7,80 for kg":^40}')
#         print('\033[m')
#         self.name = str(input('type your name: '))
#         self.descount = 0
#         self.descount_in_price = 0
#         while True:
#             self.option = str(input('what do you want? [double file/ rump/ rump steak]? ')).lower().split()
#             new_option = ''.join(self.option)
#             if new_option in 'doublefilerumprumpsteak':
#                 break
#             else:
#                 print('\033[31minvalid option, try again, please\033[m')
#         self.kg = int(input(f'how many kg do you wanna take? '))
#         if new_option == 'doublefile':
#             self.chosen = 'double file'
#             if self.kg <= 5:
#                 self.double_file = 4.90
#             else:
#                 self.double_file = 5.80
#             self.total_value = self.double_file * self.kg
#         elif new_option == 'rump':
#             self.chosen = 'rump'
#             if self.kg <= 5:
#                 self.rump = 5.90
#             else:
#                 self.rump = 6.80
#             self.total_value = self.rump * self.kg
#         elif new_option == 'rumpsteak':
#             self.chosen = 'rump steak'
#             if self.kg <= 5:
#                 self.rump_steak = 6.90
#             else:
#                 self.rump_steak = 7.80
#             self.total_value = self.rump_steak * self.kg
#
#
#
#
#     def card(self):
#         while True:
#             card = str(input('do you have a hypermarket card? ')).lower()
#             if card in 'yessimyeyenotnãonaodont':
#                 break
#             else:
#                 print(f'\033[31m answer with yes or not, please\033[m')
#         if card in 'yessimye':
#             self.descount = 10
#             self.descount_in_price = self.total_value * 10 / 100
#             self.total_value -= self.descount_in_price
#         elif card in 'notnãonaodont':
#             self.descount = 0
#             self.total_value = self.total_value
#
#
#
#     def invoice(self):
#         print(f'->' * 40)
#         print(f'type: {self.chosen}        client name: {self.name}       amount of meat: {self.kg} kg')
#         print(f'total price: {self.total_value + self.descount_in_price:.1f} dollars                  type of pagament: {"card"}')
#         print(f'descount value: {self.descount}%                          value to be paid: {cores["magenta"]}{self.total_value:.1f} dollars {cores["stop"]}')
#         print(f'->' * 40)
#         print()
#         print('\033[34mthanks for you purchase\033[m')
#         sleep(3)
#
#
# def client():
#     client1 = Hipermarket()
#     client1.card()
#     client1.invoice()
#
#     client2 = Hipermarket()
#     client2.card()
#     client2.invoice()
#
#     client3 = Hipermarket()
#     client3.card()
#     client3.invoice()
#
#     client4 = Hipermarket()
#     client4.card()
#     client4.invoice()
#
# client()



# print('\033[35mATHLETES PERFORMANCE\033[m')
# while True:
#     list = []
#     while True:
#         athlete = input('athlete: ')
#         if athlete.isnumeric():
#             print('\033[31m\033[1mERROR, TYPE A NAME\033[m')
#
#         else:
#             break
#     print()
#     for c in range(0, 5):
#         jump = float(input(f'{c+1}° jump: '))
#         list.append(jump)
#     print()
#     for i, v in enumerate(list):
#         print(f'{i + 1}° jump: {v:.1f}')
#     max = max(list)
#     print()
#     print(f'best jump: {max}')
#     print(f'worst jump: {min(list)}')
#     list.sort()
#     list.pop()
#     list.sort(reverse=True)
#     list.pop()
#
#     list.sort()
#     print(f'average of jumps: {sum(list) / len(list):.1f}')
#     print()
#     print('resultado final: ')
#     print(f'{athlete}: {sum(list) / len(list):.1f}')
#     continuar = str(input('type end to finish the program: ')).strip().lower()[0]
#     if continuar == 'e':
#         break



# while True:
#     number = int(input('type a integer and positive number: '))
#     if number > 0 and number == int(number):
#         break
# print('the number backward is: ', end='')
# number = str(number)
# number_backward = ''.join(reversed(number))
# print(number_backward)



# def pl():
#     print('\n')
# list = list()
# while True:
#     number = float(input('type a value: [-1 to finish]: '))
#     if number != -1:
#         list.append(number)
#     if number == -1:
#         break
# pl()
# print(f'foram digitados {len(list)} números')
# pl()
# print('in order: ', end=' ')
# list.sort()
# for numbers in list:
#     print(numbers, end='  ')
# pl()
# print('in reverse order one below the other: ')
# list.sort(reverse=True)
# for numbers in list:
#     print(numbers)
# pl()
# print(f'the sum of the values is: {sum(list)}')
# pl()
# average = sum(list) / len(list)
# print(f' the average of the values is: {average}')
# pl()
# print(f'the values above of the average is: ', end=' ')
# for values in list:
#     if values > average:
#         print(f'{values}', end=' ')
# pl()
# print(f'the values below of the average is: ', end='  ')
# for values in list:
#     if values < average:
#         print(f'{values}', end=' ')
# pl()
#
# print('thanks for using our program')





# def soma_imposto(value, fee):
#     print(f'value without fee: {value} real')
#     fees = fee * value / 100
#     value = value + fees
#     print(f'value with fee of {fee}% : {value} real')
#
#
# soma_imposto(float(input('type a value: ')), float(input('type a fee: ')))


# class Hour:
#     def __init__(self):
#         print('the conversor of hour')
#         self.controller = ['P.M', 'A.M']
#         self.hour = None
#         self.restante = None
#
#     def change_time(self, hour, value_pm_or_am):
#         if len(hour) > 4:
#             self.hour = hour[:2]
#             self.hour = int(self.hour)
#         elif len(hour) <= 4:
#             self.hour = hour[:1]
#             self.hour = int(self.hour)
#         if self.hour > 12:
#             self.hour = int(self.hour)
#             self.hour = self.hour - 12
#             self.restante = hour[-2:]
#         elif self.hour < 12:
#             self.restante = hour[-2:]
#         if value_pm_or_am == 'p':
#             self.controller = self.controller[0]
#         elif value_pm_or_am == 'a':
#             self.controller = self.controller[1]
#     def show_hour(self):
#         print(f'the time is: {self.hour}:{self.restante} {self.controller}')
#         print('\n')
#
#
# hour = Hour()
# cont = 0
# while True:
#     hour.change_time(str(input('type the hour: ')),
#                      str(input('type hour cotroller [p = p.m] [a = a.m]: '.lower())))
#     hour.show_hour()
#     cont += 1
#     if cont >= 2:
#         break
# print('finished program')



# def l():
#     print('\n')
#     print('->' * 30)
# phrase = 'análysis delivery value'.upper()
# dict = {'blue': '\033[34m', 'stop': '\033[m', 'red': '\033[31m'}
# print(f'{dict["blue"]}{phrase:^50} {dict["stop"]}')
# class Delivery():
#     def __init__(self):
#         pass
#     def delivery_value(self):
#         self.delivery_counter = 0
#         self.list_deliverys = []
#         while True:
#             delivery = float(input('type the delivery value: [0 to finish the program]: '))
#             if delivery != 0:
#                 number_of_days = int(input('type the number of days late: '))
#                 if number_of_days == 0:
#                     delivery = delivery
#                 else:
#                     print(f'{dict["red"]}3% fine{dict["stop"]}')
#                     print('1 % fees for days late')
#                     fees = 1 * number_of_days / 100
#                     fees = fees * delivery
#                     fine = 0.03
#                     fine = fine * delivery
#                     total_rate = fine + fees
#                     delivery = delivery + total_rate
#                 print(f'the total delivery value is: {delivery:.1f} real')
#                 self.delivery_counter += 1
#                 self.list_deliverys.append(delivery)
#                 l()
#             elif delivery == 0:
#                 break
#
#
# delivery = Delivery()
# delivery.delivery_value()
# print('\n')
# print(f'the total amount of delivery of day is: {delivery.delivery_counter}')
# print(f'the total delivery value of day is: {sum(delivery.list_deliverys):.1f} real')


# print('informing total amount of digits of the number')
# def counter_digits(number):
#     print(f'we have a total digits of: {len(number)} digits')
#
#
# number = str(input('type a number: '))
# counter_digits(number)



# print('game manual: ')
# print('''
# the dice is going to draw a random number, if the number = 7 or 11 so, you won the game
# but, if the number = 2, 3 or 12 so, you gave craps and you lost the game
# but, if the numbers are not the numbers above, your point will be this number drawn and you are gonna try to hit your point again
#  if you can hit the point, you won, if you turn 7, you lost the game, good luck
#  ''')
# from random import randint as ran
# from time import sleep as sl
# print('starting the game now')
# sl(2)
# dice = ran(2, 12)
# print('flipping the first dice..')
# sl(1)
# print(f'the firt dice number is: {dice}')
# if dice == 7 or dice == 11:
#     print('\033[33m you won the game\033[m')
# elif dice == 2 or dice == 3 or dice == 12:
#     print('\033[31myou gave craps, so, you losted\033[m')
# else:
#     print(f'your point is: {dice}, try to hit your number again')
#     point = dice
#     while True:
#         sl(3)
#         print('playing again the dice')
#         dice = ran(2, 12)
#         print(f'the number dice is: {dice}')
#         if dice == 7:
#             print('\033[31myou lost the game for turning 7\033[m')
#             break
#         elif dice == point:
#             print('\033[33myou won the game, turned your number point\033[m')
#             break
#         else:
#             print('trying again')
#         print('->'* 10)
#
# print('finished game, thanks for playing')




# for c in range(0, 30):
#    v = ('-')
#    if c == 29:
#        print(v)
#    else:
#        print(v, end='')
# for c in range(0, 4):
#     print(f'{"|"}                             {"|"}')
#
# for c in range(0, 30):
#    v = ('-')
#    print(v, end='')

from random import sample as sam
from random import choice
palavra = str(input('digite uma palavra: '))
list = []
new_string = ''
if palavra != '':
    palavra = palavra.split()
    palavra = ''.join(palavra)
    if len(palavra) > 7:
        primeira_parte = palavra[:3]
        segunda_parte = palavra[2:5]
        terceira_parte = palavra[5:len(palavra)]
    else:
        primeira_parte = palavra[:2]
        segunda_parte = palavra[2:4]
        terceira_parte = palavra[4: len(palavra)]
    value = range(1, 2)
    valor = choice(value)
    if valor == 1:
        new_string = segunda_parte + primeira_parte + terceira_parte
    elif valor == 2:
        new_string = primeira_parte + terceira_parte + primeira_parte

    elif valor == 3:
        new_string = terceira_parte + primeira_parte + segunda_parte


print(f'a palavra {palavra} embaralhada é: {new_string}')