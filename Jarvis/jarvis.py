import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import time
import pyjokes
import pyautogui
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',185)

#Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#To convert Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

        try: 
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query
#To wish 
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis. Please tell me how can I help you?")

#For news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6b4114cd60af4ca49f498f57885811c7'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__=="__main__":
    #speak("Hello Sir")
    #takecommand()
    wish()
    while True:
    #if 1:
        query=takecommand().lower()

        #logic building for tasks:

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        elif "set alarm" in query:
            speak("Sir, please tell me the time for the alarm in HH:MM format.")
            alarm_time = takecommand().lower()
            speak(f"Alarm is set for {alarm_time}.")
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                if current_time == alarm_time:
                    music_dir = 'C:\\Users\\edmun\\OneDrive\\Desktop\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Alarm is ringing, sir!")
                    break
                time.sleep(10)  # Check every 10 seconds to avoid excessive CPU usage


        elif "play music" in query:
            music_dir = "C:\\Users\\edmun\\OneDrive\\Desktop\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")
        
        # elif "open whatsapp":
        #     webbrowser.open("https://web.whatsapp.com/")
        
        elif "send message" in query:
            kit.sendwhatmsg("+919788695677","This is testing protocol",18,13)

        elif "play songs on youtube" in query:
            speak("What song should I play on Youtube")
            cm=takecommand().lower()
            kit.playonyt(f"{cm}")
        
        # elif "create a folder in desktop":
        #     speak("What should I name the folder?")
        #     folder_name = takecommand().lower()
        #     desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
        #     folder_path = os.path.join(desktop_path, folder_name)

        #     if not os.path.exists(folder_path):
        #         os.makedirs(folder_path)
        #         speak(f"Folder named {folder_name} has been created on your Desktop.")
        #     else:
        #         speak(f"A folder named {folder_name} already exists on your Desktop.")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "what is the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1) 
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")


        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")

        elif "lock the screen" in query:
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            break
        speak("Sir, do you have any other tasks")