# Example using PWM to play music with buzzer

import time
from machine import Pin, PWM

buzzer = PWM(Pin(6))

volume = 1023

def do(duration):
    buzzer.freq(1046) #1
    buzzer.duty(volume)
    time.sleep(duration)

def re(duration):
    buzzer.freq(1175) #2
    buzzer.duty(volume)
    time.sleep(duration)

def mi(duration):
    buzzer.freq(1318) #3
    buzzer.duty(volume)
    time.sleep(duration)

def fa(duration):
    buzzer.freq(1397) #4
    buzzer.duty(volume)
    time.sleep(duration)

def sol(duration):
    buzzer.freq(1568) #5
    buzzer.duty(volume)
    time.sleep(duration)

def la(duration):
    buzzer.freq(1760) #6
    buzzer.duty(volume)
    time.sleep(duration)

def si(duration):
    buzzer.freq(1967) #7
    buzzer.duty(volume)
    time.sleep(duration)

def silent(duration):
    buzzer.freq(5)
    buzzer.duty(volume)
    time.sleep(duration)

# Phát bài nhạc Twinkle twinkle little stars
# Câu 1: Đồ, Đồ, Son, Son, La, La, Son
def song_1():
  do(0.25)
  do(0.25)
  sol(0.25)
  sol(0.25)
  la(0.25)
  la(0.25)
  silent(0.1)

# Câu 2: Fa, Fa, Mi, Mi, Rê, Rê, Đồ
def song_2():
  fa(0.25)
  fa(0.25)
  mi(0.25)
  mi(0.25)
  re(0.25)
  re(0.25)
  do(0.25)
  silent(0.1)

while True:
  song_1()
  time.sleep(0.5)
  song_2()
  time.sleep(1)