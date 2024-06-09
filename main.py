import subprocess
import re
import time
import pywifi
from pywifi import PyWiFi
import nmap

def main():
    print("      _       _____  _______         ______  _______          _        ______  ___  ____ ")  
    print("     / \     |_   _||_   __ \      .' ___  ||_   __ \        / \     .' ___  ||_  ||_  _| ")  
    print("    / _ \      | |    | |__) |    / .'   \_|  | |__) |      / _ \   / .'   \_|  | |_/ /   ")  
    print("   / ___ \     | |    |  __ /     | |         |  __ /      / ___ \  | |         |  __'.   ")  
    print(" _/ /   \ \_  _| |_  _| |  \ \_   \ `.___.'\ _| |  \ \_  _/ /   \ \_\ `.___.'\ _| |  \ \_  ") 
    print("|____| |____||_____||____| |___|   `.____ .'|____| |___||____| |____|`.____ .'|____||____| ") 
    print("Air Crack v.1.1.0 - Author : Malek Mansour - Wifi Hack Tool")

# Global variables
networks = []
selected_network = None

# Scan Wifi
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
    global selected_network
    if index < 0 or index >= len(networks):
        print("Invalid index")
        return
    
    selected_network = networks[index]
    print(f"Selected Network: SSID: {selected_network.ssid}, BSSID: {selected_network.bssid}")

def show_info():
    if selected_network is None:
        print("No network selected")
        return
    
    ssid = selected_network.ssid
    bssid = selected_network.bssid
    signal = selected_network.signal
    freq = selected_network.freq
    akm = selected_network.akm
    cipher = selected_network.cipher
    print(f"Network Info:\nSSID: {ssid}\nBSSID: {bssid}\nSignal: {signal}\nFrequency: {freq} MHz\nAKM: {akm}\nCipher: {cipher}")

def get_default_gateway():
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        output = result.stdout

        lines = output.splitlines()
        gateway = None

        for line in lines:
            if "Default Gateway" in line:
                parts = line.split()
                if len(parts) > 2 and re.match(r"^\d{1,3}(\.\d{1,3}){3}$", parts[-1]):
                    gateway = parts[-1]
                    break

        return gateway
    except Exception as e:
        print(f"Error obtaining default gateway: {e}")
        return None

def scan_local_network():
    nm = nmap.PortScanner()
    gateway = get_default_gateway()
    if gateway:
        ip_parts = gateway.split('.')[:-1]
        subnet = '.'.join(ip_parts) + '.0/24'
        nm.scan(hosts=subnet, arguments='-sn')
    
        print("Connected Devices:")
        for host in nm.all_hosts():
            if 'mac' in nm[host]['addresses']:
                mac = nm[host]['addresses']['mac']
                print(f"IP: {host}, MAC: {mac}")
            else:
                print(f"IP: {host}, MAC: Not available")
    else:
        print("Unable to determine the default gateway. Please provide the subnet manually.")

def clear_interface():
    print("\033[H\033[J", end="")
