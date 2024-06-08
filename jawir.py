import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Jawir")

MASTER = "Yaseru"

engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
        
    else:
        speak("Good Evening" + MASTER)
        speak("")
        
#Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-us")
        print(f"user: {query}\n")
        
    except Exception as e:
        print("Suara tidak jelas,mohon diulang")
        query = None
    
    return query
        
#Main Code
speak("Hello my name is Jawir,I can help you!")
wishMe()
query = takeCommand()