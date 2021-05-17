# le epic surver for gaem

import sys
import numpy
import socket
import json

from _thread import start_new_thread


# initalize socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# in case the user did not supply any arguments
fallback = {
  "ip": socket.gethostbyname(''),
  "port": 25454
}

try:
  s.bind((fallback["ip"], fallback["port"]))
except socket.error as e:
  print("Did not bind successfully: " + str(e))

s.listen()
print("Waiting for connection")

currentId = 0
players = {

}

def broadcast(message):
  for i in players:
    i["socket"].send(str.encode(json.dumps(message)))



def threaded_client(conn,id):
    global players

    print("recieving data from player")
    reply = json.loads(conn.recv(2048).decode('utf-8'))

    players[str(id)] = reply
    players[str(id)]["socket"] = conn

    def send(stuff):
      return conn.send(str.encode(json.dumps(stuff)))

    send(currentId)
    
    while True:
        try:
            data = conn.recv(2048)
            reply = json.loads(data.decode('utf-8'))
            
            if not data: 
              # technically speaking if a socket 
              # does not receive data it is considered dead
              conn.send(str.encode("Goodbye"))
              break
            else:
              reply = "hello"
            
            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()


# keep accepting connections until the script
# terminates or the max amount of players connected
while True: 
    conn, addr = s.accept()
    print("Connected to: ", addr)

    currentId += 1

    start_new_thread(threaded_client, (conn,currentId))