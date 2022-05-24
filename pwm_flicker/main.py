# cyberTown 2020
# by octopusLAB + PWM module
# simple simulation of fluorescent lamp flicker

from time import sleep, sleep_ms
from machine import Pin, PWM
from utils.pinout import set_pinout
from utils.octopus_lib import randint
from math import sin, pi
# from components.iot import Pwm

pinout = set_pinout()
dutymax = 510

def randdelay(a=1000,b=2000):
    sleep_ms(randint(a,b))


def pulse(l, t):
    for i in range(20):
        l.duty(int(sin(i / 10 * pi) * 500 + 500))
        sleep_ms(t)
    l.duty(dutymax)
 
 
def flash(l, n):
    print("flash",n)
    for i in range(n):
        for j in range(randint(2,5)):
            pwmled.duty(int(randint(dutymax/2,dutymax)))
            sleep_ms(randint(10,100))
            l.duty(randint(0,50))
            sleep_ms(randint(100,500))
        l.duty(1023)
        sleep(0.1)
        l.duty(dutymax)
        randdelay()
        l.duty(0)
        randdelay()
    
        
pwmled = PWM(Pin(25))
pwmled.duty(0)

def pattern():
    pulse(pwmled, 300)
    pulse(pwmled, 100)
    pulse(pwmled, 10)
    sleep(3)
    pulse(pwmled, 10)
    pulse(pwmled, 100)


print("start")   

while True:
    pattern()
    randdelay()
    flash(pwmled,randint(2,6))
    randdelay()
    longpwm = int(randint(dutymax/2,dutymax))
    longtime = randint(5,30)
    print("long",longpwm,longtime)
    pwmled.duty(longpwm)
    sleep(longtime)

