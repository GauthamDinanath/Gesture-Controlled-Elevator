import Leap
import serial
import time
from statistics import mode


arduino = serial.Serial("com6", 9600)
time.sleep(2)


class LeapEventListener(Leap.Listener):

    def on_init(self, controller):
        print("Initialized")

    def on_frame(self, controller,):

        frame = controller.frame()
        if not frame.hands.is_empty:
            # start = len(frame.fingers.extended())
            if frame.pointables.frontmost.time_visible >= 1.1 and frame.pointables.frontmost.time_visible <= 1.12 :
                end=len(frame.fingers.extended())
                # if (end == start):
                print "selected floor is", str(end)
                arduino.write(str(end))
                # print arduino.readline()

        else:
            print "no finger detected"


controller = Leap.Controller()
listener = LeapEventListener()

a = []
while 1:
    controller.add_listener(listener)
