# pertama kita membuat server terlebih dahulu yang akan menerima koneksi dari client
import socket # import dulu modul socket'

listenersocket = socket.socket()
serverip = '0.0.0.0'
serverport = 2222
listenersocket.bind((serverip,serverport)) # menerima koneksi
listenersocket.listen(0)
print 'server siap di gunakan'
while True:
	handlerSocket, adrr = listenersocket.accept()
	print 'sebuah client baru terkoneksi dengan alamat : ',adrr
	while True:
		pesan = raw_input('masukan pesan anda : ')
		handlerSocket.send(pesan)
		pesan = handlerSocket.recv(1024)
		print 'pesan dari client : ',pesan
		pass
	pass

