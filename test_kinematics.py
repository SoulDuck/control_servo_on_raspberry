#-*- coding:utf-8 -*-
import kinematics
from operation import *
'''
--------------------------
TEST CODE FOR kinematics
--------------------------
'''

def test_unsolve():
    '''
    각도를 받아 좌표값을 반환하는 코드의 동작을 테스트
    :return:
    '''
    print '각도를 받아 좌표값을 반환하는 코드의 동작을 TEST하는 코드 실행 '

    try:
        while True:
            inputs = raw_input("Enter three Angles (0 to 180): (split by space)").split(' ')[:3]
            degrees = [float(int(angle)) for angle in inputs] # string을 float으로 바꿈
            radians =  [ kinematics.degree2radian(degree) for degree in degrees]

            x, y, z = kinematics.unsolve(*radians)
            print("radian output(x,y,z) : ({:.4f},{:.4f},{:.4f})".format(*radians))
            print("dist   output(x,y,z) : ({:.4f},{:.4f},{:.4f})".format(x, y, z))
    except KeyboardInterrupt:
        print("TEST END")


def test_solve():
    '''
    거리를 받아 움직이어야하는 좌표값을 반환하는 코드의 동작을 테스트
    :return:
    '''
    print('거리를 받아 움직어야하는 모터 회전값을 반환하는 코드의 동작을 테스트')

    try:
        while True:
            inputs = raw_input("Enter point (x,y,z): (split by space)").split(' ')[:3]
            coords = [float(int(coord)) for coord in inputs]  # string을 float으로 바꿈
            x, y, z = coords
            radians = [0,0,0]
            if kinematics.solve(x,y,z,angles=radians):
                degrees = [kinematics.radian2degree(radian) for radian in radians]
                print("radian output(shoulder,right,z) :  ({:.4f},{:.4f},{:.4f})".format(*radians))
                print("degree output(shoulder,right,left) :  ({:.4f},{:.4f},{:.4f})".format(*degrees))
            else:
                print('failed....')
    except KeyboardInterrupt:
        print("TEST END")


def test_move_by_position():
    '''
    좌표값을 받아 그 위치로 움직이는 코드의 동작을 테스트
    :return:
    '''
    print("좌표값을 받아 그 위치로 움직이는 코드의 동작을 테스트")
    shoulder_servo = initialize_servo(SHOULDER_PORT_NUM)
    right_arm_servo = initialize_servo(RIGHT_PORT_NUM)
    left_arm_servo = initialize_servo(LEFT_PORT_NUM)

    print 'init angle : 90 degree! '
    angles = [90, 90, 90]
    move_direct(shoulder_servo, angles[0])
    move_direct(right_arm_servo, angles[1])
    move_direct(left_arm_servo, angles[2])
    sleep(1)

    try:
        while True:
            inputs = raw_input("Enter position (x,y,z):").split(' ')[:3]
            if len(inputs) != 3:
                continue
            coords = [float(int(coord)) for coord in inputs]  # string을 float으로 바꿈
            x, y, z = coords
            radians = [0, 0, 0]
            if kinematics.solve(x, y, z, angles=radians):
                degrees = [kinematics.radian2degree(radian) for radian in radians]
            else:
                continue

            new_angles = [int(angle) for angle in degrees]

            move_smooth(shoulder_servo, angles[0], new_angles[0])
            move_smooth(right_arm_servo, angles[1], new_angles[1])
            move_smooth(left_arm_servo, angles[2], new_angles[2])

            angles = new_angles

    except KeyboardInterrupt:
        print "GPIO. cleanup()"
        GPIO.cleanup()


def test_move_by_degree():
    '''
    모터의 각도 값을 받아 그 위치로 움직이는 코드의 동작을 테스트
    :return:
    '''
    print("모터의 각도 값을 받아 그 위치로 움직이는 코드의 동작을 테스트")
    shoulder_servo = initialize_servo(SHOULDER_PORT_NUM)
    right_arm_servo = initialize_servo(RIGHT_PORT_NUM)
    left_arm_servo = initialize_servo(LEFT_PORT_NUM)
    claw_servo = initialize_servo(CLAW_PORT_NUM)

    print 'init angle : 90 degree! '
    angles = [90, 90, 90]
    move_direct(shoulder_servo, angles[0])
    move_direct(right_arm_servo, angles[1])
    move_direct(left_arm_servo, angles[2])
    move_direct(claw_servo, 0)
    sleep(1)

    print 'claw_servo hold the pen'
    raw_input("Press enter! Start to grab")
    hold(claw_servo, 30)

    try:
        while True:
            new_angles = raw_input("Enter Three Degrees [ BASE RIGHT LEFT ]:").split(' ')[:3]
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
        else:
            test_num = 0

        if test_num == 1:
            test_unsolve()
        elif test_num == 2:
            test_solve()
        elif test_num == 3:
            test_move_by_position()
        elif test_num == 4:
            test_move_by_degree()
        else:
            raise NotImplementedError

    finally:
        print("all test end")