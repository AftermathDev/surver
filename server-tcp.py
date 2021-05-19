# le epic surver for gaem

import sys
import numpy
import socket
import json

from OpenSSL import SSL as ssl # as much as i hate ssl i have to do this or else the web browser blocks any connections
from time import sleep

from _thread import start_new_thread


# initalize socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# in case the user did not supply any arguments
fallback = {
  "ip": socket.gethostbyname(''),
  "port": 25453
}

not_connected = not False

while not_connected == True:
    try:
      s.bind((fallback["ip"], fallback["port"]))
      not_connected = False
    except socket.error as e:
      print("Did not bind successfully: " + str(e))
      print("waiting 5 seconds before next attempt")
      sleep(5)



s.listen()
print("Waiting for connection")

currentId = 0
players = {

}

def broadcast(message):
  for i in players:
    i["socket"].send(str.encode(json.dumps(message)))


reply = ""
def threaded_client(conn,id):
    global players

    print("recieving data from player")
    #reply = conn.recv(2048).decode('utf-8')

    #players[str(id)] = reply
    #players[str(id)]["socket"] = conn

    conn.send(str.encode("hello"))

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            print("got back " + reply)
            if not data:
              # technically speaking if a socket
              # does not receive data it is considered dead
              conn.send(str.encode("Goodbye"))
              break
            else:
              reply = "hello"

            print("sending " + reply)
            conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
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
