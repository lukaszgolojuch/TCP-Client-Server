import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

#watek do obslugi klienta
def handle_client(client_socket):

    #drukuje informacje przesylanie przez klienta
    request = client_socket.recv(1024)

    print "[*] Odebrano: %s" % request

    #wysyla pakiet powrotny
    client_socket.send("Connection Correct!")

    client_socket.close()

while True:
    

    print "[*] Nasluchiwanie na porcie %s:%d" % (bind_ip, bind_port)

    client,addr = server.accept()

    print "[*] Przyjeto polaczenie od: %s:%d" % (addr[0],addr[1])

    #utworzenie watku klienta do obslugi przychodzacych danych
    client_handler = threading.Thread(target = handle_client, args=(client,))
    client_handler.start()
