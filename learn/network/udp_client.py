import socket


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # for data in [b'Michael', b'Tracy', b'Sarah']:
    #
    #     s.sendto(data, ('193.169.2.22', 8080))
    #     print(s.recv(1024).decode('utf-8'))

    s.sendto(b'ok', ('193.169.2.22', 8080))

    while True:
        print(s.recv(1024).decode('utf-8'))

    # s.close()
