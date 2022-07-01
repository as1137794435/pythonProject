# -*- utf-8 -*-
# @Time: 2022/7/1 9:25
# @Author: Heilian
# @File: client.py
# @Software: PyCharm

import socket
# Create a Socket object(IPV4,TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
client.connect(('192.163.14.51',8002))
# send data, byte type data.encoude()
data = b'hello server'
client.send(data)
# Receive returned data (size)
recv_data = client.recv(1024)
# Convert byte to a string
str_data = recv_data.decode()
# Close client
client.close()

