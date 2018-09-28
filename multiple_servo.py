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

def setServoAngle(servo, angle):
    assert angle >=30 and angle <= 150 , ''
    pwm = GPIO.PWM(servo, 100)
    pwm.start(20)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(1)
    pwm.stop()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        setServoAngle(pan, 90)
        setServoAngle(tilt, 90)
    else:

        print sys.argv
        setServoAngle(pan,int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
        setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
        #setServoAngle(z_tilt, int(sys.argv[2]))  # 30 ==> 90 (middle point) ==> 150
    GPIO.cleanup()