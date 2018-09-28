#-*- coding:utf-8 -*-
from operation import *
'''
--------------------------
TEST CODE FOR SERVO MOVING
--------------------------
'''

def test_hold():
    '''
    펜을 잡는지를 확인하는 코드
    :return:
    '''
    print '펜을 잡는지를 TEST하는 코드 실행 '

    claw_servo = initialize_servo(CLAW_PORT_NUM)

    print 'init angle : 0 degree! '
    move_direct(claw_servo, 0)

    try:
        while True:
            new_angle = raw_input("Enter Angle (0 to 180):")
            new_angle = int(new_angle)
            hold(claw_servo, new_angle)

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()

def test_rotate_shoulder():
    '''
    어깨가 돌아가는지를 확인하는 코드
    :return:
    '''
    print 'shoulder가 돌아가는지 TEST하는 코드 실행 '

    shoulder_servo = initialize_servo(SHOULDER_PORT_NUM)

    print 'init angle : 90 degree! '
    old_angle = 90
    move_direct(shoulder_servo, old_angle)

    try:
        while True:
            new_angle = raw_input("Enter Angle (0 to 180):")
            new_angle = int(new_angle)
            move_smooth(shoulder_servo, old_angle, new_angle)
            old_angle = new_angle

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()

def test_hold_and_move():
    '''
    펜을 잡은 채로, shoulder 부분을 움직일 수 있는지를 확인
    :return:
    '''
    print '펜을 잡은 채로 shoulder 부분을 움직일 수 있는지를 TEST하는 코드 실행 '

    shoulder_servo = initialize_servo(SHOULDER_PORT_NUM)
    claw_servo = initialize_servo(CLAW_PORT_NUM)

    print 'initialze all servo'
    move_direct(shoulder_servo, 90)
    move_direct(claw_servo, 0)
    sleep(1)

    print 'claw_servo hold the pen'
    raw_input("Press enter! Start to grab")
    hold(claw_servo, 30)

    print 'move the shoulder'
    old_angle = 90
    try:
        while True:
            new_angle = raw_input("Enter Angle (0 to 180):")
            new_angle = int(new_angle)
            move_smooth(shoulder_servo, old_angle, new_angle)
            old_angle = new_angle

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()

def test_right_arm():
    '''
    오른쪽 서보모터의 움직임을 확인하는 코드 실행
    :return:
    '''
    print '오른쪽 서보모터의 움직임을 테스트하는 코드 실행'
    right_arm_servo = initialize_servo(RIGHT_PORT_NUM)

    print 'init angle : 90 degree! '
    old_angle = 90
    move_direct(right_arm_servo, old_angle)

    try:
        while True:
            new_angle = raw_input("Enter Angle (0 to 180):")
            new_angle = int(new_angle)
            move_smooth(right_arm_servo, old_angle, new_angle)
            old_angle = new_angle

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()


def test_left_arm():
    '''
    왼쪽 서보모터의 움직임을 확인하는 코드 실행
    :return:
    '''
    print '왼쪽 서보모터의 움직임을 테스트하는 코드 실행'
    left_arm_servo = initialize_servo(LEFT_PORT_NUM)

    print 'init angle : 90 degree! '
    old_angle = 90
    move_direct(left_arm_servo, old_angle)

    try:
        while True:
            new_angle = raw_input("Enter Angle (0 to 180):")
            new_angle = int(new_angle)
            move_smooth(left_arm_servo, old_angle, new_angle)
            old_angle = new_angle

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()


def test_three_axis():
    '''
    삼축(shoulder, right, left)을 제어하여 움직이는 코드 실행
    :return:
    '''
    print '삼축(shoulder, right, left)을 제어하여 움직이는 코드 실행'
    shoulder_servo = initialize_servo(SHOULDER_PORT_NUM)
    right_arm_servo = initialize_servo(RIGHT_PORT_NUM)
    left_arm_servo = initialize_servo(LEFT_PORT_NUM)

    print 'init angle : 90 degree! '
    angles = [90, 90, 90]
    move_direct(shoulder_servo, angles[0])
    move_direct(right_arm_servo, angles[1])
    move_direct(left_arm_servo, angles[2])

    try:
        while True:
            new_angles = raw_input("Enter Three Angles (0 to 180):").split(' ')[:3]
            if len(new_angles) < 3:
                continue
            new_angles = [int(angle) for angle in new_angles]

            move_smooth(shoulder_servo, angles[0], new_angles[0])
            move_smooth(right_arm_servo, angles[1], new_angles[1])
            move_smooth(left_arm_servo, angles[2], new_angles[2])

            angles = new_angles

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()

if __name__ == '__main__':
    import sys
    GPIO = initialize_GPIO()
    try:
        if len(sys.argv) > 1:
            test_num = int(sys.argv[1])

        if test_num == 1:
            test_hold()
        elif test_num == 2:
            test_rotate_shoulder()
        elif test_num == 3:
            test_hold_and_move()
        elif test_num == 4:
            test_right_arm()
        elif test_num == 5:
            test_left_arm()
        elif test_num == 6:
            test_three_axis()
        else:
            print("1~6를 좀 입력해라")

    finally:
        GPIO.cleanup()