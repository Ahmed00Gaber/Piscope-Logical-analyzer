import RPi.GPIO as GPIO
import time
from LCD import *

input_pin = 23  # Change this to the GPIO pin you're using
def GPIO_init():
	# Set up GPIO mode and input pin
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(input_pin, GPIO.IN)

# Function to measure frequency

#this function measure frequency more accurate
def measure_frequency(pin, num_cycles):
    start = time.time()
    for impulse_count in range(num_cycles):
		#wait 100 block:function block until falling edge detected
        GPIO.wait_for_edge(pin, GPIO.FALLING)
    duration = time.time() - start  # duration of the wholee 100 cycle
    period_sginal=duration / num_cycles #to measure period of 1 signal /num of cycles
    frequency = num_cycles / duration  # in Hz
    return frequency
    
def measure_duty_cycle(pin, num_cycles):
    high_time = 0
    low_time = 0
    # Measure the high
    GPIO.wait_for_edge(pin, GPIO.RISING)
    start_time = time.time()
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    high_time = time.time() - start_time
    # Measure the low
    start_time = time.time()
    GPIO.wait_for_edge(pin, GPIO.RISING)
    low_time = time.time() - start_time
    
    total_time = high_time + low_time
    duty_cycle = (high_time / total_time) * 100  # Calculate duty cycle as a percentage
    freq= 1/total_time
    #note we can return freq using tuple 
    #return duty_cycle,freq
    return duty_cycle

    
# Main function to continuously measure frequency
def main():
    try:
        GPIO_init()  # Assuming this function initializes GPIO
        lcd_init()   # Assuming this function initializes LCD
        while True:
            frequency = measure_frequency(input_pin, 100)  # Example: measure 100 samples
            Duty_cycle=measure_duty_cycle(input_pin,100)
            print(f"Measured Frequency: {int(frequency)} hz")
            lcd_string(f"Frequency:{int(frequency)}Hz", LCD_LINE_1)  # Assuming LCD_LINE_1 is defined
            lcd_string(f"D-Cycle:{int(Duty_cycle)} %", LCD_LINE_2)
            time.sleep(0.1)  # Adjust the sleep time according to your sampling rate
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
