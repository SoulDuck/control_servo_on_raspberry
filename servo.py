import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--angle' , type=int)
args = parser.parse_args()





#this sets the names to board mode,
## which just names the pins according to the numbers
# #in the middle of the diagram above.
GPIO.setup(03, GPIO.OUT)
#setup PWM on pin #3 at 50Hz
pwm=GPIO.PWM(03, 50)
pwm.start(0)
# Then start it with 0 duty cycle so
# it doesn't set any angles on startup

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)



if __name__ == '__main__':
    print 'Angle : {}'.format(args.angle)
    SetAngle(args.angle)
    sleep(3)
    pwm.stop()
    GPIO.cleanup()
