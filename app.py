#!/usr/bin/env python

import RPi.GPIO as GPIO
import atexit
from time import sleep
led1 = 29
led2 = 31
led3 = 11
led4 = 13

def cleanup_gpio():
  print('Ended')
  GPIO.cleanup()
atexit.register(cleanup_gpio)

def light(pin):
  ''' light up a pin'''
  pass
def dark(pin):
  ''' light up a pin'''
  pass

def photobooth():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(led1,GPIO.OUT)
  GPIO.setup(led2,GPIO.OUT)
  GPIO.setup(led3,GPIO.OUT)
  GPIO.setup(led4,GPIO.OUT)
  for pin in led1, led2, led3, led4:
    GPIO.output(pin,True)
    sleep(2)
    GPIO.output(pin,False)

  

if __name__ == '__main__':
  photobooth()
