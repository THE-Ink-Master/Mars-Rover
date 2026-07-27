import serial
import time
import pyttsx3
import os
import pygame
import atexit

os.system('cls' if os.name == 'nt' else 'clear')

pygame.mixer.init()
pygame.init()

serial1 = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)

time.sleep(2)

def exit():
    print("Closing...")
    serial1.close()

atexit.register(exit)

def play():
    if pygame.mixer.music.get_busy():
        print("playing")
    else:
        pygame.mixer.music.load("./music/Moon Lord.mp3")
        pygame.mixer.music.play(0)

def say(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

def read_serial():
    if serial1.in_waiting > 0:
        global last_received

        buffer_string = ''
        buffer_string = buffer_string + serial1.read(serial1.inWaiting())
        if '\n' in buffer_string:
            lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer_string = lines[-1]

    
        if last_received == "Play Music"():
            play()

def println(printIn):
    toPrint = f"{printIn}\n"
    serial1.write(toPrint.encode("utf-8"))

def print(print):
    serial1.write(print.encode("utf-8"))

try:
    # Main loop
    while True:
        read_serial()
        print("playing")

except KeyboardInterrupt:
    print("Closing, please wait")

finally:
    serial1.close()
    print("E")