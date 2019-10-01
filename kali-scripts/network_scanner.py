#!/usr/bin/env python3
# encoding: utf-8
import scapy.layers.l2 as  scapy
#from scapy.all import ARP, Ether, srp
import argparse


# Este programa podría ser sustituído por Nmap

# 1 - ARP request enviado a todas las maquinas de la red
# 1.1 - arp_request = scapy.ARP(pdst=ip) → Sends ARP request
# 1.2 - print(arp_request.summary()) → Prints ARP request message
# 1.3 - scapy.ls(scapy.ARP()) → Lists out all commands you can execute within the .ARP class
# 2 - Enviamos paquete y recibimos respuesta
# 3 - Parseamos la respuesta
# 4 - Imprimimos resultado


def scan(ip):  # Función que dado una IP o un rango de IP escanea una subred
    # Creamos un objeto ARP con la dirección IP objetivo
    arp_request = scapy.ARP(pdst=ip)
    # Lo vamos a enviar por broadcast, por eso ponemos como mac todo 1
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # scapy.srp() envía el paquete arp_request_broadcast y mete en answered_list las respuestas
    # [0] permite listar solo las respuestas
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):  # Función para imprimir los resultados de scap(ip)
    print("IP\t\t\tMAC Address")
    print("----------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

def get_arguments(): # Funcion para pillar los argumentos del script
    parser = argparse.ArgumentParser()
    #El parser aceptará el argumento -y para indicar la IP o el rango
    parser.add_argument("-t", "--target", dest="target",
                        help="Target IP/IP Range")
    options = parser.parse_args()
    return options

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)