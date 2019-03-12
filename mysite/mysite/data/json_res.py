
res_get_Data = '''{
"current_mode": "team_mode",
    "team_mode": {
        "coin_count": 1,
        "game_count": 1,
        "game_time": 120,
        "music_volume": 100,
        "sound_volume": 100,
        "resolution": "1366*768",
        "thump_blood": 30,
        "tap_blood": 20,
        "skill_number": 2
    },
    "melee_mode": {
        "coin_count": 1,
        "game_count": 0,
        "game_time": 120,
        "music_volume": 100,
        "sound_volume": 100,
        "resolution": "1366*768",
        "thump_blood": 30,
        "tap_blood": 20,
        "skill_number": 2
    },
    "football_mode": {
        "coin_count": 1,
        "game_count": 1,
        "game_time": 120,
        "music_volume": 100,
        "sound_volume": 100,
        "resolution": "1366*768"
    }
}'''


res_modify_data = '''{
    "return": 1,
    "error_message": "错误信息"
}'''


res_set_wifi = '''{
    "return": 1,
    "error_message": "错误信息"
}'''


res_scan_robot = '''{
    "robot_num": 2,
    "robot_1": {
        "id": 1,
        "ip": "192.168.1.2",
        "ssid": "wifi_ssid",
        "password": "wifi_password"
    },
    "robot_2": {
        "id": 2,
        "ip": "192.168.1.3",
        "ssid": "wifi_ssid",
        "password": "wifi_password"
    }
}'''


res_get_robot_info = '''{
    "id": 1,
    "ip": "192.168.1.2",
    "ssid": "wifi_ssid",
    "password": "wifi_password",
    "control_id": 1
}'''


res_set_robot_info = '''{
    "return": 1,
    "error_message": "错误信息"
}'''


res_pair = '''{
    "return": 1,
    "error_message": "错误信息"
}'''

response = [res_get_Data, res_modify_data, res_set_wifi, res_scan_robot, res_get_robot_info, res_set_robot_info, res_pair]