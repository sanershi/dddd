import socket
import threading

# Sunucunun IP adresi ve portu
HOST = "45.133.36.238"
PORT = 9987

# TCP soketi oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# İstemci bağlantısını kabul et
def handle_client(client_socket, client_address):
    print(f'{client_address} bağlandı.')
    
    while True:
        # İstemciden veri al
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        
        print(f'Alındı: {data}')
        
        # İstemciye cevap gönder
        response = f'Eko: {data}'
        client_socket.send(response.encode('utf-8'))
    
def test(ip, port):
    server_socket.sendto(b"", (ip, port))

while True:
    # İstemci bağlantısını kabul et
    client_socket, client_address = server_socket.accept()
    
    # Her istemci için bir threading başlat
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
    client_thread2 = threading.Thread(target=test, args=(HOST, PORT))
    client_thread2.start()
