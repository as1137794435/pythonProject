# -*- utf-8 -*-
# @Time: 2022/7/1 9:56
# @Author: Heilian
# @File: server.py
# @Software: PyCharm

import socket
import threading


def client_data(client_socket):
    while True:
        # Receive data
        recv_data = client_socket.recv(1024)
        print(recv_data)
        # return data
        data = 'Hello client'
        client_socket.send(data.encode())

# Encapsulates methods for processing client data


# Create object
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Bind an IP address and a port ifconfig
server.bind(('192.168.14.26',8003))
# set the number of listeners
server.listen(5)
print('server starts')
# wait for connection of client
while True:
    # Waiting for the client to connect
    client_socket, addr = server.accept()
    print('client socket',client_socket)
    print('client address',addr)
    # Create threads to handle requests from each client
    t = threading.Thread(target=client_data,args = (client_socket,))
    t.start()
# close
server.close()