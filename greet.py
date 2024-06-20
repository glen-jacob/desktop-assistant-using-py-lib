import datetime
from pyttsx3 import speak
def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        print("Good morning!")
        speak("Good morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
        speak("Good afternoon!")
    elif 18 <= hour < 22:
        print("Good evening!")
        speak("Good evening!")