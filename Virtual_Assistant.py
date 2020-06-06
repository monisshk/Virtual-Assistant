import pyttsx3
import speech_recognition as sr 
import datetime
import os
import smtplib
import wikipedia 
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.setProperty('rate',170)
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
volume = engine.setProperty('volume',4.5)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12 :
        speak("Good Morning ")

    elif hour>=12 and hour <18:
        speak("Good Afternoon !!")
    elif hour>=18 and hour <20:
        speak("Good Evening ")
    else:
        speak("Good Night")   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        #r.pause_threshold = 1
        r.energy_threshold = 1207.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query  

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your_passwrod')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

wishMe()

while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 1)
        print(results)
        speak(results)

    elif 'hello' in query:
        speak("Hello, How may I help you ?")

    elif 'how are you' in query:
        speak("Yes I am fine ... ")

    elif 'thank you' in query:
        speak("Your most Welcome Sir !!")

    elif 'what is your name' in query:
        speak("My name is Lady Jarvis.")
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        speak("Opening Youtube Sir ")

    elif 'open google' in query:
        webbrowser.open("google.com")
        speak("Opening Google Sir ")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        speak("Opening StackOverFLow Sir ")

    elif 'gmail' in query:
        webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
        speak("Opening your Gmail Inbox Sir !!")
    
    elif 'hotstar' in query:
        webbrowser.open("https://www.hotstar.com/in")
        speak("Opening Hotstar Sir ")

    elif 'music' in query:
        dir_music="PATH"
        musics=os.listdir(dir_music)
        speak("Playing Music Sir !!!")
        os.startfile(os.path.join(dir_music,random.choice(musics)))
        
    elif 'movie' in query:
        dir_video="PATH"
        videos = os.listdir(dir_video)
        print(videos)
        os.startfile(os.path.join(dir_video,random.choice(videos)))

    elif 'time' in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir The time is {strTime}")

    elif 'email' in query:
        try:
            speak("What should I say ?")
            content = takeCommand()
            to="prince007ch@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry I can't send email right now Sir")

    elif 'twitter' in query:
        webbrowser.open("https://twitter.com/home")
    
    elif 'wallpaper' in query:
        speak("Opening your wallpaper Gallery")
        speak("Select the wallpaper Sir")
        wp_dir="D:\\My Wallpapers"
        wp=os.listdir(wp_dir)
        os.startfile(wp_dir)

    elif 'quit' in query:
        speak("Bye Bye Sir !! Meet Soon")
        exit(0)