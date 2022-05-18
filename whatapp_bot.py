# Navegar até uma nova mensagem (Verde)
# Abrir e copiar a informação que o Usuário mandou
# Verficar o banco de dados para caso haja palavras chaves na frase
# Retornar caso haja ou não palavras iguais

import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
import PIL
from time import sleep

mouse = Controller()

class Whatsapp:
    
    def __init__(self, speed = .5, click_speed = .3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.count = 0

    def verificate_greenDots(self):
        try:
            
            position = 0
            position = pt.locateCenterOnScreen('images/greenDot.png', confidence=0.7)
            if(position != 0):
                pt.moveTo(position, duration= self.speed)
                pt.moveRel(-100, 0, duration= self.speed)
                pt.doubleClick(interval= self.click_speed)
                return True
            else:
                return False
        except Exception as e:
            print("Exception (verificate_greenDots): ", e)

    def get_userAnswer(self):
        try:
            
            position = pt.locateCenterOnScreen('images/paperClip.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(20, -80, duration= self.speed)

            mouse.click(Button.left, 3)
            sleep(self.speed)
            pt.hotkey('ctrl', 'c')

            self.message = pc.paste()

        except Exception as e:
            print("Exception (nav_messageBox): ", e)

    def verificate_userAnswer(self):
        try:
            file = open("bd.txt", "r")
            list_phrase = self.message.split(" ")
            list_bd = file.readlines()
            print(list_phrase)
            self.count = 0

            for i in range(len(list_bd)):
                list_bd[i] = list_bd[i].replace("\n", "")

            for i in range(len(list_phrase)):
                j = 0
                while(j < len(list_bd)):
                    if(list_phrase[i] == list_bd[j]):
                        self.count += 1
                    j += 1

            file.close()
            if(self.count > 0 and list_phrase[0] != ""):
                return 1
            elif(self.count == 0 and list_phrase[0] != ""):
                return 0
            elif(self.count == 0 and list_phrase[0] == ""):
                return 2

        except Exception as e:
            print("Exception (verificate_userAnswer): ", e) 

    def nav_messageBox_Fake(self):
        try:
            
            position = pt.locateCenterOnScreen('images/paperClip.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(100, 10, duration= self.speed)
            pt.doubleClick(interval= self.click_speed)

            pt.typewrite("*RELATORIO*", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Sua Frase foi verificada e apresenta ", interval=.1)
            pt.typewrite(str(self.count))
            pt.typewrite(" palavras chaves do nosso banco de dados.", interval=.1)
            pt.hotkey("shift", "enter")
            sleep(1)
            pt.typewrite("Por Favor verifique melhor sua fonte para ter mais confiabilidade na sua noticia!\n", interval=.1)
            sleep(1)

        except Exception as e:
            print("Exception (nav_messageBox_Fake): ", e)

    def nav_messageBox_NotFake(self):
        try:
            
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

    def close_bug(self):
        try:
             
            position = pt.locateCenterOnScreen('images/xButton.png', confidence=0.7)
            pt.moveTo(position, duration= self.speed)
            pt.moveRel(10, 10, duration= self.speed)
            pt.doubleClick(interval= self.click_speed)
            mouse.click(Button.left, 1)

        except Exception as e:
            print("Exception (close_bug): ", e)

if __name__ == '__main__':

    while(True):
        count = 0
        bot = Whatsapp(speed=.6, click_speed=.4)
        sleep(5)
        verifica = bot.verificate_greenDots()
        sleep(3)
        if(verifica == True):
            bot.get_userAnswer()
            sleep(3)
            veri_ = bot.verificate_userAnswer()
            if(veri_ == 1):
                bot.nav_messageBox_Fake()
            elif(veri_ == 0):
                bot.nav_messageBox_NotFake()
            elif(veri_ == 2):
                bot.close_bug()

        count = 0
        sleep(10)