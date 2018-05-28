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

print('BBBBBBBBB')
#
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

print('AAAAAAAAAAAAAAAAAA')

ma = Motor('outA')
mb = Motor('outB')
mc = Motor('outC')
md = Motor('outD')
assert ma.connected, "Connect a motor to port A"
assert mb.connected, "Connect a motor to port B"
assert mc.connected, "Connect a motor to port C"
assert md.connected, "Connect a motor to port D"

print('CCCCCCCCCCCC')

j=0
while j<8:
    a1 = 1000-(s1.value()+10)
    a2 = 1000-(s2.value()-7)
    a3 = 1000-(s3.value()-7)
    a4 = 1000-(s4.value()+1)
    j=j+1
# 清除刚刚开始探测的误差

while True:
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    i=0
    while i < 4:
        b1 = b1+(1000-(s1.value()+10))
        b2 = b2+(1000-(s2.value()-7))
        b3 = b3+(1000-(s3.value()-7))
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

    diff = 10
    t60 = 500+200
    t90 = 1000+200
    t120 = 1500+200
    t180 = 2000+200
    v0 = 1000
####
    if ((v2+v3)-(v1+v4))>diff:
        if(v2-v1<diff and v1-v4>diff) or (v2-v3>diff and v3-v4>diff):
            ma.run_timed(time_sp=t60, speed_sp=-v0)
            mb.run_timed(time_sp=t60, speed_sp=v0)
            mc.run_timed(time_sp=t60, speed_sp=v0)
            md.run_timed(time_sp=t60, speed_sp=-v0)
            print('right 60!')
        else:
            if (abs(v2-v3)<diff and v3-v1>diff) and abs(v1-v2)<diff:
                ma.run_timed(time_sp=t90, speed_sp=-v0)
                mb.run_timed(time_sp=t90, speed_sp=v0)
                mc.run_timed(time_sp=t90, speed_sp=v0)
                md.run_timed(time_sp=t90, speed_sp=-v0)
                print('right 90!')
            else:
                if v3-v2>diff and v2-v1>diff or v3-v4>diff and v4-v1>diff:
                    ma.run_timed(time_sp=t120, speed_sp=-v0)
                    mb.run_timed(time_sp=t120, speed_sp=v0)
                    mc.run_timed(time_sp=t120, speed_sp=v0)
                    md.run_timed(time_sp=t120, speed_sp=-v0)
                    print('right 120!')
    else:
        if ((v1+v4)-(v2+v3))>diff:
            if (v1-v2>diff and v2-v3>diff) or (v1-v4>diff and v4-v3>diff):
                ma.run_timed(time_sp=t60, speed_sp=v0)
                mb.run_timed(time_sp=t60, speed_sp=-v0)
                mc.run_timed(time_sp=t60, speed_sp=-v0)
                md.run_timed(time_sp=t60, speed_sp=v0)
                print('left 60!')
            else:
                if(abs(v1-v4)<diff and v4-v2>diff) and abs(v2-v3)<diff:
                    ma.run_timed(time_sp=t90, speed_sp=v0)
                    mb.run_timed(time_sp=t90, speed_sp=-v0)
                    mc.run_timed(time_sp=t90, speed_sp=-v0)
                    md.run_timed(time_sp=t90, speed_sp=v0)
                    print('left 90!')
                else:
                    if v4-v3>diff and v3-v2>diff or v4-v1>diff and v1-v2>diff:
                        ma.run_timed(time_sp=t120, speed_sp=v0)
                        mb.run_timed(time_sp=t120, speed_sp=-v0)
                        mc.run_timed(time_sp=t120, speed_sp=-v0)
                        md.run_timed(time_sp=t120, speed_sp=v0)
                        print('left 120!')
        else:
            if (abs(v3-v4)<diff and v4-v1>diff) and abs(v1-v2)<diff:
                ma.run_timed(time_sp=t180, speed_sp=-v0)
                mb.run_timed(time_sp=t180, speed_sp=v0)
                mc.run_timed(time_sp=t180, speed_sp=v0)
                md.run_timed(time_sp=t180, speed_sp=-v0)
                print('180!')
            else:
                print('yes!')
    sleep(1)
    print('6666666666')
    #问题向左转只有left60