#This project is done with the help of https://www.geeksforgeeks.org/convert-text-speech-python-using-win32com-client/
import win32com.client
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 Created by Ayush")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    while True:
        s = input("Enter what you want me to speak : ")
        if s == 'Q':
            speaker.Speak("bye bye friend Nice to meet you see you soon'")
            break
        speaker.Speak(s)



