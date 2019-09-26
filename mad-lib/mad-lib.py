# encoding: utf-8
# Way 1
# a, b, c, d, e = input("Introduce 4 sustantivos y un verbo separados por espacios. ").split(" ")

# story = "Había una vez un {} que alegraba siempre el {}, te llena de {}, te pega el {} y siempre se {} esta canción".format(a, b, c, d, e)

# print(story)

# Way 2

count = 1
lista = []
print("Introduce 4 sustantivos.")
while count < 5:
    a = input("Introduciendo el sustantivo {}: ".format(str(count)))
    lista.append(a)
    count += 1
a = input("Introduce un verbo: ")
lista.append(a)

story = "Había una vez un {} que alegraba siempre el {}, te llena de {}, te pega el {} y siempre se {} esta canción".format(
    lista[0], lista[1], lista[2], lista[3], lista[4])
print(story)
