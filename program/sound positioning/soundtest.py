from ev3dev.ev3 import *
from time import sleep

import ev3dev.ev3 as ev3
p = ev3.LegoPort(ev3.INPUT_2)
p.set_device="lego-nxt-sound"
q = ev3.LegoPort(ev3.INPUT_3)
q.set_device="lego-nxt-sound"
sleep(1)
sl = ev3.SoundSensor('in2')
sr = ev3.SoundSensor('in3')
assert sl.connected, "Connect a sound sensor to 2 sensor port"
assert sr.connected, "Connect a sound sensor to 3 sensor port"

sl.mode = 'DBA'
sr.mode = 'DBA'

ma = Motor('outA')
mb = Motor('outB')
mc = Motor('outC')
md = Motor('outD')
assert ma.connected, "Connect a motor to port A"
assert mb.connected, "Connect a motor to port B"
assert mc.connected, "Connect a motor to port C"
assert md.connected, "Connect a motor to port D"

while True:
    voll1 = sl.value()
    volr1 = sr.value()-6
    sleep(0.1)
    voll2 = sl.value()
    volr2 = sr.value()-6
    sleep(0.1)
    voll3 = sl.value()
    volr3 = sr.value()-6
    sleep(0.1)
    voll4 = sl.value()
    volr4 = sr.value()-6
    vl=(voll1+voll2+voll3+voll4)/4
    vr=(volr1+volr2+volr3+volr4)/4
    if (vl-vr)>6:
        ma.run_timed(time_sp=500, speed_sp=-500)
        mb.run_timed(time_sp=500, speed_sp=500)
        mc.run_timed(time_sp=500, speed_sp=500)
        md.run_timed(time_sp=500, speed_sp=-500)
        print('bingo right')
    else:
        if (vr-vl)>6:
            ma.run_timed(time_sp=500, speed_sp=500)
            mb.run_timed(time_sp=500, speed_sp=-500)
            mc.run_timed(time_sp=500, speed_sp=-500)
            md.run_timed(time_sp=500, speed_sp=500)
            print('bingo left')
        else:
            sleep(1)
    print(str(vl)+' '+str(vr))
    sleep(1)
