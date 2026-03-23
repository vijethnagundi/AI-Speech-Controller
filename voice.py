import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Somthing...")
    audio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(audio)
        print("You said:",text)
    except:
        print("Sorry, could not understand")
