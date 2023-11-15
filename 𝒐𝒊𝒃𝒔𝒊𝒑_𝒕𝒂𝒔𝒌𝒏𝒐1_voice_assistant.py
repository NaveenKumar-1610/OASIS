voice assistant :

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't reach the internet.")
        return ""

# Function to handle user commands
def handle_commands(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
    else:
        speak("I'm not sure how to help with that.")

# Main loop for continuous interaction
speak("Hello! How can I assist you today?")
while True:
    user_input = listen()
    if user_input:
        handle_commands(user_input)
/// also 
To run the voice assistant code in VS Code, you'll need to ensure that you have the required Python libraries installed. You can install them using pip:

bash
Copy code
pip install SpeechRecognition pyttsx3
