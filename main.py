import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
 
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
        
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")
                
        
chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"jignesh: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    speak("Welcome to Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()

        if "open music" in query:
            musicPath = "/Users/jignesh/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/jignesh/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} bajke {min} minutes")

        elif "open" in query:
            Nameofweb = query.replace("open ","")
            Link = f"https://www.{Nameofweb}"
            speak(f"Opening {Nameofweb}sir...")
            webbrowser.open(Link)

        elif "open github" in query:
            webbrowser.open_new_tab("github.com")

        elif "open facetime".lower() in query.lower():  
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")
        
        elif "who created you" in query or "who devloped you" in query or "who creted you" in query or "who design you" in query or "who tryed to devlope you" in query or "how are you devloped" in query:
            speak("i was Devloped by jignesh jogal in 20 days")

        elif "help me fast" in query:
           speak("just a mintue, tell me your situation") 
           # incompleted     

        elif "call to cop" in query:
            speak("calling to cop")    
            # incompleted      

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Checking...")
            chat(query)





