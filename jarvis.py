import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr. vasu!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Mr. vasu!")
    else:
        speak("Good evening Mr. vasu!")
    speak("I am jarvis sir please tell me what can i do for you")
def tc():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"you said:{query}\n")
    except Exception as e:
        speak("pardon sir....")
        return "None"
        #print(e)
        
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gaarav31100@gmail.com','pardeep69')
    server.sendmail('gaarav31100@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    #tc()
    while True:
        query = tc().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia sir")
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube sir")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google sir")
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir= 'F:\\music\\P.p'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'open chrome' in query:
            path="C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif ' send email' in query:
            try:
                speak("what should i say?")
                content=tc()
                to= "gracygupta96@gmail.com"
                sendEmail(to, content)
                speak("email has been send sir")
            except Exception as e:
                print(e)
                speak("i am unable to send email")
        elif 'quit' or 'bye' in query:
            speak("bye bye sir it was nice to serve u")
            break



    
