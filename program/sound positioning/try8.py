from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
assert cl.connected, "Connect an EV3 color sensor to any sensor port"

ts1 = TouchSensor('in1')
ts2 = TouchSensor('in2')
assert ts1.connected, "shit!"
# Connect a large motor to port B and check it is connected.
ml = Motor('outA')
mr = Motor('outB')
assert ml.connected, "Connect a large motor to port A"

# Put the color sensor into COL-AMBIENT mode
# to measure ambient light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode = 'COL-AMBIENT'

# run_forever command will allow us to vary motor
# performance on the fly by adjusting speed_sp attribute.

spl = 0
spr = 0
while True:
    if ts1.value():
        spl = spl+10
        ml.run_forever(speed_sp=spl)
        print(spl)
    else:
        spl = spl-10
        ml.run_forever(speed_sp=spl)
        print(spl)
    if ts2.value():
        spr = spr+10
        mr.run_forever(speed_sp=spr)
        print(spr)
    else:
        spr = spr-10
        mr.run_forever(speed_sp=spr)
        print(spr)
    #if ts1.value() == 1 and ts2.value() == 1:
        #break

Sound.beep()
ml.stop()
mr.stop()


