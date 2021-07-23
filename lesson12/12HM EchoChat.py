import socket
import time
import json
import re


host = '0.0.0.0'
port = 35200
clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
quit = False
print('[Server Started]')

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            name = re.findall(r"\w+", data.decode('utf-8'))
            clients.update({addr: name[0]})
            print(clients)
        itsattime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
        print(addr, itsattime, end="")
        print(data.decode("utf-8"))
        name = re.findall(r"\w+", data.decode('utf-8'))
        print(name[1])
        if name[1] in clients.values():
            for addr_n, name_i in clients.items():
                print(name[1], name)
                if name[1] == name_i:

                    s.sendto(data, addr_n)

        else:
            for client in clients:
                if addr != client:
                    s.sendto(data, client)

    except Exception as ex:
        print(ex)
        print('\n[ Server Stopped ]')
        quit = True

s.close()