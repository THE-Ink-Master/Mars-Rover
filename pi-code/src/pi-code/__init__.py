import serial
import time
import pyttsx3
import os
import pygame
import atexit

os.system('cls' if os.name == 'nt' else 'clear')

pygame.mixer.init()
pygame.init()

# serial0 = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)

time.sleep(2)

def exit():
    # serial0.close()
    print("Closing...")

atexit.register(exit)

# def println(printIn):
#     toPrint = f"{printIn}\n"
#     serial0.write(toPrint.encode("utf-8"))

# def print(print):
#     serial0.write(print.encode("utf-8"))

def play():
    pygame.mixer.music.load("./music/Moon Lord.mp3")
    pygame.mixer.music.play(0)

def say(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

# serial0.readline()

try:
    # while True:
        # Main loop
        # pass
    play()
    while True:
        print("playing")

except KeyboardInterrupt:
    print("Closing, please wait")

finally:
    # serial0.close()
    print("E")