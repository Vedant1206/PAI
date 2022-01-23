# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyttsx3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say("testing voice")

    engine.runAndWait()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
