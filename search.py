# for this library to work, we need to add flask library as well.
import pywhatkit
import pyttsx3
import speech_recognition as sr

# pywhatkit.search("Github")

# Python program to translate
# speech to text and text to speech

import pyaudio


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

if __name__ == '__main__':
    while (1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                SpeakText("Hello there, what do you want to search today")
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using g0ogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                text = "Did you say "+MyText
                print(text)
                pywhatkit.search(MyText)
                SpeakText(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

"""
num = number of results we want
stop = the last result to retrieve, use none for searching infinitely
pause = Lapse to wait between HTTP requests
"""
