import Leap
import statistics
import serial
import time

class LeapEventListener(Leap.Listener):

    def on_init(self, controller):
        print("Initialized")


    def on_frame(self, controller):
        frame = controller.frame()
        if not (frame.hands.is_empty):

            hand = int(frame.hands.frontmost.palm_position.y)
            a.append(hand)
            print hand
            if len(a)>50:
                print("average",statistics.mean(a))
                global a
                a=[]
        else:
            print "no hand detected"



controller = Leap.Controller()
listener = LeapEventListener()

a = []
while 1:
    controller.add_listener(listener)