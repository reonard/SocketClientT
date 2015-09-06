__author__ = '01348930'

import socket
import re

HEARTBEAT = "hbSync"

def process_command(cmd_string):
    print cmd_string

HOST, PORT = "10.45.132.131", 9995

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

try:
    while True:
        sock.connect((HOST, PORT))
        sock.sendall("I am connecting !")
        data_buf = sock.recv(1024)
        if data_buf == "Established":
            print "Connected !"
        data = ""
        while True:
            data_buf = sock.recv(1024)
            if not len(data_buf):
                print "Server Disconnected"
                break
            # if HEARTBEAT in data_buf:
            #     send_response()
            #     continue
            data = "".join([data, data_buf])
            matchobj = re.match(r'^command: (.*)End', data_buf, re.I)
            if matchobj is not None:
                cmd = matchobj.group(1)
                process_command(cmd)
                sock.sendall("Result data is xxxxx")
                data = ""
            else:
                continue
except:
    print "Error"
finally:
    sock.close()


