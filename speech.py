import speech_recognition as sr
import subprocess
import webbrowser
import os
import time

# Initialize recognizer
r = sr.Recognizer()

# Define command actions
def open_app(path):
    subprocess.Popen([path])

def open_website(url):
    webbrowser.open(url)

def say_hello():
    print("Hello! How can I help you today?")

def shutdown():
    os.system("shutdown /s /t 1")

# Command map
commands = {
    "open chrome": lambda: open_app(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    "open notepad": lambda: open_app("notepad.exe"),
    "open calculator": lambda: open_app("calc.exe"),
    "open command prompt": lambda: open_app("cmd.exe"),
    "open youtube": lambda: open_website("https://www.youtube.com"),
    "open google": lambda: open_website("https://www.google.com"),
    "say hello": say_hello,
    "shut down computer": shutdown,
}

# Main loop
print("Voice assistant is running. Say a command...")
print("Say 'stop listening' to exit.")

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("\nListening...")
            audio = r.listen(source)

        text = r.recognize_google(audio).lower()
        print(f"You said: {text}")

        if "stop listening" in text:
            print("Voice assistant stopped.")
            break

        matched = False
        for phrase, action in commands.items():
            if phrase in text:
                print(f"Executing: {phrase}")
                action()
                matched = True
                break

        if not matched:
            print("Sorry, I didn't recognize that command.")

    except sr.UnknownValueError:
        print("Didn't catch that. Try again.")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    except KeyboardInterrupt:
        print("\nManually stopped.")
        break

    time.sleep(1)  # Short pause to avoid overlapping input
