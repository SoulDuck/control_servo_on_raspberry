
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--servo_0' , type=int)
parser.add_argument('--servo_1' , type=int)
parser.add_argument('--servo_2' , type=int)
args = parser.parse_args()

#this sets the names to board mode,
## which just names the pins according to the numbers
# #in the middle of the diagram above.

GPIO.setup(03, GPIO.OUT)
GPIO.setup(04, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
#setup PWM on pin #3 at 50Hz
pwm_0=GPIO.PWM(03, 50)
pwm_1=GPIO.PWM(04, 50)
pwm_2=GPIO.PWM(05, 50)

map(lambda  pwm : pwm.start(0) ,[pwm_0,pwm_1,pwm_2])



def SetAngle(angle , pwm):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)


if __name__ == '__main__':

    print "servo 1 : {}\n servo 2 : {}\n servo 3 {}]\n".format(args.servo_0 , args.servo_1 , args.servo_2)





# Then start it with 0 duty cycle so
# it doesn't set any angles on startup
