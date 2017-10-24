from gpiozero import LED
from random import randint

GPIO_PINS=[4, 10, 27, 22]
leds = [LED(GPIO_PINS[0]), LED(GPIO_PINS[1]), LED(GPIO_PINS[2]), LED(GPIO_PINS[3])]
def blinkblink(blinktime):
    '''
    blinktime in seconds
    '''
    leds[randint(0,3)].blink(on_time=blinktime, n=1)
