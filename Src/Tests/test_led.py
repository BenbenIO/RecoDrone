# Simple test for blinking LED
import time, sys
sys.path.insert(0, '../')
import Record

def main():
    # Create LED
    record_led = Record.LED()

    # Blinking Test
    print("Start blinking LED at {}".format())
    record_led.blink()
    time.sleep(10)
    record_led.stop()
    print("Finished blinking.")

if __name__ == "__main__":
    main()
