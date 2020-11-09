# -*- coding:utf8 -*-

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    res = ''

    cmd = 'get_data'

    res = '''{
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
}'''

    # res = 'hello'

    await websocket.send(res)
    print(res)

if __name__ == '__main__':
    start_server = websockets.serve(hello, '127.0.0.1', 9000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()