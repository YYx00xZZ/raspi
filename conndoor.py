from gpiozero import Button,PWMLED,OutputDevice,Buzzer
import telepot
from telepot.loop import MessageLoop
from datetime import datetime
from pprint import pprint
from signal import pause

    #   Constants
timestampDate = datetime.now().strftime('%d-%m-%Y')
timestampTime = datetime.now().strftime('%H:%M')
myId = 537399849
global state
state = 'null'
bot = telepot.Bot('955446257:AAFkJSzhsMpWxB9xEud0OITobZvAmjJlF-M')

def snitchMsg(txt,mode):
    message = (txt+'\nDate: {}\nTime: {}'.format(timestampDate, timestampTime))
    bot.sendMessage(myId, message, parse_mode=mode)

def puls(intime, outtime):
    led.pulse(fade_in_time=intime, fade_out_time=outtime, n=None, background=True)

def initVal(initstate):
    if initstate == True:
        state='CLOSED'
        closed()
    if initstate == False:
        state='OPENED'
        opened()

def closed(state='CLOSED'):
    snitchMsg(state,None)
#    print (state)
    puls(1, 0.6)
    bz.off()

def opened(state='OPENED'):
    snitchMsg(state,None)
#    print (state)
    puls(0.05, 0.6)
    bz.beep(on_time=1, off_time=1, n=2, background=True)

button = Button(18)
led = PWMLED(16, frequency=80)
relay = OutputDevice(17,active_high=True,initial_value=False)
bz = Buzzer(26)
    #   About chat
def checkId(chat_id):
    if chat_id == myId:
        return True
    else:
        return False

def handle(msg):
    chat_id=msg['chat']['id']
    #   Check for auth user
    if checkId(chat_id) == True:
        #   If it is auth user do
        if 'entities' in msg and msg['entities'][0]['type'] == 'bot_command':
            command = msg['text']
            if command == '/lamp':
                relay.toggle()
                snitchMsg('\nStatus: {}'.format(str(relay.value)), None )
            elif command == '/status':
                statusCheck()
        #   If not an auth user
        else:
            return
    else:
        bot.sendMessage(chat_id, 'You do\'nt have permission.')

MessageLoop(bot, handle).run_as_thread()

def statusCheck():
    message=('<code>Door sensor:{}\nLED value:{}\nRelay status:{}\nBuzzer status: {}</code>'.format(button.value,led.value,relay.value,bz.value))
    snitchMsg(message,'Html')
try:
    initVal(button.is_pressed)

    button.when_pressed = closed

    button.when_released = opened

    pause()
except KeyboardInterrupt:
    print ('\nExiting app\n')
    bz.close()
    relay.close()
