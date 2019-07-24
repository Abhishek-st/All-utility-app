import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18:
        speak("Good Evening")
    speak("Hello, I am jarvis . How may I help you ")


def take():
    s = input("give command")
    return s


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    # speak("Meri mummy khana bana rahi hai")
    wishme()
    # q = take_command()

    while True:
        query = take()
        query = query.lower()
        if "add" in query:
            q = query.split()
            s = 0
            for i in q:
                if i.isnumeric():
                    s += int(i)
            speak(f"Your answer is {s}")

        elif "mul" in query:
            q = query.split()
            s = 1
            for i in q:
                if i.isnumeric():
                    s *= int(i)
            speak(f"Your answer is {s}")

        elif "sub" in query:
            q = query.split()
            s = 0
            for i in q:
                if i.isnumeric():
                    s -= int(i)
            speak(f"Your answer is {s}")

        elif "youtube" in query:
            webbrowser.open("youtube.com")
            speak("ok sir it will be opened in few seconds ")

        elif "google" in query:
            webbrowser.open("google.com")
            speak("ok sir it will be opened in few seconds ")

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            c = wikipedia.summary(query, sentences=1)
            print(c)
            speak(c)

        elif "music" in query or "video" in query:
            mu = 'F:\\my songs'
            query = query.replace("music", "")
            query = query.replace("play", "")
            query = query.replace("video", "")
            query = query.replace(" ", "")
            songs = os.listdir(mu)
            for i in songs:
                k = i.split("_")
                if query.lower() in k:
                    os.startfile(os.path.join(mu, i))
                    break
                elif query.upper() in k:
                    os.startfile(os.path.join(mu, i))
                    break
                elif query.capitalize() in k:
                    os.startfile(os.path.join(mu, i))
                    break
            else:
                print("Sorry file not found")
                speak("Sorry file not found")

        elif "quit" in query:
            break

        elif "code" in query:
            os.startfile(os.path.join('C:\\Program Files (x86)\\CodeBlocks', 'codeblocks.exe'))
        else:
            print("Sir I am unable to understand, can you say that again please")
            speak("Sir I am unable to understand, can you say that again please")
