import Leap
import serial
import time

arduino = serial.Serial('com7', 9600)
time.sleep(2)


class LeapEventListener(Leap.Listener):

    def on_init(self, controller):
        print("Initialized")
        # arduino.write('i')

    # def on_connect(self, controller):
    #     print("Connected")
    #     # controller.enable_gesture(Leap.Gesture.Type.TYPE_SWIPE)
    #     # controller.config.set("Gesture.Swipe.MinLength", 200.0)
    #     # controller.config.save()

    def on_frame(self, controller):
        frame = controller.frame()
        if not (frame.hands.is_empty):
            ht = 0
            time.sleep(0.1)
            hand = int(frame.hands.frontmost.palm_position.y)
            ht=hand
            if (ht > 45 and ht < 115 ):# 155
                if frame.hands.frontmost.grab_strength==1:
                    # print 0
                    arduino.write('0')
                    print arduino.readline()
                    ht = 0

            elif (ht > 175 and ht < 235):#280
                if frame.hands.frontmost.grab_strength== 1:
                    # print 1
                    arduino.write('1')
                    print arduino.readline()
                    ht = 0


            elif (ht > 300  and ht < 360 ):#410
                if frame.hands.frontmost.grab_strength == 1:
                    print 2
                    # arduino.write('2')
                    # print arduino.readline()
                    ht = 0

            # elif (ht > 587 and ht < 537):  # 517
            #     if frame.hands.frontmost.grab_strength == 1:
            #         print 4
            #         # arduino.write('4')
            #         # print arduino.readline()
            #         ht = 0

        else:
            print "no hand detected"

    # print "Press Enter"
    # try:
    #     sys.stdin.readline()
    # except KeyboardInterrupt:


controller = Leap.Controller()
listener = LeapEventListener()

a = []
while 1:
    controller.add_listener(listener)