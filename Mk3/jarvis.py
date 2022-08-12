import datetime
import os
import random
import webbrowser
import requests
from Assets.Timer.autotimer import activate
import sqlite3
from Assets.subtitle.subtitle import subtitle
import pyshorteners
import sys
from spaceinvaders import start

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

import cv2

import pyautogui
import pyjokes
import scan_port

import winshell

from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from translate import Translator
from youtubetaggenerator.youtubetaggenerator import YoutubeTagGenerator

from Assets.Amazon import utils as u
from Assets.Deskcleaner import cleandesk as cd

from diction import translate
from loc import weather
from camera import face_rec, New_access
from control_keys import Tab_Opt, Win_Opt, Ctrl_Keys
from system_specs import System_specs

# from keylogger import keylogger_py

from Mk3 import speak, takecommand

# for the memory it should have
conn = sqlite3.connect('Assets/memory/memmory.db')
try:
    conn.execute("""CREATE TABLE MEMORY
                (USER_INPUT TEXT PRIMARY KEY NOT NULL);""")
except:
    pass

# chatbot = ChatBot('Jarvis')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")


none_counter = 0


def make_short(url_to_short):
    shorturl = pyshorteners.Shortener().tinyurl.short(url_to_short)
    return shorturl


def init_check():
    if internet_availability():
        if face_rec():
            return True
        else:
            return False
    else:
        return False


def authentication():
    speak("Hello and Welcome sir, I am Jarvis.")
    speak("Sir, I need to authenticate you.")
    auth_key = "jarvis"
    speak("Facial recognition underway")
    count = 0
    for i in range(51):
        if init_check():
            break

        else:
            count += 1
    if count == 50:
        speak("please authenticate yourself with your special word.")
        query = takecommand().lower()
        if query == auth_key:
            speak("Yes, i recognized you, you are an authorized user. and you are successfully logged in.")

        else:
            speak("Please type your answer")
            a = input()
            a = a.lower()
            if a == auth_key:
                speak("Yes, i recognized you, you are an authorized user. and you are successfully logged in.")
            else:
                speak(
                    "ok, you are not a authorized user. so you can't use this program. i am sorry but i am going "
                    "offline ")
                quit()


def internet_availability():
    try:
        url = "http://google.com/"
        timeout = 2
        _ = requests.get(url, timeout=timeout)
        return True
    except:
        speak("No internet connection!")
        return False


def create_Subtitle():
    k = input()
    subtitle(k)


def contain(data, words):
    for word in words:
        if word in data:
            return True
    return False


def access():
    speak("Are you confirm in access control transfer!")
    data = takecommand()
    if "confirm" in data or "yes" in data or "yeah" in data:
        speak("could you please say the name of  the person of whom you are going to give access")
        name = input()
        speak("okay")
        speak("new visual confirmation required!")
        New_access(name)
        speak("access control transferred successfully!")
        return
    else:
        speak("are you sure in cancelling access control transfer!")
        data = takecommand()
        if data == "yes":
            return
        else:
            access()


def scanning(addr):
    scan_port.scan(addr)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning SIR")
    elif 12 <= hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

    weather()
    speak('I am JARVIS. Please tell me how can I help you SIR?')


def joke():
    i = 0
    if i == 4:
        i = 0
    else:
        speak(pyjokes.get_jokes()[i])
        i += 1


def gooffline():
    speak('Closing all system applications.')
    speak('Disconnecting to servers.')
    speak('Going offline.')
    quit()


def online():
    speak('Starting all system applications.')
    speak('Every driver is installed.')
    speak('All system applications have been started.')
    speak('Now i am online Sir .')
    strDate = datetime.datetime.today().strftime("%d %B %y")
    speak(f"Sir, today's date is {strDate}.")
    wishMe()


def open_application(i):
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    if "chrome" in i:
        speak("Opening Google Chrome")
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

    elif "firefox" in i or "mozilla" in i:
        speak("Opening Mozilla Firefox")
        os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

    elif "word" in i:
        speak("Opening Microsoft Word")
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

    elif "excel" in i:
        speak("Opening Microsoft Excel")
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

    elif "notepad" in i:
        speak("Opening Notepad")
        os.startfile('C:\\Windows\\system32\\notepad.exe')

    elif 'youtube' in i:
        speak("Opening youtube")
        webbrowser.get('chrome').open("youtube.com")

    elif "stack overflow" in i:
        speak("Opening stackoverflow")
        webbrowser.get('chrome').open("https://stackoverflow.com")

    elif 'google' in i:
        speak("Opening google")
        webbrowser.get('chrome').open("google.com")

    elif 'explorer' in i:
        speak("Opening File Explorer")
        os.system('explorer.exe ')

    elif ('documents' in i) or ('documents' in i):
        speak("Opening Documents")
        os.startfile("C:\\Users\\sat_c\\Documents")
    elif 'github' in i:
        speak("Opening github")
        webbrowser.get('chrome').open_new_tab('https://github.com/')

    elif ('downloads' in i) or ('download' in i):
        speak("Opening Downloads")
        os.startfile("C:\\Users\\sat_c\\Downloads")

    elif "cmd" in i:
        os.system("start cmd.exe")

    else:
        speak("Application not available")


