
import keyboard
from time import sleep
import os
import json
from PIL import ImageGrab, Image
import inspect
import win32api
import os
from PIL import ImageGrab, Image
import pytesseract  # Paquete de texto de reconocimiento de imagen

ancho = win32api.GetSystemMetrics(0)
alto = win32api.GetSystemMetrics(1)
file_ = inspect.getfile(inspect.currentframe())
dir_path = os.path.abspath(os.path.dirname(file_))
pytesseract.pytesseract.tesseract_cmd = "C:"+ os.sep + "Program Files"+ os.sep + "Tesseract-OCR"+ os.sep + "tesseract.exe"
coordinate = [int(ancho*0.1), int(alto*0.7), int(ancho*0.9), alto-10]
    
def inJail():
    pic = ImageGrab.grab(coordinate)
    text = pytesseract.image_to_string(pic)
    if (text.find('jail') == -1 ) or (text.find('rpg rules')):
        print("Estás en la carcel, pulsa ENTER para continuar.")
        keyboard.wait('Enter')


what = 'chop'
total = {"hunt":0, "heal":0, "chop":0, "farm":0, "adv":0}


def info():
    os.system("cls")
    print("PARA SALIR PULSE CTRL+C EN ESTA VENTANA O CIERRELA")
    print("Pongase en la linea de entrada y pulse Enter para que el programa empiece.")
    print()
    total_t = 0
    for key, value in total.items():
        total_t += value
        key_ = key
        if key == "chop":
            key_ = what
        print(key_ + ": " + str(value))
    
    print("-------------")
    print("Total hechos: " +  str(total_t))


def autoBot(params:dict):  # pickup axe net
    global what
    what = params["chop"]["what"]
    info()
    keyboard.wait('enter')  # enter to start
    count_heal = 0
    count_chop = 800
    count_adv = 800
    count_farm = 800
    count_buy = 0
    count_adv_heal = 0
    while True:
        
        inJail()
            
        if params["hunt"]["do"]:
            sleep(1.2)
            keyboard.write("rpg hunt")
            keyboard.send("enter")
            total["hunt"] += 1
            count_heal += 1
            info()
            
        if params["hunt"]["heal"] and count_heal >= params["hunt"]["frequency_hunt_per_heal"]:
            count_heal = 1
            sleep(1.2)
            keyboard.write("rpg heal")
            keyboard.send("enter")
            total["heal"] += 1
            count_buy += 1
            info()
        
        if params["hunt"]["buy_lifepotion"] and count_buy >= params["hunt"]["lifepotion_per_buy"]:
            count_buy = 1
            sleep(1.2)
            keyboard.write("rpg buy life potion " + params["hunt"]["lifepotion_per_buy"])
            keyboard.send("enter")
            info()
            
        if params["chop"]["do"] and count_chop >= 5:
            count_chop = 1
            sleep(1.2)
            keyboard.write("rpg " + params["chop"]["what"])
            keyboard.send("enter")
            total["chop"] += 1
            info()
        else:
            count_chop += 1
            
        if params["farm"]["do"] and count_farm >= 10:
            if params["farm"]["buy_seed"]:
                sleep(1.2)
                keyboard.write("rpg buy seed 1")
                keyboard.send("enter")
            count_farm = 1
            sleep(1.2)
            keyboard.write("rpg farm ")
            if not params["farm"]["buy_seed"]:
                keyboard.write(params["farm"]["what"])
            keyboard.send("enter")
            total["farm"] += 1
            info()
        else:
            count_farm += 1 
              
        inJail()
            
        if params["adventure"]["do"] and count_adv >= params["adventure"]["try_frecuency"]:
            count_adv = 1
            if params["adventure"]["heal_before"] and params["adventure"]["trys_until_heal_before"] >= count_adv_heal:
                sleep(1.2)
                keyboard.write("rpg heal")
                keyboard.send("enter")
                count_heal += 1
                count_adv_heal = 1
                total["heal"] += 1
            else:
                count_adv_heal += 1
            
            sleep(1.2)
            keyboard.write("rpg adv")
            keyboard.send("enter")
            total["adv"] += 1
            info()
            
            if params["adventure"]["heal_after"]:
                sleep(1.2)
                keyboard.write("rpg heal")
                keyboard.send("enter")
                count_heal += 1
                total["heal"] += 1
        else:
            count_adv += 1
            
        sleep(params["hunt"]["time_per_hunt"]+1)


if __name__ == '__main__':
    with open('params_AutobotRPG.json', 'r') as f:
        params = json.load(f)
        autoBot(params)
