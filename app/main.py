import sys, time, os
import RPi.GPIO as GPIO

COLOR = os.getenv('COLOR', 'blue').lower()

redPin   = 11
greenPin = 13
bluePin  = 15

pinColors = {
  'red': redPin,
  'green': greenPin,
  'blue': bluePin
}

def blink(pin):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.HIGH)

  print("LED on")
  time.sleep(15)
  print("LED off")

  GPIO.output(pin, GPIO.LOW)

def main():
  while True:

    blink(pinColors[COLOR])

    return False

  return

main()