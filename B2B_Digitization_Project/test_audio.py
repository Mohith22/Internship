import speech_recognition as sr
import sys
import pandas as pd
from pyexcel_ods import save_data,get_data
from collections import OrderedDict
import json
import ast

reload(sys)
sys.setdefaultencoding('utf-8')
# Record Audio
indata = []
c=1

init_data = get_data("sample.ods")
init_data = json.dumps(init_data)
init_data = ast.literal_eval(init_data)
init_data = init_data['Sheet 1']

for i in init_data:
	indata.append(i)


while(1):



	if c==1:
		r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("Say Invoice:")
		    audio = r.listen(source)
		 
		# Speech recognition using Google Speech Recognition
		try:
		    print("Invoice: " + r.recognize_google(audio))
		    invoice = r.recognize_google(audio)
		except sr.UnknownValueError:
		    print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))

		low_incase = invoice.lower()
		if low_incase == "bye":
			break;
	if c==2:

		r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("Say Date:")
		    audio = r.listen(source)
		 
		# Speech recognition using Google Speech Recognition
		try:
		    print("Date: " + r.recognize_google(audio))
		    date = r.recognize_google(audio)
		except sr.UnknownValueError:
		    print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))

	if c==3:
		data = OrderedDict()
		indata.append([invoice,date])
		data.update({"Sheet 1": indata})
		print data
		save_data("sample.ods",data)
		c=0


	c=c+1


