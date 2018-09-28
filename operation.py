#-*- coding:utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

CLAW_PORT_NUM = 17
SHOULDER_PORT_NUM = 27
RIGHT_PORT_NUM = 22
LEFT_PORT_NUM = 18

def initialize_GPIO():
    '''
    GPIO를 초기화하는 코드
    :return:
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(CLAW_PORT_NUM, GPIO.OUT)  # white => TILT
    GPIO.setup(SHOULDER_PORT_NUM, GPIO.OUT)  # gray ==> PAN
    GPIO.setup(RIGHT_PORT_NUM, GPIO.OUT)  # gray ==> PAN
    GPIO.setup(LEFT_PORT_NUM, GPIO.OUT)
    return GPIO

def initialize_servo(port_num):
    '''
    서보모터에 접속하여 object를 생성
    :param port_num: servo 모터가 연결된 포트 번호

    :return: 포트번호에 매칭된 pwm object
    '''
    hz = 50
    servo = GPIO.PWM(port_num, hz)
    servo.start(7.5)
    return servo

def hold(servo, hold_angle):
    '''
    서보모터가 물건을 쥘수 있도록 동작하는 코드
    :param servo: 움직이고자 하는 servo의 pwm object
    :param hold_angle: 잡을 떄 각도, hold 각도가 커질수록 잡는 세기가 쎄짐(최대 40도 까지 가능)
    :return:
    '''
    if hold_angle < 0 and hold_angle > 40:
        return
    move_smooth(servo, 0, hold_angle)

def move_direct(servo, angle):
    '''
    서보모터가 주어진 각도로 바로 이동하는 코드
    :param servo: 움직이고자 하는 servo의 pwm object
    :param angle: 목표로 하는 각도
    :return:
    '''
    duty = float(angle) / 18.0 + 2.5
    servo.ChangeDutyCycle(duty)
    sleep(0.1)

def move_smooth(servo, curr_angle, target_angle, step=5):
    '''
    서보모터가 주어진 각도로 smooth하게 이동하는 코드
    :param servo: 움직이고자 하는 servo의 pwm object
    :param curr_angle: 현재 각도
    :param target_angle: 목표 각도
    :param step: 한번에 움직이는 각도 크기, 클수록 빠르게 움직인다
    :return:
    '''
    if curr_angle < target_angle:
        direction = step
    else:
        direction = -step
    for angle in range(curr_angle, target_angle, direction):
        move_direct(servo, angle)

    move_direct(servo, target_angle)