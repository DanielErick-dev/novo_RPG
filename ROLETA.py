from random import randint as ran
cores = {'azul': '\033[34m', 'stop': '\033[m'}

class Filhos:
    def __init__(self):
        self.lista = []

    def filhos(self):
        filhos = int(input('quantos filhos voçê ganhou? '))
        self.lista.append(filhos)

    def valordosfilhos(self):
        valor_total = sum(self.lista) * 48.000
        print(valor_total)

filhos = Filhos()
marina = Filhos()
daniel = Filhos()
rosa = Filhos()
silvina = Filhos()
while True:
    r = str(input('DIGITE ENTER: ')).lower()
    if r == '':
        n = ran(1, 10)
        print(f'o número sorteado é:{cores["azul"]} {n} {cores["stop"]}')
    elif r == 'fim':
        break
    elif r == 'filho':
        escolha = str(input('digite de quem é o filho: ')).lower()[0]
        if escolha == 'm':
            marina.filhos()
        elif escolha == 'd':
            daniel.filhos()
        elif escolha == 'r':
            rosa.filhos()
        elif escolha == 's':
            silvina.filhos()

    elif r == 'contar':
        escolha = str(input('digite de quem é o filho:  ')).lower()[0]
        if escolha == 'm':
            marina.valordosfilhos()
        elif escolha == 'd':
            daniel.valordosfilhos()
        elif escolha == 'r':
            rosa.valordosfilhos()
        elif escolha == 's':
            silvina.filhos()
