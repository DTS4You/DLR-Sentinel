from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()


def main():
    print("--- Programm Start ---")

#------------------------------------------------------------------------------
if __name__ == "__main__":

    timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

    main()

#------------------------------------------------------------------------------