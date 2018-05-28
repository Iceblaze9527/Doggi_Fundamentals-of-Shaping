from ev3dev.ev3 import *

from time import sleep

m = Motor('outA')

m.run_forever(speed_sp=9100)
sleep(5)
m.stop(stop_action="hold")
sleep(5)