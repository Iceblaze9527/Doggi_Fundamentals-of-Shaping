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

v1 = 0
v2 = 0
v3 = 0
v4 = 0
while True:
    v1 = s1.value()
    v2 = s2.value()
    v3 = s3.value()
    v4 = s4.value()
    print(str(v1)+"")
    print(str(v2)+"")
    print(str(v3)+"")
    print(str(v4)+"")
    print("hhhhhh")