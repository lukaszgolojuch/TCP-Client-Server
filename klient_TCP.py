import socket

target_host = "0.0.0.0"
target_port = 9999

#utworzenie obiektu gniazda
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#polaczenie sie z klientem 
client.connect((target_host,target_port))

#wysylanie danych
client.send("GET / HTTP/1.1\r\nConnection succesful...\r\n\r\n")

#odebranie danych
response = client.recv(4096)

print response
