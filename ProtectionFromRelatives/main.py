import pyautogui, serial, time
import sys

#Эта функция проверяет наличие подключенного устройства
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

ports_availible = serial_ports()

if len(ports_availible) > 0:
    port = ports_availible[0]
else:
    print("Подключите устройство!")
    while serial_ports() == []:
        pass
    ports_availible = serial_ports()
    port = ports_availible[0]

print(ports_availible)
flag = 0

#Цикл, принимающий данные и имитирующий нажатие клавиш
while len(ports_availible) > 0:
    s = serial.Serial(port)
    val = int(s.readline()) #чтение из serial порта
    s.close()

    if val == 0 and flag == 0:
        pyautogui.hotkey('ctrl', 'f11') #нажатие клавиш
        flag = 1
    elif val == 1 and flag == 1:
        pyautogui.hotkey('ctrl', 'f11')
        flag = 0