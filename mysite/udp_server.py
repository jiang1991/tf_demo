import socket
import json

# CMD
cmd = '{"cmd" : "get_data"}'

# res
res_query = '{"mode" : 0,"coin_count" : 1,"game_count" : 1,"game_time" : 120,"music_volume" : 100,"sound_volume" : 100,"resolution" : "1366*768","spare_1" : "spare_value_1","spare_2" : "spare_value_2","spare_3" : "spare_value_3","spare_4" : "spare_value_4","spare_5" : "spare_value_5"}'

res_set = '{"return" : 1}'


def response(data):
    # j = json.load(data)

    if "cmd" in data:
        return res_query
    else:
        return res_set

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('127.0.0.1', 8888))
    print('Bind UDP on 9999...')

    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % (addr, data))
        # s.sendto(b'Hello, %s!' % data, addr)
        s.sendto(bytes(response(data.decode("utf-8")), 'utf-8'), addr)

