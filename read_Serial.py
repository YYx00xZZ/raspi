import serial
import time
import signal

ser = serial.Serial("COM8", 9600)
ser.baudrate = 9600

prevState = "null"

def normalize(inputData):
    inputData1 = inputData.decode()
    inputData2 = inputData1.strip()
    return inputData2

try:
    while True:
        currState=normalize(ser.readline())
        if currState == "0" and prevState == "1" or currState == "0" and prevState == "null":
            prevState = "0"
            print (prevState)
#            snitchMsg('CLOSED', None)
        if currState != "0" and prevState == "0" or currState != "0" and prevState == "null":
            prevState = "1"
            print (prevState)
#            snitchMsg('OPENED', None)

except KeyboardInterrupt:
    print ('\nExiting . . . \n')
