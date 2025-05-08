import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

class Led:
    
    def _init_(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.LOW)
        
    def blink(self, count, time):
        for _ in range(count):
            gpio.output(pin, gpio, HIGH)
            sleep(time)
            gpio.output(pin, gpio, LOW)
            sleep(time)
            
    def ledOn(self):
        gpio.output(self.pin, gpio.HIGH)
        
    def ledOff(self):
        gpio.output(self.pin, gpio.LOW)
        
class button:
    
    def _init_(self, pin, onPressed):
        
    