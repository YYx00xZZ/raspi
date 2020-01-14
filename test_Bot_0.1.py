import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# serial connection imports
import serial
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# serial connection things
ser = serial.Serial('COM8', 9600)

bot = telegram.Bot(token=config.TOKEN)

def normalize(inputData):
    inputData1 = inputData.decode()
    inputData2 = inputData1.strip()
    return inputData2
    
def stitch(text):
    bot.send_message(chat_id=config.houseKeeper, text=text)

def echo(update, context):
    update.message.reply_text(update.message.text)

def toggleLed(update, context):
    print("arguments of cmd" + context.args[0])
    preBit = update.message.text.encode()
    print (preBit)
    ser.write(preBit)
    
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    prevState = "null"
    
    updater = Updater(config.TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("led", toggleLed, pass_args=True))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

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

if __name__ == '__main__':
    main()
