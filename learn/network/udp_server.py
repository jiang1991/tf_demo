import socket


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('127.0.0.1', 9999))
    print('Bind UDP on 9999...')

    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % (addr, data))
        s.sendto(b'Hello, %s!' % data, addr)

