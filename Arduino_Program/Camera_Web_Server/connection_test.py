import serial as PortSerial
import time
ArduinoUnoSerial = PortSerial.Serial('COM3',9600) #create Serial object *REMEMBER to check the number of COM
print(ArduinoUnoSerial.readline()) #read the serial data and print it as line
print("You have new message from Arduino")
while 1:
    var = input()
    if(var == '1'):
        ArduinoUnoSerial.write('1'.encode()) #send 1 to the arduino's Data code
        print("LED turned ON")
        time.sleep(1)
    elif(var == '0'):
        ArduinoUnoSerial.write('0'.encode()) #send 0 to the arduino's Data code
        print("LED turned OFF")
        time.sleep(1)