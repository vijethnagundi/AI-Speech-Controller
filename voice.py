import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time
import os
import pyautogui

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
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source,timeout=5,phrase_time_limit=5) 
        
        command=recognizer.recognize_google(audio).lower()
        print("You said:",command)

        if "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")
            time.sleep(0.25)

        elif "open chrome" in command:
            os.system("start chrome")
            speak("Opening Chrome")
            time.sleep(0.25)

        elif "open notepad" in command:
            os.system("start notepad")
            speak("Opening Notepad")
            time.sleep(0.25)

        elif "open vscode" in command or "open vs code" in command:
            os.system("code")
            speak("Opening VS Code") 
            time.sleep(0.25)

        elif "time" in command:
            current_time=datetime.now().strftime("%H:%M")
            speak("Time is "+current_time)
            time.sleep(0.25)

        elif any(word in command for word in ["type", "write", "right", "taip"]):
            speak("What should I type?")
            
            with sr.Microphone() as source:
                audio=recognizer.listen(source)
            
            text=recognizer.recognize_google(audio)
            print("Typing:",text)

            pyautogui.write(text,interval=0.05)
            time.sleep(1)
            speak("Typed successfully")

        elif "enter" in command:
            pyautogui.press("enter")

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

