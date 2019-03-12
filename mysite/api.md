## 读取数据库

```json
{
    "cmd" : "get_data"
}
```

```json
{
    "current_mode": "melee_mode",
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
}
```

## 设置数据库

```json
{
    "cmd": "modify_data",
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
```

```json
{
    "return": 1,
    "error_message": "错误信息"
}
```

## 打开/配置 wifi

```json
{
    "cmd": "set_wifi_state",
    "parameter": {
        "wifi_state": 0
    }
}
```

```json
{
    "return": 1,
    "error_message": "错误信息"
}
```

## Scan Robots

```json
{
    "cmd": "scan_robot"
}
```

```json
{
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
}
```

## get robot info

```json
{
    "cmd": "get_robot_info",
    "parameter": {
        "id": 1,
        "ip": "192.168.1.2"
    }
}
```

```json
{
    "id": 1,
    "ip": "192.168.1.2",
    "ssid": "wifi_ssid",
    "password": "wifi_password",
    "control_id": 1
}
```

## set robot info

```json
{
    "cmd": "set_robot_info",
    "parameter": {
        "id": 1,
        "ip": "192.168.1.2",
        "ssid": "wifi_ssid",
        "password": "wifi_password",
        "control_id": 1
    }
}
```

```json
{
    "return": 1,
    "error_message": "错误信息"
}
```

## pair

```json
{
    "cmd": "auto_pairing"
}
```

```json
{
    "return": 1,
    "error_message": "错误信息"
}
```

