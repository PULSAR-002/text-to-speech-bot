import speech_recognition as sr
import pyautogui
import time
import subprocess


# Function to launch Notepad
def open_notepad():
    subprocess.Popen(['notepad.exe'])


# Function to listen to voice input and type it
def voice_to_text():
    recognizer = sr.Recognizer()

    # Start listening to the microphone
    with sr.Microphone() as source:
        print("Please say something...")
        #recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen to the user's speech

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Use Google's speech-to-text engine
        print(f"You said: {text}")

        # Simulate typing in Notepad
        pyautogui.write(text)
        pyautogui.press('enter')  # Press Enter key after typing

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


if __name__ == "__main__":
    open_notepad()  # Open Notepad
    time.sleep(2)  # Wait for Notepad to open
    voice_to_text()  # Start listening to voice input
