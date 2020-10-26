#include <Servo.h>


int currentFloor = 0;
int destinationFloor = 0;

Servo myservo;
Servo myservo1;

#define CW   1900
#define STOP 1450
#define CCW  1000

int data;
int tt;

void setup() 
{ 
  Serial.begin(9600); 
  //initially set to low
  myservo.attach(9);
  myservo.writeMicroseconds(STOP);
  myservo1.attach(8);
  myservo1.write(175);
  pinMode(10, OUTPUT); 
  pinMode(11, OUTPUT); 
  pinMode(7, OUTPUT); 
  pinMode(12, OUTPUT); 
  digitalWrite (10, LOW);
  digitalWrite (11, LOW);
  digitalWrite (7, LOW);
  digitalWrite (12, LOW);
}

 
void loop() 
{
  
  while (Serial.available())
   {     char data = Serial.read();
//         Serial.println(data);
       
   switch (data)
   {
            case '0' :
                destinationFloor=0 ;  
                myservo1.write(175);
                digitalWrite (7, HIGH);
                digitalWrite (10, LOW);
                digitalWrite (11, LOW);
                digitalWrite (12, LOW);
                             
                break;
            case '1' :
                destinationFloor=1 ;
                myservo1.write(118);
                digitalWrite (11, HIGH);
                digitalWrite (7, LOW);
                digitalWrite (10, LOW);
                digitalWrite (12, LOW); 
                break;
            case '2' :
                destinationFloor=2 ;
                myservo1.write(65);
                digitalWrite (10, HIGH);
                digitalWrite (7, LOW);
                digitalWrite (12, LOW);
                digitalWrite (11, LOW);
                break;
//            case '3':
//                destinationFloor=3 ;
//                myservo1.write(25);
//                digitalWrite (12, HIGH); 
//                digitalWrite (7, LOW);
//                digitalWrite (10, LOW);
//                digitalWrite (11, LOW);
//                break;
//           case 'i':
//                  Serial.println('i');
//                  destinationFloor=0 ;
//                  currentFloor=1;
//                  break;
//                
     }
//      Serial.println(destinationFloor);
     if (destinationFloor > currentFloor) 
       {
                  tt=6700*(destinationFloor - currentFloor);
//                  Serial.println(tt);
                  myservo.writeMicroseconds(CW);
                  delay(tt);
                  myservo.writeMicroseconds(STOP);
       }
      else
      {
                  tt=6700*(currentFloor - destinationFloor);
                  myservo.writeMicroseconds(CCW);
                  delay(tt);
                  myservo.writeMicroseconds(STOP);
      }
 
       currentFloor=destinationFloor;
//
    }  
}
