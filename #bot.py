#bot
#PARA USAR:
#0. CONFIGURAR ARCHIVO lista_nombres.py
#1. ABRIR LA PAGINA DE INSTAGRAM
#2. CORRER EL CODIGO 
#3. TIENES 5 SEGUNDOS PARA POSICIONAR EL CURSOR EN EL CUADRO DE COMENTARIOS
#4. ESPERAR QUE EL BOT TERMINE DE COMENTAR


import random
import time
import pyautogui as pg
from comentarios_nombres import combinaciones_formato as cf


time.sleep(5)

for comentario in cf:
    pg.write(comentario)
    pg.press('enter')
    #time.sleep(35)
