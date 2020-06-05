from tkinter import *
import wikipedia
import wolframalpha
import os
from gtts import gTTS
import requests
import re
import webbrowser
import urllib.request
import urllib.parse
import bs4
import time
from selenium import webdriver
from IPython.display import clear_output


def on_enter(event):
	
	q=get_q.get() #command
	language='en'
	myobj=gTTS(text='Recognising your command.Please wait',lang=language,slow=False)
	myobj.save("welcome.mp3")
	os.system("mpg321 welcome.mp3")
	if 'open google' in q:
        #matching command to check it is available
        	reg_ex = re.search('open google (.*)',q)
        	url = 'https://www.google.com/'
        	if reg_ex:
            		subgoogle = reg_ex.group(1)
            		url = url + 'r/' + subreddit
       		webbrowser.open(url)
        	print('Done!')
	elif 'open' in q:
		open_application(q.lower())
		return


	try:
		try:
			app_id="U4U65X-KYKW4UAQHU"
			client=wolframalpha.Client(app_id)

			res=client.query(q)
			answer=next(res.results).text
		
		#text.insert(INSERT,answer)
			tts=gTTS(answer,lang='en')
			tts.save("wolf.mp3")
			os.system(" mpg321 wolf.mp3")
		
		except:
			google_search(q)
	except:
		#google search
		try:
			summary=wikipedia.summary(q,sentences=2)
			#text.insert(INSERT,summary)
			tts=gTTS(summary,lang='en')
			tts.save("wiki.mp3")
			os.system("mpg321 wiki.mp3")
	
		except:
			google_search(q)
			
def google_search(q):
			tts=gTTS(text="Opening Google for your search",lang='en')
			tts.save("gog.mp3")
			os.system("mpg321 gog.mp3")
	
			new =2

			tabUrl="https://google.com/?#q="
			webbrowser.open(tabUrl+q,new=new)
			
def open_application(q):
	if 'firefox' in q:
		tts=gTTS(text="Opening firefox",lang='en')
		tts.save("fire.mp3")
		os.system("mpg321 fire.mp3")
		os.system('/snap/bin/firefox')
		return
	elif 'videos' in q:
		tts=gTTS(text="Opening Videos",lang='en')
		tts.save("video.mp3")
		os.system("mpg321 video.mp3")
		os.system('totem %U')
		return
	elif 'amazon' in q:
		tts=gTTS(text="Opening Amazon",lang='en')
		tts.save("ama.mp3")
		os.system("mpg321 ama.mp3")
		os.system("/usr/share/ubuntu-web-launchers/amazon-launcher")
		return
	elif 'calendar' in q:
		tts=gTTS(text="opening Calendar",lang='en')
		tts.save("calen.mp3")
		os.system("mpg321 calen.mp3")
		os.system('gnome-calendar')
		return
	elif 'calculator' in q:
		tts=gTTS(text="Opening Calculator",lang='en')
		tts.save("cal.mp3")
		os.system("mpg321 cal.mp3")
		os.system('gnome-calculator')
		return
		
root=Tk()
root.title('Virtual Assistance')
quest=Label(root,text="Give me any command",bg='powder blue',fg='white',font='arial 12 bold')
quest.pack()
root.config(background='powder blue')
root.geometry("500x50")
get_q=Entry(root,width=50)
get_q.pack()
language='en'
myobj=gTTS(text='Hello I am Friday.How can I help you',lang=language)
myobj.save("welcome1.mp3")
os.system("mpg321 welcome1.mp3")


root.bind('<Return>',on_enter)
text=Text(root)
#text.pack()

root.mainloop()
