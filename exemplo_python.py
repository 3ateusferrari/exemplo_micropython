import machine
import dht
import time


sensor = dht.DHT11(machine.Pin(14))  # GPIO14
led = machine.Pin(2, machine.Pin.OUT)  # GPIO2

limite_temp = 30

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()

        print("Temperatura: {}°C, Umidade: {}%".format(temp, umid))

        if temp > limite_temp:
            led.on()
        else:
            led.off()

        time.sleep(2)

    except OSError as e:
        print("Erro ao ler o sensor:", e)
