# le epic surver for gaem

import sys
import numpy
import socketio

from _thread import start_new_thread


# initalize socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# in case the user did not supply any arguments
fallback = {
  "ip": socket.gethostbyname(''),
  "port": 25454
}

try:
  s.bind(fallback.ip, fallback.port)
except socket.error as e:
  print("Did not bind successfully: " + str(e))

s.listen(30)
print("Waiting for connection")

currentId = 0
pos = {}
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                reply = pos[nid][:]
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))