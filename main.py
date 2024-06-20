import pyttsx3 as p
import speech_recognition as sr
import pyjokes
from greet import *
from selenium_web import Info
from YT_audio import *
from news import *
import sys
import randfacts
from weather import *
import os
import datetime

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    r = sr.Recognizer()
    greet()
    print("Welcome, I am your desktop voice assistant. How are you?")
    speak("Welcome, I am your desktop voice assistant. How are you?")


    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("User: " + text)

    if "what" and "about" and "you" in text:
        speak("I'm having a good day sir!")

    while True:
        sleep(2)
        print("What else can I do for you?")
        speak("What else can I do for you?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening....")
            audio = r.listen(source)
            text2 = r.recognize_google(audio)
            print("User: " + text2)

        if "Wikipedia" in text2:
            print("you need information related to which topic?")
            speak("you need information related to which topic?")

            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening....")
                audio = r.listen(source)
                information = r.recognize_google(audio)
            print("{}".format(information))
            speak("searching {} in wikipedia".format(information))
            info_instance = Info()
            info_instance.get_info(information)
            continue

        elif "YouTube" in text2:
            speak("you want me to play which video?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening....")
                audio = r.listen(source)
                vid = r.recognize_google(audio)
            print("Playing {} on Youtube".format(vid))
            speak("Playing {} on Youtube".format(vid))
            youtube_player = YouTubePlayer()
            youtube_player.search_and_play_video(vid)
            continue

        # Check if the user asks for a joke
        elif "joke" in text2:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            continue

        elif "news" in text2:
            print("Here are some news headlines")
            speak("Here are some news headlines")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
            continue

        elif "fact" in text2:
            x = randfacts.get_fact()
            print("Did you know that, " + x)
            speak("Did you know that, " + x)
            continue

        elif "temperature" in text2:
            print("The current temperature in Mumbai is " + str(temp()) + " " + str(des()))
            speak("The current temperature in Mumbai is " + str(temp()) + "degree celsius" + str(des()))
            continue

        elif "date" in text2:
            today_date = datetime.datetime.now()
            print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime(
                "%B") + " and the year is " + today_date.strftime("%Y"))
            speak("Today is "+ today_date.strftime("%d") + " of " + today_date.strftime(
                "%B") + "and the year is " + today_date.strftime("%Y"))
            continue

        elif "the time" in text2:
            today_date = datetime.datetime.now()
            print("It is " + today_date.strftime("%I") + ":" + today_date.strftime("%M") + " " + today_date.strftime("%p"))
            speak("It is " + today_date.strftime("%I") + today_date.strftime("%M") + today_date.strftime("%p"))
            continue

        elif "exit" in text2:
            print("Have a great day!")
            speak("Have a great day!")
            sys.exit()

except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
    speak("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    speak("Could not request results from Google Speech Recognition service.")
except Exception as e:
    print("An error occurred:", e)
    speak("An error occurred. Please try again.")
