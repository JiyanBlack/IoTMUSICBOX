from gpiozero import LED
from random import randint


def binkblink(blinktime, GPIO_PINS=[4, 17, 27, 22]):
    '''
    blinktime in seconds
    '''
    ledid = randint(0, 4)
    light = LED(ledid)
    light.blink(on_time=blinktime, n=1)
