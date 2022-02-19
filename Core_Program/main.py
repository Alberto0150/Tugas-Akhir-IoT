import serial as PortSerial
import time
ArduinoUnoSerial = PortSerial.Serial('COM3',115200) #create Serial object *REMEMBER to check the number of COM
print(ArduinoUnoSerial.readline()) #read the serial data and print it as line

# Define
LAMP = 4

# void loop
while 1:
    ArduinoUnoSerial.write('1'.encode())