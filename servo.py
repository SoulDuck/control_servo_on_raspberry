import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPin = 11
GPIO.setup(servoPin ,GPIO.OUT)
pmw = GPIO.PWM(servoPin , 50 )
pwm.start


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)



if __name__ == '__main__':
    SetAngle(90)
    pwm.stop()
    GPIO.cleanup()