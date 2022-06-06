# Navegar até uma nova mensagem (Verde)
# Abrir e copiar a informação que o Usuário mandou
# Verficar o banco de dados para caso haja palavras chaves na frase
# Retornar caso haja ou não palavras iguais

import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
import PIL
from time import sleep
from whatapp import Whatsapp

mouse = Controller()

while(True):

    bot = Whatsapp(speed=.6, click_speed=.4)
    sleep(5)
    bot.verificate_greenDots()
    sleep(3)
    bot.get_userAnswer()
    sleep(3)
    verifica = bot.verificate_userAnswer()
    if(verifica == 1):
        bot.nav_messageBox_Fake()
        bot.nav_vsCode()
        bot.nav_links()
        bot.nav_whatBot()
        bot.nav_chrome()
        bot.nav_links()
        bot.nav_sendLinks()

    elif(verifica == 0):
        bot.nav_messageBox_NotFake()
        bot.nav_vsCode()
        bot.nav_links()
        bot.nav_whatBot()
        bot.nav_chrome()
        bot.nav_links()
        bot.nav_sendLinks()

    elif(verifica == 2):
        bot.close_bug()

    sleep(10)