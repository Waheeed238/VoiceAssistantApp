import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
import time
import sys

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, the speech service is down.")
        return None

# Function to perform commands
def perform_command(query):
    # Basic commands:
    if 'hello' in query:
        speak("Hello! How can I help you today?")
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'what time is it' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif 'play music' in query:
        speak("Playing music")
        os.system("start music.mp3")  # Ensure you have a music file named 'music.mp3' in the working directory.
    elif 'tell me a joke' in query:
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif 'search for' in query:
        query = query.replace('search for', '')
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    elif 'exit' in query:
        speak("Goodbye!")
        sys.exit()
    elif 'who are you' in query:
        speak("I am your voice assistant.")
    elif 'what is your name' in query:
        speak("My name is Assistant.")
    else:
        speak("Sorry, I didn't understand that.")

# Main function to run the assistant
def main():
    speak("Hello, I am your voice assistant. How can I assist you?")
    while True:
        query = listen()

        if query:
            perform_command(query)

if __name__ == "__main__":
    main()
