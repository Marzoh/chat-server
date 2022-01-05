#!/usr/bin/env python3

import socket

nickname = input("Enter A User Nickname: ")
host = input("Enter IP To Connect To: ")
port = input("Enter The Server Port Number: ")
try:
    port = int(port)
except ValueError:
    exit()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((host, port))
    except socket.error as e:
        print(str(e))
    
    print("[+] Client Connected To The Server!")

    while True:
        data = s.recv(1024).decode()
        if data:
            print(data)
        else:
            pass
        msg = input(f"[{nickname}]: ")
        thing = ("[" + nickname + "]" + ": " + msg).encode("utf-8")
        s.send(thing)