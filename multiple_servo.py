#-*- coding:utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pan = 27
tilt = 17
z_tilt = 22

GPIO.setup(tilt, GPIO.OUT) # white => TILT
GPIO.setup(pan, GPIO.OUT) # gray ==> PAN
GPIO.setup(z_tilt, GPIO.OUT) # gray ==> PAN


def duty_check():

    servo = 17
    hz = 50

    pwm = GPIO.PWM( servo, hz)
    pwm.start(1)

    for i in range(3):
        for j in range(1, 6):
            pwm.ChangeDutyCycle(2.5 *i)
            sleep(1.5)

def cali(servo , angle):
    # servo pin , Hz
    pwm = GPIO.PWM(servo, 50)
    pwm.start(20)
    angle = angle / 18. + 3.
    pwm.ChangeDutyCycle(angle)
    sleep(0.1)
    pwm.stop()

def setServoAngle(servo, start_angle ,end_angle):
    #assert start_angle >=30 and start_angle <= 150 , ''
    #assert end_angle>= 30 and end_angle<= 150, ''

    pwm = GPIO.PWM(servo, 100)
    pwm.start(20)
    start_dutyCycle = start_angle/ 18. + 3.
    end_dutyCycle = end_angle / 18. + 3.
    # duty cycle range  3 ~ 13
    print 'start : {} ==> end : {}'.format(start_dutyCycle , end_dutyCycle)
    dutyCycles= range(int(start_dutyCycle)*10,int(end_dutyCycle)*10)
    # 각이 일정 이상 벗어나면 삐이익 소리가 나게 된다
    for dutyCycle  in dutyCycles:
        dutyCycle = dutyCycle/10.

        assert dutyCycle > 3.0 and dutyCycle < 13 , 'duty cycle{}'.format(dutyCycle)
        print dutyCycle
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.5)
    pwm.stop()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:

        setServoAngle(tilt , 0, 180)
        #cali(tilt , 90)
        #setServoAngle(tilt, 30 , 150)
        #setServoAngle(z_tilt, 30, 150)
    else:
        print sys.argv
        #setServoAngle(pan,int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
        #setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
        #setServoAngle(z_tilt, int(sys.argv[3]))  # 30 ==> 90 (middle point) ==> 150
    GPIO.cleanup()