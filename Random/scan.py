from scapy.all import *
import time
import os
import csv

def scan_wifi(interface):
    results = []
    sniff(iface=interface, prn=lambda pkt: process_packet(pkt, results), timeout=5)
    return results

def process_packet(packet, results):
    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        ssid = packet[Dot11Elt][0].info.decode(errors='ignore')
        bssid = packet[Dot11].addr2
        rssi = -(256 - ord(packet.notdecoded[-6:-5]))
        channel = int(ord(packet[Dot11Elt:3].info)) if Dot11Elt in packet and packet[Dot11Elt].ID == 3 else "N/A"
        encryption = "Open"
        if packet.haslayer(Dot11Auth):
            encryption = "WEP?"
        if packet.haslayer(Dot11Elt) and packet[Dot11Elt].ID == 48:
            encryption = "WPA"
        if packet.haslayer(Dot11Elt) and packet[Dot11Elt].ID == 221 and packet[Dot11Elt].info.startswith(b'\x00P\xf2\x01\x01\x00'):
            encryption = "WPA2"
        if packet.haslayer(Dot11Elt) and packet[Dot11Elt].ID == 221 and packet[Dot11Elt].info.startswith(b'\x00O\xac'):
            encryption = "WPA3"

        if not any(result['bssid'] == bssid for result in results):
            results.append({'ssid': ssid, 'bssid': bssid, 'rssi': rssi, 'channel': channel, 'encryption': encryption})

def save_to_csv(data, filename="wifi_scan_data.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ssid', 'bssid', 'rssi', 'channel', 'encryption']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
    print(f"\nData saved to {filename}")

if __name__ == "__main__":
    interface = "WiFi"  # Ganti dengan nama interface Wi-Fi kamu
    all_networks = []
    try:
        while True:
            print("Scanning for Wi-Fi networks...")
            networks = scan_wifi(interface)
            if networks:
                print("\nAvailable Wi-Fi Networks:")
                for network in networks:
                    print(f"SSID: {network['ssid']:<30} BSSID: {network['bssid']} RSSI: {network['rssi']:<4} dBm Channel: {network['channel']:<4} Encryption: {network['encryption']}")
                all_networks.extend(networks)
            else:
                print("\nNo Wi-Fi networks found.")
            time.sleep(5)  # Jeda antar pemindaian
    except KeyboardInterrupt:
        print("\nScanning stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if all_networks:
            save_to_csv(all_networks)