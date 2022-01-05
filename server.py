#!/usr/bin/env python3

import socket

nickname = input("Enter A User Nickname: ")
host = input("Enter Server Host IP: ")
port = input("Enter Server Host Port: ")
try:
	port = int(port)
except ValueError:
	exit()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.bind((host, port))
	except socket.error as e:
		print(str(e))
	
	print("[+] Server Started! Listening For A Connection...")
	s.listen()

	while True:
		conn, addr = s.accept()

		with conn:
			print("[+] Client Connected From", addr)

			while True:
				msg = input(f"[{nickname}]: ")
				data = ("[" + nickname + "]" + ": " + msg).encode("utf-8")
				conn.send(data)
				data2 = conn.recv(1024).decode()

				if data2:
					print(data2)
				else:
					pass