import speech_recognition as sr
import webbrowser
import time
import pyttsx3

# -------------------------------
# Text-to-Speech
# -------------------------------
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech (offline)."""
    engine.say(text)
    engine.runAndWait()

# -------------------------------
# Speech-to-Text
# -------------------------------
def listen():
    """Listen to microphone and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            speak("No input detected.")
            return ""
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return ""

# -------------------------------
# Command Handling
# -------------------------------
def process_command(command):
    """Perform actions based on the command."""
    if "time" in command:
        speak(f"The time is {time.ctime()}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if not search_term:
            speak("What do you want me to search for?")
            search_term = listen()
        if search_term:
            url = f"https://www.google.com/search?q={search_term}"
            speak(f"Searching for {search_term}")
            webbrowser.open(url)
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I am not sure how to do that.")

# -------------------------------
# Main Loop
# -------------------------------
if __name__ == "__main__":
    speak("Hello! How can I help you today?")
    while True:
        cmd = listen()
        if cmd:
            process_command(cmd)
