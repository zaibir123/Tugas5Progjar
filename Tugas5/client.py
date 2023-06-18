import socket

server_address = ('localhost', 55555)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
