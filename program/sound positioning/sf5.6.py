from ev3dev.ev3 import *
from time import sleep
import ev3dev.ev3 as ev3


p = ev3.LegoPort(ev3.INPUT_1)
p.set_device="lego-nxt-sound"
q = ev3.LegoPort(ev3.INPUT_2)
q.set_device="lego-nxt-sound"
m = ev3.LegoPort(ev3.INPUT_3)
m.set_device="lego-nxt-sound"
n = ev3.LegoPort(ev3.INPUT_4)
n.set_device="lego-nxt-sound"
sleep(1)

print('AAAAAAAAAAAA')


#第一个ev3的声明
s1 = ev3.SoundSensor('in1')
s2 = ev3.SoundSensor('in2')
s3 = ev3.SoundSensor('in3')
s4 = ev3.SoundSensor('in4')
assert s1.connected, "Connect a sound sensor to 1 sensor port"
assert s2.connected, "Connect a sound sensor to 2 sensor port"
assert s3.connected, "Connect a sound sensor to 3 sensor port"
assert s4.connected, "Connect a sound sensor to 4 sensor port"

s1.mode = 'DBA'
s2.mode = 'DBA'
s3.mode = 'DBA'
s4.mode = 'DBA'

ma = Motor('outA')
mb = Motor('outB')
mc = Motor('outC')
md = Motor('outD')
assert ma.connected, "Connect a motor to port A"
assert mb.connected, "Connect a motor to port B"
assert mc.connected, "Connect a motor to port C"
assert md.connected, "Connect a motor to port D"

print('BBBBBBBBBB')

#第二个ev3的声明
gy = GyroSensor('in1')
assert gy.connected, "Connect a gyro sensor to 1 sensor port"

gy.mode = 'GYRO-ANG'

j=0
while j<8:
    a1 = 1000-(s1.value()+10)
    a2 = 1000-(s2.value()-7)
    a3 = 1000-(s3.value()-7)
    a4 = 1000-(s4.value()+1)
    j=j+1


while True:
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    i=0
    while i < 4:
        b1 = b1+(1000-(s1.value()+10))
        sleep(0.1)
        b2 = b2+(1000-(s2.value()-7))
        sleep(0.1)
        b3 = b3+(1000-(s3.value()-7))
        sleep(0.1)
        b4 = b4+(1000-(s4.value()+1))
        i = i+1

    v1 = b1/4
    v2 = b2/4
    v3 = b3/4
    v4 = b4/4

    print(str(v1)+"")
    print(str(v2)+"")
    print(str(v3)+"")
    print(str(v4)+"")

    diff = 15
    equal = 10
    v0 = 1000

