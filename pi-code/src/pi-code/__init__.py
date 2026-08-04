import serial
import time
import pyttsx3
import os
import pygame
import atexit
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)

# logger.debug('')
# logger.info('')
# logger.warning('')
# logger.error('')

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Start pygame audio player
pygame.mixer.init()
pygame.init()

# Disable serial if you don't have the mega connected
# Start up serial
serial1 = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)

# Give python3-serial time to connect
time.sleep(2)

# Close the serial port on exit
def exit():
    print("Closing...")
    serial1.close()
atexit.register(exit)

# Play reversing sound when going back
def play():
    if pygame.mixer.music.get_busy():
        print("playing")
    else:
        # change to reversing sound
        pygame.mixer.music.load("./music/Moon Lord.mp3")
        pygame.mixer.music.play(0)

# Stop reversing sound
def stop():
    pygame.mixer.music.stop()

# TTS code we can use to tell us statis of the rover (eg. low battery)
def say(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

# Read serial (untested)
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

            logger.debug(last_received)
    
        if last_received == "Reverse":
            play()
        elif last_received == "Forward":
            stop()

# Print with new line
def println(printIn):
    toPrint = f"{printIn}\n"
    serial1.write(toPrint.encode("utf-8"))

# Print without new line
def print(print):
    serial1.write(print.encode("utf-8"))

try:
    # Main loop
    while True:
        read_serial()
        print("playing")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Closing, please wait")

finally:
    # On close:
    serial1.close()
    print("closed")