def main():
    print("      _       _____  _______         ______  _______          _        ______  ___  ____ ")  
    print("     / \     |_   _||_   __ \      .' ___  ||_   __ \        / \     .' ___  ||_  ||_  _| ")  
    print("    / _ \      | |    | |__) |    / .'   \_|  | |__) |      / _ \   / .'   \_|  | |_/ /   ")  
    print("   / ___ \     | |    |  __ /     | |         |  __ /      / ___ \  | |         |  __'.   ")  
    print(" _/ /   \ \_  _| |_  _| |  \ \_   \ `.___.'\ _| |  \ \_  _/ /   \ \_\ `.___.'\ _| |  \ \_  ") 
    print("|____| |____||_____||____| |___|   `.____ .'|____| |___||____| |____|`.____ .'|____||____| ") 
    print("Air Crack v.1.0.9 - Author : Malek Mansour - Wifi Hack Tool")
    
import subprocess
import re
import time
import pywifi
from pywifi import PyWiFi
import nmap

# Global variable to store the list of networks
networks = []
selected_network = None

def scan_wifi():
    global networks
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    
    iface.scan()
    time.sleep(2)

    networks = iface.scan_results()

    print("Available Networks:")
    for idx, network in enumerate(networks):
        ssid = network.ssid
        bssid = network.bssid
        signal = network.signal
        print(f"{idx}. SSID: {ssid}, BSSID: {bssid}, Signal: {signal}")


def select_network(index):
    pass

def show_info():
    pass
