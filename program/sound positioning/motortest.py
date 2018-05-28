from ev3dev.ev3 import *

ma = Motor('outA')
mb = Motor('outB')
mc = Motor('outC')
md = Motor('outD')
assert ma.connected, "Connect a motor to port A"
assert mb.connected, "Connect a motor to port B"
assert mc.connected, "Connect a motor to port C"
assert md.connected, "Connect a motor to port D"

ma.run_timed(time_sp=500,speed_sp=-500)
mb.run_timed(time_sp=500,speed_sp=-500)
#ma.position.(hold)
##
#mc.run_timed(time_sp=5000,speed_sp=-500)
#md.run_timed(time_sp=5000,speed_sp=500)


