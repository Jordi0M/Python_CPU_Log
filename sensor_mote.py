import wmi, socket

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
info_temperatura = w.Sensor()

for sensor in info_temperatura:
    if sensor.SensorType==u'Temperature':
        if sensor.Name=='CPU Package':
            print(sensor)
            temperatura_CPU = sensor.Value
    if sensor.SensorType==u'Temperature':
        
        if 'Core #1' in sensor.Name:
            print(sensor)
            temperatura_CPU = sensor.Value

print(temperatura_CPU)

HOST = '127.0.0.1'
PORT = 65432

enviar_info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enviar_info.connect((HOST, PORT))

enviar_info.send(str(temperatura_CPU).encode())
enviar_info.close()
