
cmd_get_data = '''{
    "cmd" : "get_data"
}'''


cmd_modify_data = '''{
    "cmd": "modify_data",
    "parameter": {
        "team_mode": {
            "music_volume": 100
        },
        "melee_mode": {
            "skill_number": 2
        },
        "football_mode": {
            "game_time": 110
        }
    }
}'''


cmd_set_wifi = '''{
    "cmd": "set_wifi_state",
    "parameter": {
        "wifi_state": 0
    }
}'''


cmd_scan_robot = '''{
    "cmd": "scan_robot"
}'''


cmd_get_robot_info = '''{
    "cmd": "get_robot_info",
    "parameter": {
        "id": 1,
        "ip": "192.168.1.2"
    }
}'''


cmd_set_robot_info = '''{
    "cmd": "set_robot_info",
    "parameter": {
        "id": 1,
        "ip": "192.168.1.2",
        "ssid": "wifi_ssid",
        "password": "wifi_password",
        "control_id": 1
    }
}'''


cmd_pair = '''{
    "cmd": "auto_pairing"
}'''

command = [cmd_get_data, cmd_modify_data, cmd_set_wifi, cmd_scan_robot, cmd_get_robot_info, cmd_set_robot_info, cmd_pair]