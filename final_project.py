import speech_recognition as sr
from selenium import webdriver

class Voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        print("Working...")
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(command)

                    if "search" in command:
                        driver = webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?q={command.split('search')[-1]}")
            except sr.UnknownValueError:
                pass
            except KeyboardInterrupt:
                print('ERR: KEYBOARD_INTERRUPTION')
                break

listener = Voice()