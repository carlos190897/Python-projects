# encoding: utf-8
import random
import os

game = "y"
while game == "y":
    find = "n"
    num = 0
    x = random.randint(1, 10)
    while num == 0:
        try:    
            num = int(input("Intenta adivinar el número en el que estoy pensando. "))
        except ValueError:
            print("Debes introducir un número.")
    while find == "n":
        if num == x:
            game = input("Enhorabuena! Has acertado!!! Quieres volver a jugar? ")
            x = random.randint(1, 10)
            find = "y"
            os.system('clear')
        elif num > x:
            num = int(input("Te has pasado, prueba otra vez. "))
        elif num < x:
            num = int(input("Te has quedado corto, prueba otra vez. "))