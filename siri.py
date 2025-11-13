# Project Name: BabySiri ( Voice Assistant )

# pip install speech_recognition
# pip install PyAudio
# pip install pyttsx3

# Libraries
import speech_recognition as sr   # for converting speech to text
import pyttsx3                    # for text to speech conversion
import datetime                   # to access system time
import webbrowser                 # used to access websites


# initialize text to speech engine
engine = pyttsx3.init()


# This function will speak the text passed to it
def speak(text):
    voices = engine.getProperty('voices')  # bring list of voices
    engine.setProperty('voice', voices[1].id)  # choose the voice (female)
    engine.say(text)
    engine.runAndWait()


# This function will listen to your voice command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print("Your Command:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I am not able to understand")
            speak("Sorry, I am not able to understand")
            return ""
        except sr.RequestError:
            print("Speech service not available")
            speak("Speech service not available")
            return ""


def run_assistant():
    speak("Hello, I am your Baby Siri. How can I help you?")
    while True:
        command = listen()

        if 'time' in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")   # Example: 08:45 PM
            print("Time:", current_time)
            speak(f"The current time is {current_time}")

        elif 'date' in command or 'today date' in command:
            today = datetime.date.today()
            current_date = today.strftime("%B %d, %Y")   # Example: November 10, 2025
            print("Date:", current_date)
            speak(f"Today's date is {current_date}")

        elif 'open google' in command:
            speak("Okay Sir, opening Google for you.")
            webbrowser.open("https://www.google.com/")

        elif 'exit' in command or 'stop' in command or 'go to hell' in command:
            speak("Okay bye bye, shutting down Baby Siri.")
            break

        elif command != "":
            speak("Sorry, I didn't get that. Please try again.")


run_assistant()
