# encoding: utf-8
import random


lista = ["cenutrio", "ceporro", "zopenco", "chichinabo",
         "calamandurrio", "topacio", "meloncio", "cazurro"]
palabra = ""
encontradas = set()
letras = set()
vidas = 5
find = False


def elige_palabra():
    global palabra
    length = len(lista)
    num = random.randint(0, length-1)
    palabra = lista[num]


def muestra_huecos():
    global palabra
    global encontradas
    resultado = ""
    for i in range(len(palabra)):
        if(palabra[i] in encontradas):
            resultado += palabra[i]
        else:
            resultado += "-"
        resultado += " "
    print(resultado)
    

def elige_letra(letra):
    global letras
    #letra = input("Elige la letra que quieras: ")
    if letra in letras:
        #print("Ya has elegido esa letra. Prueba otra vez.")
        return False
    else:
        return True
    
def comprueba_letra(letra):
    global palabra
    if letra in palabra:
        return True
    else:
        return False

def comprueba_fin():
    for letra in palabra:
        if letra  not in encontradas:
            return False
    return True
            



print("Este es el juego del ahorcado. Se va a elegir una palabra aleatoria y debes adivinarla.")
elige_palabra()
print("Ahora mismo tienes {} vidas".format(vidas))
while find == False and vidas > 0:    
    print("Esto es lo que has descubierto: ")
    muestra_huecos()
    letra = input("Elige la letra que quieras probar: ")
    if elige_letra(letra) == False:
        print("Ya has cogido esa letra antes. Prueba otra.")
        print("")
        continue
    else:
        letras.add(letra)
        if comprueba_letra(letra) == False:
            vidas += -1
            print("Lástima, esa letra no estaba.")
            print("Te quedan {} vidas.".format(vidas))
            print("")
            continue
        else:
            encontradas.add(letra)
            print("Muy bien, has acertado.")
            print("")
            find = comprueba_fin()
            continue

if vidas == 0:
    print("""Oh no! Te has quedado sin vidas. La palabra era {}. Gracias por jugar!""".format(palabra))
elif find == True:
    print("Enhorabuena! Has encontrado la palabra. Gracias por jugar!")

        



    # if type(letra) is not str:
    #     print("Tienes que elegir una letra")

