# Navegar até uma nova mensagem (Verde)
# Abrir e copiar a informação que o Usuário mandou
# Verficar o banco de dados para caso haja palavras chaves na frase
# Retornar caso haja ou não palavras iguais

import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
import PIL
from time import sleep

# Click do Mouse
mouse = Controller()

class Whatsapp:
    # Método Inicial do bot
    def __init__(self, speed = .5, click_speed = .3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''

    # Método para visualizar se existe uma mensagem enviada
    def verificate_greenDots(self):
        try:
            # Guarda a posição de uma mensagem enviada pelo usuário e clica nele 
            position = pt.locateCenterOnScreen('images/greenDot.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(-100, 0, duration= self.speed)
            pt.doubleClick(interval= self.click_speed)

        except Exception as e:
            print("Exception (verificate_greenDots): ", e)

    def get_userAnswer(self):
        try:
            # Guarda a posição da caixa de mensagem e clica nele 
            position = pt.locateCenterOnScreen('images/paperClip.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(20, -80, duration= self.speed)

            # Copia a resposta do usuário
            mouse.click(Button.left, 3)
            sleep(self.speed)
            pt.hotkey('ctrl', 'c')

            self.message = pc.paste()

        except Exception as e:
            print("Exception (nav_messageBox): ", e)

    def verificate_userAnswer(self):
        try:
            file = open("bd.txt", "r")
            count = 0
            list_phrase = self.message.split(" ")
            list_bd = file.readlines()

            # Retirar os \n das palavras no banco de dados
            for i in range(len(list_bd)):
                list_bd[i] = list_bd[i].replace("\n", "")

            # Verificação se existe uma palavra chave na Frase
            for i in range(len(list_phrase)):
                j = 0
                while(j < len(list_bd)):
                    if(list_phrase[i] == list_bd[j]):
                        count += 1
                    j += 1

            file.close()
            return count

        except Exception as e:
            print("Exception (verificate_userAnswer): ", e) 

    # Método para enviar o relatório caso tenha palavras chaves encontradas na frase
    def nav_messageBox_Fake(self, count):
        try:
            # Guarda a posição da caixa de mensagem e clica nele 
            position = pt.locateCenterOnScreen('images/paperClip.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(100, 10, duration= self.speed)
            pt.doubleClick(interval= self.click_speed)

            # Relatório para o usuário
            pt.typewrite("*RELATORIO*", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Sua Frase foi verificada e apresenta ", interval=.1)
            pt.typewrite(str(count))
            pt.typewrite(" palavras chaves do nosso banco de dados.", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Por Favor verifique melhor sua fonte para ter mais confiabilidade na sua noticia!\n", interval=.1)
            sleep(1)

        except Exception as e:
            print("Exception (nav_messageBox_Fake): ", e)

    def nav_messageBox_NotFake(self):
        try:
            # Guarda a posição da caixa de mensagem e clica nele 
            position = pt.locateCenterOnScreen('images/paperClip.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(100, 10, duration= self.speed)
            pt.doubleClick(interval= self.click_speed)

            # Mensagem de Nenhuma Palavra Encontrada
            pt.typewrite("*RELATORIO*", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Nenhuma palavra do nosso Banco de Dados foi encontrado no seu texto.", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Entretanto, tenha cuidado com todos as noticias que aparecem!\n", interval=.1)
            sleep(1)

        except Exception as e:
            print("Exception (nav_messageBox_NotFake): ", e)

if __name__ == '__main__':
    # Contador para as palavras chaves
    count = 0
    bot = Whatsapp(speed=.6, click_speed=.4)
    sleep(5)
    # Verifica se tem uma mensagem nova
    bot.verificate_greenDots()
    sleep(3)
    # Pega a mensagem do usuário
    bot.get_userAnswer()
    sleep(3)
    # Verifica se tem no Banco de Dados
    count = bot.verificate_userAnswer()
    if(count > 0):
        bot.nav_messageBox_Fake(count)
    else:
        bot.nav_messageBox_NotFake()