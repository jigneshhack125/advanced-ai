import datetime
from main import speak
import subprocess
import keyboard
import pyautogui

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour== 20 :
		keyboard.press('enter')
		keyboard

	elif hour>= 12 and hour<18:
		

	else:
		speak("none")