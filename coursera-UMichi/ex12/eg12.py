# https://www.coursera.org/learn/python-network-data/lecture/e731e/12-1-networked-technology

# make phone call to web server

import socket
# make a gateway
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the gateway
mysock.connect(('data.pr4e.org', 80)) # host, port
# prepare a command
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# send command
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print(data.decode())
mysock.close()