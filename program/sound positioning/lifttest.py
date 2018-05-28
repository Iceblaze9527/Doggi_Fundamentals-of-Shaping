from ev3dev.ev3 import *
from time import sleep

import ev3dev.ev3 as ev3

ma = Motor('outA')
mb = Motor('outB')
mc = Motor('outC')

assert ma.connected, "Connect a motor to pt A"
assert mb.connected, "Connect a motor to port B"or
assert mc.connected, "Connect a motor to port C"

ma.run_timed(time_sp=1500, speed_sp=200)
mb.run_timed(time_sp=1500, speed_sp=200)
sleep(3)
mc.run_timed(time_sp=1600, speed_sp=-200)#负数上升 T=1600*2e