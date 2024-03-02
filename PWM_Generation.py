import RPi.GPIO as GPIO
import time
import tkinter as tk

PWM_signal = 18 #channel 0

def GPIO_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # Configure GPIO pin
    GPIO.setup(PWM_signal, GPIO.OUT, initial=GPIO.LOW)

def set_pwm_frequency_duty_cycle():
    frequency = int(frequency_scale.get())
    duty_cycle = int(duty_cycle_scale.get())
    PWM_CH.ChangeFrequency(frequency)
    PWM_CH.ChangeDutyCycle(duty_cycle)

# Initialize GPIO
GPIO_init()

# Create PWM object
PWM_CH = GPIO.PWM(PWM_signal, 500)  # 500 Hz frequency
PWM_CH.start(30)  # 30% duty cycle

# Tkinter GUI
root = tk.Tk()
root.title("PWM Control")
root.geometry("300x200")

# Frequency Scale
frequency_label = tk.Label(root, text="Frequency (Hz):")
frequency_label.pack()

frequency_scale = tk.Scale(root, from_=1, to=2000, orient=tk.HORIZONTAL)
frequency_scale.pack()

# Duty Cycle Scale
duty_cycle_label = tk.Label(root, text="Duty Cycle (%):")
duty_cycle_label.pack()

duty_cycle_scale = tk.Scale(root, from_=0, to=99, orient=tk.HORIZONTAL)
duty_cycle_scale.pack()

# Apply Button
apply_button = tk.Button(root, text="Apply", command=set_pwm_frequency_duty_cycle)
apply_button.pack()

try:
    root.mainloop()

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    PWM_CH.stop()
    GPIO.cleanup()
