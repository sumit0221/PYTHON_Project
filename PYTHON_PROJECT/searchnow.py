import speech_recognition
import pyttsx3
import pywhatkit
import webbrowser
import wikipedia


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


query = takecommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)


