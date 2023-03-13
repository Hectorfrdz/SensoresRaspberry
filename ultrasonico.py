import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setwarnings(False)
        self.inicio = 0
        self.final = 0

    def medirDistancia(self):
        GPIO.setwarnings(False)

        GPIO.output(self.trigger_pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            self.inicio = time.time()
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            self.final = time.time()
        duracion = self.final - self.inicio
        distance = (duracion * 17150)
        return round(distance, 2)

    def liberarPin(self):
        GPIO.cleanup()
