import websocket
import json

ws = websocket.create_connection('ws://echo.websocket.org/')


def make_complete_buffer(_temperature, _humidity, _moisture):
    _data = {
        "temperature": _temperature,
        "humidity": _humidity,
        "moisture": _moisture
    }
    _json_buffer = json.dumps(_data)
    return _json_buffer


def send_buffer_to_websocket(_buffer):
    ws.send(_buffer)
    _result = f'Received: {ws.recv()}'
    return _result


if __name__ == '__main__':
    while True:
        print(send_buffer_to_websocket(
            make_complete_buffer(23, 23, 123)
        ))
