
import sys
import socket

host, port = 'localhost', 6666
msg = 'hello there # '
data = ' '.join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(bytes(msg + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(s.recv(1024), "utf-8")

print("Sent:     {}".format(msg))
print("Received: {}".format(received))
