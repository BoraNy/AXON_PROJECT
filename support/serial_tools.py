import serial
import serial.tools.list_ports


def scan_ports(_device='arduino'):
    _ports = serial.tools.list_ports.comports()
    _Arduino_Port = ''
    _Serial_Port_Silicon_Lab = ''
    _Serial_Port_CH340 = ''

    for _port in _ports:
        if 'Arduino' in _port.description:
            _Arduino_Port = _port.device
        elif 'Silicon' in _port.description:
            _Serial_Port_Silicon_Lab = _port.device
        elif 'CH340' in _port.description:
            _Serial_Port_CH340 = _port.device

    if _device == 'arduino':
        return _Arduino_Port
    elif _device == 'silicon_lab':
        return _Serial_Port_Silicon_Lab
    elif _device == 'ch340':
        return _Serial_Port_CH340
    else:
        return 'No Serial Port Found'


if __name__ == '__main__':
    print(scan_ports())
