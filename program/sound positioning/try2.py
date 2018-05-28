from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')

m.run_forever(speed_sp=900)
sleep(5)
m.stop(stop_action="hold")
sleep(5)