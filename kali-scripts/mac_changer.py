#!/usr/bin/env python3
# encoding: utf-8


import subprocess
import optparse
import re

# Si queremos cambiar nuestra MAC usaremos estos comandos:
#     ifconfig eth0 down
#     ifconfig eth0 hw ether 00:11:22:33:44:55
#     ifconfig eth0 up
#     ifconfig
# Si queremos reiniciar nuestra MAC usaremos este comandos
#     sudo ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')

# TODO:Meter también la opción de reiniciar

def reset_mac(interface):
    mac = subprocess.check_output(["sudo","ethtool","-P", interface]).decode("utf-8")
    regex_mac_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac)
    change_mac(interface,regex_mac_search_result.group(0))

def get_arguments():  # Funcion para pillar los argumentos del script
    parser = optparse.OptionParser()
    # El parser aceptará los atributos -i -m que estarán ligados con los atributos interface y new_mac
    parser.add_option("-i", "--interface", dest="interface",
                      help="Specify the interface of which you want to change the MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="Specify a random MAC address you would like to the interface to use.")
    parser.add_option("-r", "--reset", dest="reset", default="",
                      help="Reset yout MAC address to your original MAC address")
    # Aquí parseamos lo que hemos metido en el script
    (options, arguments) = parser.parse_args()
    # Validamos que estos dos valores tiene que estar
    if not options.interface:
        parser.error(
            "[-] Error: interface not specified, use --help for more info.")
    if not options.new_mac and not options.reset:
        parser.error(
            "[-] Error: MAC address not specified, you should specify your new MAC address using -m or use -r to restart it")
    return options


def change_mac(interface, new_mac):  # Función para cambiar la dirección MAC
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # Subprocess.call permite lanzar un comando de terminal desde el script
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):  # Función para ver la dirección MAC actual
    # Subprocess.check_output coge el resultado de lanzar en terminal un comando
    ifconfig_result = subprocess.check_output(
        ["ifconfig", interface], shell=True).decode("utf-8")
    # Como no queremos el mensaje entero sino que queremos solo la dirección buscamos dentro del mensaje la dirección MAC con expresiones regulares
    # re.search() busca el primer argumento en el texto del segundo argumento y devuelve True o False. 'r' Indica que no es un string sino una expresión regular. \w hace referencia a caracteres alfanuméricos
    regex_mac_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if regex_mac_search_result:
        # group(0) en este caso es la cadena con la que ha encontrado coincidencia
        return regex_mac_search_result.group(0)
    else:
        print("[-] Error: could not read MAC address.")


options = get_arguments()

if options.reset:
    current_mac = get_current_mac(options.interface)
    print("The current MAC Address = " + str(current_mac))
    reset_mac(options.interface)
    current_mac = get_current_mac(options.interface)
    print("[+] The MAC address successfully changed to " + current_mac)
else:
    current_mac = get_current_mac(options.interface)
    print("The current MAC Address = " + str(current_mac))
    change_mac(options.interface, options.new_mac)
    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] The MAC address successfully changed to " + current_mac)
    else:
        print("[-] Error: the MAC address did not get changed.")