def closeapplication(i):
    if "chrome" in i:
        speak("Closing Google Chrome")
        os.system("taskkill /f /im chrome.exe")

    elif "firefox" in i or "mozilla" in i:
        speak("Closing Mozilla Firefox")
        os.system("taskkill /f /im firefox.exe")

    elif "word" in i:
        speak("Closing Microsoft Word")
        os.system("taskkill /f /im WINWORD.EXE")

    elif "excel" in i:
        speak("Closing Microsoft Excel")
        os.system("taskkill /f /im EXCEL.EXE")

    elif 'notepad' in i:
        speak("Closing Notepad")
        os.system('taskkill /f /im notepad.exe')

    elif 'youtube' in i:
        speak("Closing youtube")
        os.system("taskkill /f /im chrome.exe")

    elif 'google' in i:
        speak("Closing google")
        os.system("taskkill /f /im chrome.exe")

    elif "teams" in i:
        speak("closing Microsoft teams")
        os.system("taskkill /f /im Teams.exe")


def takephoto():
    if 'picture' or "photo" in query:
        camera_port = 0
        speak("Checking for camera availability.")
        speak("Clicking your Picture. Sir smile please.")
        camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        if not camera.isOpened():
            raise IOError("Cannot open webcam")
        grabbed, image = camera.read()
        speak("Your picture is clicked. it looks really nice.")
        speak("lets take a look.")
        print("Instructions : please Press Q to quit")
        speak("please Press Q to quit")

        while camera.isOpened():
            if grabbed:
                cv2.imshow('pic.jpg', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.imwrite('Image\\Photo\\pic.jpg', image)
                    speak("Picture has been saved.")
                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()

    elif 'screenshot' in query:
        speak("Taking a screenshot..")
        ss = pyautogui.screenshot()
        strDate = datetime.datetime.today().strftime("%d-%b-%y_")
        strTime = datetime.datetime.now().strftime("%H %M %S")
        ssName = "Image\\Screenshots\\" + strDate + strTime + ".png"
        ss.save(ssName)
        speak("Screenshot captured. and saved to storage.")

    elif 'selfie' in query:
        camera_port = 0
        speak("Checking for camera availability.")
        speak("Clicking your Picture. Sir smile please.")
        camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        # Check if the webcam is opened correctly
        if not camera.isOpened():
            raise IOError("Cannot open webcam")
        grabbed, image = camera.read()
        speak("Your picture is clicked. it looks really nice.")
        speak("lets take a look.")
        print("Instuctions : please Press Q to quit")
        speak("please Press Q to quit")

        while camera.isOpened():
            if grabbed:
                # out.write(image)
                cv2.imshow('pic.jpg', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.imwrite('Image\\Selfie\\pic.jpg', image)
                    speak("Picture has been saved.")
                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()


def sleep():
    global none_counter
    if none_counter < 3:
        none_counter += 1
    else:
        speak("I am going to sleep sir")
        while True:
            try:
                command = takecommand().lower()
                if "jarvis" in command:
                    speak("I am awake sir")
                    break
            except Exception:
                pass


def check_sleep(words):
    if 'sleep' in words or 'hibernate' or 'None' in words:
        sleep()
    if ('shut' in words and 'down' in words) or 'bye' in words or 'goodbye' in words:
        extPro = "I am going offline, Take care sir", "i am quitting", "Bye", "Bye. meet you soon.", "I am shutting " \
                                                                                                     "down, " \
                                                                                                     "Have a nice " \
                                                                                                     "day", \
                 "Goodbye. meet u soon "
        speak("Ok sir, " + random.choice(extPro))
        gooffline()


def search_web(query):
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located
    if 'youtube' in query.lower():
        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        query = str(query.split()[indx + 2:])
        webbrowser.get("Chrome").open_new_tab("https://www.youtube.com/results?search_query=" + query)
        return
    elif 'wikipedia' in query.lower():
        speak("Opening Wikipedia")
        indx = query.lower().split().index('wikipedia')
        query = query.split()[indx + 1:]
        webbrowser.get("Chrome").open_new_tab("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:
        if 'search' in query:
            query = query.split()
            try:
                indx = query.index("google")
            except:
                indx = query.index('search')
            query = query[indx + 2:]
            webbrowser.get("Chrome").open_new_tab("https://www.google.com/search?q=" + '+'.join(query))
        else:
            webbrowser.get("Chrome").open_new_tab("https://www.google.com/search?q=" + '+'.join(query.split()))
        return


if __name__ == '__main__':
    # authentication()
    # online()
    # still developing keylogger
    # keylogger_py()
    activate()
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    count_of_none = 0
    music_count = 0
    while True:

        query = takecommand().lower()

        if 'search' in query:
            search_web(query)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif 'jarvis are you there' in query:
            speak("Yes Sir, at your service")

        elif 'open' in query:
            open_application(query)

        elif 'take' in query:
            takephoto()

        elif 'play music' in query:
            if music_count == 0:
                webbrowser.get('Chrome').open_new_tab('https://www.youtube.com/watch?v=f02mOEt11OQ')

            elif "next" in query:
                music_count += 1

            elif music_count == 1:
                webbrowser.get('Chrome').open_new_tab('https://www.youtube.com/watch?v=knGM3Y2e6Ks')

            elif music_count == 2:
                webbrowser.get('Chrome').open_new_tab("https://www.youtube.com/watch?v=oPVte6aMprI")

            elif music_count == 3:
                webbrowser.get('Chrome').open_new_tab("https://www.youtube.com/watch?v=9vWNauaZAgg")
                music_count = 0

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            h, m, s = strTime.split(":")
            h = int(h)
            m = int(m)
            s = int(s)
            if h > 12:
                h -= 12
            speak(f'Sir, the time is {h}:{m}')

        elif "scan port" in query:
            speak("Please type in the IPV4 ADDR")
            a = input("Please type the IPV4 address:\n")
            scanning(a)

        elif 'location' in query:
            speak('What is the location you are searching for?')
            location = takecommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            speak('Darshan is my master. He created me couple of days ago')

        elif 'your name' in query:
            speak('My name is JARVIS')

        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif 'joke' in query:
            joke()

        elif 'remember' in query:
            speak("what should i remember sir")
            rememberMessage = takecommand()
            speak("you said me to remember" + rememberMessage)
            remember = open('data.txt', 'a+')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif "clear reminders" in query:
            remeber = open("data.txt", "w")
            remeber.write("")
            speak("Done Sir")

        elif 'dictionary' in query:
            speak('What do you want to search in your dictionary, Sir?')
            translate(takecommand())

        elif 'clear bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                speak('Trash Cleared!')
            except Exception as e:
                speak('Bin is clean sir!')

        elif "amazon" in query:
            speak("What do you want to search amazon for, Sir?")
            a = input()
            u.main(a)
            u.sort_results_by_price("results.csv")
            u.sort_results_by_discount("results.csv")
            u.get_discount_page("sorted_by_discount.csv")

        elif "clean dir" in query:
            speak("Please type in the dir you want organized?")
            a = input()
            speak(
                "Please put a folder inside the folder that you want to organize. This new folders name should be "
                "Sorted with a capital S")
            b = f"{a}/Sorted"
            cd.activate(a, b)

        elif "generate tags" in query:
            speak("What is the title Sir?")
            a = input()
            obj = YoutubeTagGenerator(title=a)
            print(obj.getTags)

        elif 'translate' in query:
            speak("Whats should i translate?")
            trans_content = takecommand()
            speak("In which language do you wish to translate?")
            trans_Lang = takecommand()
            translator = Translator(to_lang=trans_Lang)
            translation = translator.translate(trans_content)
            speak("Translation of  : " + trans_content + " is " + translation)

        elif "close" in query:
            closeapplication(query)

        elif ('record video' in query) or ('record a video' in query):
            speak("Recording a video.")
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('Video\\output.mp4', -1, 20.0, (640, 480))
            print("Instructions : please Press Q to stop recording")
            speak("please Press Q to stop recording")
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                    cv2.imshow('Recording Video..', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        speak("Video has been saved.")
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()

        elif contain(query,
                     ['select all', 'cut', 'copy', 'paste', 'history', 'download', 'undo', 'redo', 'save', 'enter',
                      'search', 'find']):
            Ctrl_Keys(query)

        elif "access" in query:
            access()

        elif "internet connection" in query or "connection" in query:
            if internet_availability():
                speak("Internet Connection is okay!")

        elif "tab" in query:
            Tab_Opt(query)

        elif "window" in query:
            Win_Opt(query)

        elif contain(query, ["battery", "cpu", "memory", "brightness"]):
            System_specs(query)

        elif "thank you" in query:
            speak("Your welcome")

        elif "type" in query:
            try:
                indx = query.split().index("type")
            except Exception:
                break
            query = query.split()[indx + 1:]
            pyautogui.write(query)

        elif "math" in query:
            speak("Type your question please")
            a = input("What is your question:\n")
            nums = list(a)
            unwanted_num = {"+", " ", "/", "*", "-"}
            if '+' in nums:
                nums = [ele for ele in nums if ele not in unwanted_num]
                print("It is " + str(int(nums[0]) + int(nums[1])))
            if '-' in nums:
                nums = [ele for ele in nums if ele not in unwanted_num]
                print("It is " + str(int(nums[1]) - int(nums[0])))
            if "*" in nums:
                nums = [ele for ele in nums if ele not in unwanted_num]
                print("It is " + str(int(nums[0]) * int(nums[1])))
            if '/' in nums:
                nums = [ele for ele in nums if ele not in unwanted_num]
                print("It is " + str(int(nums[0]) / int(nums[1])))

        elif "subtitle" in query:
            create_Subtitle()

        elif "shorten" and "url" in query:
            speak("Please type your url")
            a = input("What is your url:\n")
            print(make_short(a))

        elif "game" in query:
            speak("Shall we play a game ?")
            start()

        check_sleep(query)
        # elif 'safe' in query:
        #     m()
        #
        # else:
        #     speak(chatbot.get_response(query))
