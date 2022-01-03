import pyttsx3
from decouple import config
from datetime import datetime 
#variables required
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

#sapi5 to help us use the voices from microsoft
engine = pyttsx3.init('sapi5')

#Speed rate.. of voice
engine.setProperty('rate', 190)

#volume of voice
engine.setProperty('volume', 1.0)

#get voices will be list...
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()
def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if(hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif hour >= 12 and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif hour >= 16 and (hour < 19):
        speak(f"Good evening {USERNAME}")
    elif (hour >= 19):
        speak(f"I am not your mother but you should be sleeping {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you")
    