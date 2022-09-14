# import all the necesary libraries
import machine
import utime
import random
print("Starting...") # tell the serial on the USB that we are booting up the Pico
#
# setup of variables required for operation :-
#
# set up internal led pin
intPled=machine.Pin(25, machine.Pin.OUT)
# set up pwm objects for light strip pins
pwmDblue=machine.PWM(machine.Pin(12))
pwmDred=machine.PWM(machine.Pin(11))
pwmDgreen=machine.PWM(machine.Pin(10))
pwmSgreen=machine.PWM(machine.Pin(16))
pwmSred=machine.PWM(machine.Pin(17))
pwmSblue=machine.PWM(machine.Pin(18))
# set up the door sensor pin
extPreedS=machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
# set pwm frequencies for lights
pwmDblue.freq(1000)
pwmDred.freq(1000)
pwmDgreen.freq(1000)
pwmSgreen.freq(1000)
pwmSred.freq(1000)
pwmSblue.freq(1000)
# set brightness for wake mode for all lights
bDblueS = 0
bDredS = 100000
bDgreenS = 10000
bSgreenS = 100
bSredS = 1000
bSblueS = 0
# set brightness for sleep mode for all lights
bDblueNM = 0
bDredNM = 10000
bDgreenNM = 1000
bSgreenNM = 100
bSredNM = 1000
bSblueNM = 0
#
# define functions :-
#
def get_reed_switch_1_status(): # detects if the door is open and returns the opposite
    return not extPreedS.value()
def wake(): # turns on all lights to standard values MODE 1
    pwmDred.duty_u16(bDredS)
    pwmDgreen.duty_u16(bDgreenS)
    pwmDblue.duty_u16(bDblueS)
    pwmSred.duty_u16(bSredS)
    pwmSgreen.duty_u16(bSgreenS)
    pwmSblue.duty_u16(bSblueS)
def sleep(): # turns on all lights to sleepmode values MODE 2
    pwmDred.duty_u16(bDredNM)
    pwmDgreen.duty_u16(bDgreenNM)
    pwmDblue.duty_u16(bDblueNM)
    pwmSred.duty_u16(bSredNM)
    pwmSgreen.duty_u16(bSgreenNM)
    pwmSblue.duty_u16(bSblueNM)
#
# start doing meaningful things :-
#
wake()
# start the main loop
while True:
    doorState = get_reed_switch_1_status()
    if doorState:
        intPled(0)
        pwmSred.duty_u16(bSredNM)
    else:
        intPled(1)
        pwmSred.duty_u16(0)
