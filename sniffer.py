from scapy.all import sniff, IP, TCP, Raw
import sys

# Global counter for packets captured
packet_count = 0

def process_packet(packet):
    """
    Callback function to handle each captured packet.
    Extracts and displays Source IP, Destination IP, Protocol, and Payload.
    """
    global packet_count
    
    # Check if the packet has an IP layer (to avoid errors with other layers)
    if IP in packet:
        packet_count += 1
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP"  # Since we're filtering for TCP
        
        # Display packet information in a clean, readable format
        print(f"\n[+] Packet #{packet_count}:")
        print(f"    Source IP:      {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    Protocol:       {protocol}")
        
        # Check if the packet has a Payload (Raw layer)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            # Try to decode the payload for human readability, otherwise show hex
            try:
                decoded_payload = payload.decode('utf-8', errors='replace')
                print(f"    Payload:        {decoded_payload[:100]}...") # Limit display to 100 chars
            except Exception:
                print(f"    Payload (Hex):  {payload.hex()[:100]}...")
        else:
            print("    Payload:        None")

def start_sniffer(interface=None):
    """
    Starts the network sniffer.
    Handles permissions and captures only TCP packets.
    """
    print("--- Starting Basic Network Sniffer ---")
    print("--- Filtering for TCP packets only ---")
    print("--- Press Ctrl+C to stop ---\n")
    
    try:
        # Start sniffing
        # filter="tcp" ensures only TCP packets are captured at the kernel level
        # prn is the callback function called for each packet
        # store=0 prevents storing packets in memory to save resources
        sniff(filter="tcp", prn=process_packet, iface=interface, store=0)
    except PermissionError:
        print("[!] Error: Permission denied. Please run as Administrator (Windows) or root (Linux).")
        sys.exit(1)
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n--- Sniffing stopped. Total packets captured: {packet_count} ---")
        sys.exit(0)

if __name__ == "__main__":
    # You can specify an interface like 'eth0' or 'wlan0' if needed
    # Default is None, which sniffs on all available interfaces
    start_sniffer()
