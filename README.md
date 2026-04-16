# Python Network Sniffer

A basic, beginner-friendly network sniffer built using Python and the Scapy library. This tool captures live network packets, filters for TCP traffic, and displays essential information such as source/destination IP addresses, protocols, and payloads.

## Features
- **Live Packet Capture:** Uses Scapy to intercept real-time traffic.
- **TCP Filtering:** Specifically captures and displays only TCP packets.
- **Modular Design:** Functions for both packet processing and the sniffer engine.
- **Error Handling:** Gracefully handles permission issues and user interruptions (Ctrl+C).
- **Clean Output:** Formatted displays showing packet count and key metadata.
- **Beginner-Friendly:** Well-commented code for easy learning.

## Requirements
- Python 3.x
- Scapy library
- Npcap (Windows only - required for packet capturing)
- `tcpdump` or root privileges (Linux/macOS)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-network-sniffer.git
   cd python-network-sniffer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Npcap (Windows users):**
   Download and install [Npcap](https://npcap.com/#download). Ensure "Install Npcap in WinPcap API-compatible Mode" is selected during installation.

## How to Run

### Windows
Open your terminal (Command Prompt or PowerShell) **as an Administrator** and run:
```bash
python sniffer.py
```

### Linux / macOS
Use `sudo` to run the script with root privileges:
```bash
sudo python3 sniffer.py
```

## How the Code Works

1. **Scapy Integration:** The project uses the `sniff()` function from Scapy to capture live traffic.
2. **Filtering:** We apply a `filter="tcp"` to ensure only TCP-based packets are processed, keeping the output focused and efficient.
3. **Packet Processing:** The `process_packet` function acts as a callback. For every packet captured:
   - It checks for an `IP` layer to extract source and destination addresses.
   - It looks for a `Raw` layer to extract the packet's payload.
   - It safely attempts to decode the payload into human-readable text.
4. **Error Handling:** The `start_sniffer` function is wrapped in a try-except block to catch `PermissionError` (common if not running as admin/root) and `KeyboardInterrupt` (to allow clean exits).

## Output Example
```
--- Starting Basic Network Sniffer ---
--- Filtering for TCP packets only ---
--- Press Ctrl+C to stop ---

[+] Packet #1:
    Source IP:      192.168.1.5
    Destination IP: 142.250.190.46
    Protocol:       TCP
    Payload:        GET / HTTP/1.1...
```

## Disclaimer
This tool is for educational purposes only. Unauthorized network sniffing may violate local laws and organizational policies. Use it responsibly on networks you own or have explicit permission to monitor.
