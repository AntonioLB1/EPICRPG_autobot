
from PIL import ImageGrab, Image
import inspect
import win32api
import os
from PIL import ImageGrab, Image
import pyHook  # Gancho ~
import pythoncom
import pytesseract  # Paquete de texto de reconocimiento de imagen
import pyperclip

file_ = inspect.getfile(inspect.currentframe())
dir_path = os.path.abspath(os.path.dirname(file_))
file_path = dir_path + os.sep +'read.jpg'

print(file_path)
ancho = win32api.GetSystemMetrics(0)
alto = win32api.GetSystemMetrics(1)
coordinate = [int(ancho*0.1), int(alto*0.7), int(ancho*0.9), alto-10]
pic = ImageGrab.grab(coordinate)
pic.save(file_path)
pytesseract.pytesseract.tesseract_cmd = "C:"+ os.sep + "Program Files"+ os.sep + "Tesseract-OCR"+ os.sep + "tesseract.exe"
text = pytesseract.image_to_string(pic)
with open('texto.txt', 'w') as f:
    f.write(text)
    f.close()
print(text.find('jail'))