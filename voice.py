import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time

recognizer=sr.Recognizer()


def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 177)
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening ...")
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            audio=recognizer.listen(source,timeout=5,phrase_time_limit=5) 
        
        command=recognizer.recognize_google(audio).lower()
        print("You said:",command)

        if "youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")
            time.sleep(0.25)
            
        elif "time" in command:
            current_time=datetime.now().strftime("%H:%M")
            speak("Time is "+current_time)
            time.sleep(0.25)

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye")
            break
    
        else:
            speak("I did not understand")
            time.sleep(0.25)

    except sr.WaitTimeoutError:
        print("Listening timed out...")

    except sr.UnknownValueError:
        print("Could not understand audio")        
    except Exception as e:
            print("Error:", e)