#####


    if ((v2+v3)-(v1+v4))>diff:
        if v2-v1<diff and v1-v4>diff and v2-v3>diff or v2-v3>diff and v3-v4>diff or v2-v1>diff and v2-v3>diff and v2-v4>diff and abs(v1-v3)<equal and abs(v3-v4)<equal and abs(v1-v4)<equal:
            gy.mode = 'GYRO-ANG'
            while True:
                ma.run_forever(speed_sp=-v0)
                mb.run_forever(speed_sp=v0)
                mc.run_forever(speed_sp=v0)
                md.run_forever(speed_sp=-v0)
                if int(str(gy.value),10) > 60:
                    ma.stop()
                    mb.stop()
                    mc.stop()
                    md.stop()
                    break
            print('right 60!')
        else:
            if abs(v2-v3)<equal and v3-v1>diff and abs(v1-v4)<equal:
                gy.mode = 'GYRO-ANG'
                while True:
                    ma.run_forever(speed_sp=-v0)
                    mb.run_forever(speed_sp=v0)
                    mc.run_forever(speed_sp=v0)
                    md.run_forever(speed_sp=-v0)
                    if int(str(gy.value),10) > 90:
                        ma.stop()
                        mb.stop()
                        mc.stop()
                        md.stop()
                        break
                print('right 90!')
            else:
                if v3-v2>diff and v2-v1>diff or v3-v4>diff and v4-v1>diff and v3-v2>diff or v3-v1>diff and v3-v2>diff and v3-v4>diff and abs(v1-v2)<equal and abs(v2-v4)<equal and abs(v1-v4)<equal:
                    gy.mode = 'GYRO-ANG'
                    while True:
                        ma.run_forever(speed_sp=-v0)
                        mb.run_forever(speed_sp=v0)
                        mc.run_forever(speed_sp=v0)
                        md.run_forever(speed_sp=-v0)
                        if int(str(gy.value),10) > 120:
                            ma.stop()
                            mb.stop()
                            mc.stop()
                            md.stop()
                            break
                    print('right 120!')
    else:
        if ((v1+v4)-(v2+v3))>diff:
            if (v1-v2>diff and v2-v3>diff) and v1-v4>diff or (v1-v4>diff and v4-v3>diff) or v1-v2>diff and v1-v3>diff and v1-v4>diff and abs(v2-v3)<equal and abs(v2-v4)<equal and abs(v3-v4)<equal:
                                                #严苛了一些
                gy.mode = 'GYRO-ANG'
                while True:
                    ma.run_forever(speed_sp=v0)
                    mb.run_forever(speed_sp=-v0)
                    mc.run_forever(speed_sp=-v0)
                    md.run_forever(speed_sp=v0)
                    if int(str(gy.value),10) < -60:
                        ma.stop()
                        mb.stop()
                        mc.stop()
                        md.stop()
                        break
                print('left 60!')
            else:
                if abs(v1-v4)<equal and v4-v2>diff and abs(v2-v3)<equal:
                    gy.mode = 'GYRO-ANG'
                    while True:
                        ma.run_forever(speed_sp=v0)
                        mb.run_forever(speed_sp=-v0)
                        mc.run_forever(speed_sp=-v0)
                        md.run_forever(speed_sp=v0)
                        if int(str(gy.value),10) < -90:
                            ma.stop()
                            mb.stop()
                            mc.stop()
                            md.stop()
                            break
                    print('left 90!')
                else:
                    if v4-v3>diff and v3-v2>diff and v4-v1>diff or v4-v1>diff and v1-v2>diff or v4-v2>diff and v4-v3>diff and v4-v1>diff and abs(v2-v3)<equal and abs(v2-v1)<equal and abs(v3-v1)<equal:
                        gy.mode = 'GYRO-ANG'
                        while True:
                            ma.run_forever(speed_sp=v0)
                            mb.run_forever(speed_sp=-v0)
                            mc.run_forever(speed_sp=-v0)
                            md.run_forever(speed_sp=v0)
                            if int(str(gy.value),10) < -120:
                                ma.stop()
                                mb.stop()
                                mc.stop()
                                md.stop()
                                break
                        print('left 120!')
        else:
            if v4-v1 > diff or v3-v2 > diff:
                gy.mode = 'GYRO-ANG'
                while True:
                    ma.run_forever(speed_sp=-v0)
                    mb.run_forever(speed_sp=v0)
                    mc.run_forever(speed_sp=v0)
                    md.run_forever(speed_sp=-v0)
                    if int(str(gy.value),10) >180:
                        ma.stop()
                        mb.stop()
                        mc.stop()
                        md.stop()
                        break
                print('180!')
            else:
                if v1-v4 > diff or v2-v3 > diff:
                    print('front!')
                    # 前进一小下
                    ma.run_timed(time_sp=50, speed_sp=v0)
                    mb.run_timed(time_sp=50, speed_sp=v0)
                    mc.run_timed(time_sp=50, speed_sp=v0)
                    md.run_timed(time_sp=50, speed_sp=v0)
    print('6666666666')

    ##############################

    #插入视频调整代码

    ##############################

    #受到刺激重新开始声音探测
    while True:
        sleep(1)
        if v4-v1>diff or v4-v2>diff or v3-v1>diff or v3-v2>diff:
            break
