from pyttsx3 import init
import speech_recognition as sr
from Assets import *

engine = init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception:
        print('Say that again please...')
        return 'None'
    return query
