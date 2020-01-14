import telegram
import serial
import config

ser = serial.Serial('COM8', 9600)

bot = telegram.Bot(token=config.TOKEN)

prevState = 'null'

def normalize(inputData):
    inputData1 = inputData.decode()
    inputData2 = inputData1.strip()
    return inputData2

def stitch(text):
    bot.send_message(chat_id=config.houseKeeper, text=text)

try:
    while True:
        currState = normalize(ser.readline())
        if currState == "0" and prevState == "1" or currState == "0" and prevState == "null":
            prevState = "0"
            print (prevState)
            stitch("CLOSED.")
        if currState != "0" and prevState == "0" or currState != "0" and prevState == "null":
            prevState = "1"
            print (prevState)
            stitch("OPEN.")
except KeyboardInterrupt:
    print('\nExiting . . . \n')
