# membuat listener di sisi client

import socket

handlerSocket = socket.socket()
serverip = "127.0.0.1" # karena saya menguji coba nya di satu komputer maka saya menggunakan ip lokal
serverport = 2222

handlerSocket.connect((serverip, serverport))
print 'terkoneksi dengan server'
while True:
	pesan = handlerSocket.recv(1024)
	print 'pesan dari server : ',pesan
	pesan = raw_input('masukan pesan anda :')
	handlerSocket.send(pesan)
	pass