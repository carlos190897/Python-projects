# encoding: utf-8
import random

dice = True
try:
    caras = int(input("Introduce el numero de caras del dado: "))
except NameError:
        print("Es necesario introducir un número")
while dice == True:
    num = random.randint(1, caras)
    print("El número aleatorio es: "+str(num))
    dice = bool(input("Quieres volver a tirar (1/0)? "))
    cambio = bool(input("Quieres cambiar el numero de caras (1/0)? "))
    if cambio == True:
        caras = int(input("Introduce el numero de caras del dado: "))