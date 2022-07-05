from machine import Pin
from time import sleep, sleep_ms
from utils.octopus import disp7_init
from components.button import Button
from components.rgb import Rgb, wheel 
import colors_rgb as rgb
import random


print("this is simple OctopusLAB micro roulette | ESP32 & octopusLAB")
print()

button_pin = 0
pin34 = Pin(34, Pin.IN)
button = Pin(button_pin, Pin.IN)
button_lef = Button(pin34, release_value=1)

d7 = disp7_init()   # 8 x 7segment display init

WSMAX = 45
ws = Rgb(15,WSMAX) #27 DEV3 # 15 WS
offset = 24

def transform(i,offs=0):
    ret = i+offs
    if ret > WSMAX-1: ret = ret-WSMAX
    return ret


press_start = False
@button_lef.on_release
def on_press_lef():
    global press_start
    print("left")
    press_start = True


def pattern_fill(col=(50,0,0),speed_delay=0,num1=0,num2=WSMAX):
    for i in range(num1,num2): 
       ws.color(col,i)
       sleep_ms(speed_delay)


def pattern_single_run(col=(50,0,0),num=2):
  for loop in range(num):
   for i in range(WSMAX): 
       ws.color((50,0,0),i)
       d7.show(i)
       sleep(0.001*loop*loop)
       sleep_ms(10)
       ws.color((0,0,0),i)
       
  
def pattern_ruleta():
    ws.color((0,50,0),transform(0,offset))
    for i in range(1,WSMAX):
        if i%2==0:
            ws.color((12,0,0),transform(i,offset))
        else:
            ws.color((0,0,3),transform(i,offset))
        sleep_ms(10)


def ruleta_game_intro():
  d7.show("octopus")
  pattern_fill((20,6,0),20) # orange  
  sleep(1.5)
  d7.show("micro")
  pattern_fill((0,30,0),15)  
  sleep(1.5)
  d7.show("rOULEttE")
  pattern_ruleta() 
  sleep(3)
       

def rainbow_cycle_irq(ws,wait=2,intensity=10):
    global press_start
    for j in range(16):
        for i in range(WSMAX):
            rc_index = (i * 256 // WSMAX) + j
            ws.color(wheel(rc_index & 255,intensity),i)           
        if press_start:
            print("btn_start")           
            break    
    sleep_ms(wait)


def ruleta_game(col=(50,0,0),num=7):
  for loop in range(num):
    for i in range(WSMAX): 
       ws.color((50,0,0),transform(i,offset))
       d7.show(str(i) + "   ")
       sleep(0.001*loop*loop)
       sleep_ms(10)
       ws.color((0,0,0),transform(i,offset))
       
  rndnum = random.randint(0,WSMAX)
  for i in range(rndnum): 
       ws.color((100,0,0),transform(i,offset))
       d7.show(" - "+str(i)+" - ")
       sleep(0.1*rndnum/20)
       print(rndnum,i,rndnum-i)
       if rndnum-i<5: sleep(1)
       if rndnum-i<2: sleep(0.5)           
       ws.color((0,0,0),transform(i,offset))
       
  ws.color((0,50,100),transform(rndnum,offset))
  d7.show(" - "+str(rndnum)+" - ")
  return rndnum    
 
 
def ruleta_pause(win):
     global press_start
     ws.color((0,50,0),transform(0,offset))
     ws.color((0,50,100),transform(win,offset))
     sleep(2)
     for i in range(99):
         d7.show("")
         rainbow_cycle_irq(ws)           
         
         d7.show("---"+str(win)+"---")
         pattern_fill((0,0,0),0)
         ws.color((0,50,0),transform(0,offset))
         ws.color((0,50,100),transform(win,offset))
         if press_start:
             press_start = False
             break
         
         sleep(1.5)
  
   
while True:
    rainbow_cycle_irq(ws)
    ruleta_game_intro()
    win = ruleta_game()
    ruleta_pause(win)
