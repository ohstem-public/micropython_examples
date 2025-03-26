from machine import Pin, PWM

class Servo:

    def __init__(self, pin):
        self.pin = pin
        self.pwm = PWM(Pin(pin), freq=50, duty=0)

    def turn(self, angle):
        # calculate duty cycle and move the motor
        # Angle 0: 0.5ms/20ms = 0.025 = 2.5% duty cycle
        # => duty = 0.025*1024 = 25.6 ~ 26
        # Angle 180: 2.4ms/20ms = 0.12 = 12% duty cycle
        # => duty: 0.12*1024 = 122.88 ~ 123
        duty = 26 + int(angle/180*(123-26))
        self.pwm.duty(duty)