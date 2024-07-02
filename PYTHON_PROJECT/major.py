import pyttsx3
import speech_recognition
import webbrowser
import requests
import datetime
from bs4 import BeautifulSoup
import os
import pyautogui
import keyboard
import speedtest
from plyer import notification
from pygame import mixer
import searchnow 
import speedtest
import random




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone()  as source :
        print("Listening you sir ...")
        r.pause_threshold = 1
        r.energy_threshold=250
        audio = r.listen(source,0,3)

    try:
        print("recognizing..")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You said that : {query}\n")
    except Exception as e :
        print("Error in listening , please say again")
        return "NONE"
    return query





if __name__ == "__main__" :
    while True :
        query = takecommand().lower()    
        # for taking the command 
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime if you need me")
                    break 

            # ******* search engine  **********   WORKING
                elif "google" in query :
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchWikipedia
                    searchWikipedia(query)


            

            # ********WHATSAPP MESSENGER ********* -->> working 
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


            #***** Finding my internet speed ******* -- WORKING
              #Megabyte = 1024*1024 Bytes
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                #******remember my details ******* -->>  WORKING
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())


                #*******MOOD CHANGER *********** -->> WORKING
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/Az-mGR-CehY?si=DrvgfHAxZDQ-XFJF")
                    elif b==2:
                        webbrowser.open("https://youtu.be/1-xGerv5FOk?si=shB1GYkdaColkSkv")
                    elif b==3:
                        webbrowser.open("https://youtu.be/dhYOPzcsbGM?si=_QvBXN6M5xRhYSCc")

                 #******* FOR NORMAL CONVERSATION ***** WORKING 
                elif "hello friday" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thanks" in query:
                    speak("you are welcome, sir")



                     #FOR SHUT DOWN THE SYSTEM --- >> WORKING
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break 

            

    # ********** FOR YOUTUBE CONTROLS ************** WORKING
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

            # ************FOR OPENING ANY SPECIFIC APP***********  WORKING
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

            # **********for taking screenshot********** WORKING
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

            # ************for taking camera*************** WORKING
                elif "take a picture" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

            # ********for temperature and weather report ******* WORKING
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                #for jarvis to stop working for you----->> WORKING
                elif "sleep jarvis" in query:
                    speak("Good night , Sir")
                    exit()
