import socket

# CMD
cmd = '{"cmd" : "get_data"}'

# res
res_query = '{"mode" : 0,"coin_count" : 1,"game_count" : 1,"game_time" : 120,"music_volume" : 100,"sound_volume" : 100,"resolution" : "1366*768","spare_1" : "spare_value_1","spare_2" : "spare_value_2","spare_3" : "spare_value_3","spare_4" : "spare_value_4","spare_5" : "spare_value_5"}'

res_set = '{"return" : 1}'

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # for data in [b'Michael', b'Tracy', b'Sarah']:
    #
    #     s.sendto(data, ('193.169.2.22', 8080))
    #     print(s.recv(1024).decode('utf-8'))

    s.sendto(bytes(cmd, 'utf-8'), ('127.0.0.1', 8888))
    print(s.recv(1024).decode('utf-8'))
    s.close()

    # s.sendto(bytes(res_query, 'utf-8'), ('127.0.0.1', 8888))
    # print(s.recv(1024).decode('utf-8'))
    # s.close()

    # while True:
    #     print(s.recv(4096).decode('utf-8'))
    #     s.close()

