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

def setServoAngle(servo, start_angle ,end_angle):
    assert start_angle >=30 and start_angle <= 150 , ''
    assert end_angle>= 30 and end_angle<= 150, ''

    pwm = GPIO.PWM(servo, 100)
    pwm.start(20)
    start_dutyCycle = start_angle/ 18. + 3.
    end_dutyCycle = end_angle / 18. + 3.

    print 'start : {} ==> end : {}'.format(start_dutyCycle , end_dutyCycle)
    exit()
    for dutyCycle  in range(start_dutyCycle , end_dutyCycle):
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(1)
        pwm.stop()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        setServoAngle(pan, 30, 120)
        setServoAngle(tilt, 30 , 120)
        setServoAngle(z_tilt, 30, 120)
    else:
        print sys.argv
        #setServoAngle(pan,int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
        #setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
        #setServoAngle(z_tilt, int(sys.argv[3]))  # 30 ==> 90 (middle point) ==> 150
    GPIO.cleanup()