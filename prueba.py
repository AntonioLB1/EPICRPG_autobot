# coding:utf-8
import inspect
import win32api
import os
from PIL import ImageGrab, Image
import pyHook  # Gancho ~
import pythoncom
import pytesseract  # Paquete de texto de reconocimiento de imagen
import pyperclip

# Crear una lista de coordenadas
coordinate = [1, 1, 1, 1]


# Escuchar eventos de teclado
def on_mouse_event(event):
    # Obtener la ruta actual del archivo
    file_ = inspect.getfile(inspect.currentframe())
    dir_path = os.path.abspath(os.path.dirname(file_))
    file_path = dir_path + '/read.jpg'
    # Monitorear eventos del mouse
    if event.MessageName == 'mouse left down':
        coordinate[0:2] = event.Position
        print('mouse left down')
    elif event.MessageName == 'mouse left up':
        coordinate[2:4] = event.Position
        print('mouse left up')
        win32api.PostQuitMessage()  # Salga del ciclo de monitoreo
        # Imagen de coordenadas de intercepción
        pic = ImageGrab.grab(coordinate)
        pic.save(file_path)
        print('jksdhfjksdhfjkdhfkjsdhjk')
        text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')  # Identificar y devolver
        pyperclip.copy(text.replace(' ', ''))  # Importa el contenido reconocido al portapapeles del sistema
    return True


if __name__ == '__main__':
    hm = pyHook.HookManager()  # Crear un objeto de administración de gancho
    hm.MouseAll = on_mouse_event  # Escucha todos los eventos del mouse
    hm.HookMouse()  # Establecer gancho del mouse
    pythoncom.PumpMessages()  # Ingrese al bucle, el programa ha estado escuchando