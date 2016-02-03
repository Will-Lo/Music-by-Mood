from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

import os 
import sys
import shutil
import pyen
import time

#To be changed in Kivy
#tempo = "Placeholder"
name = os.listdir(r"C:\Users")[1]

	
#API Information
en = pyen.Pyen("XXY4BU0R8WQMMQQ64")
en.trace = False

Study = []
Workout = []
Sleep = []
Relax = []
	
	
def create_dest(name, tempo, mp3):
	return ((main_folder(mp3) + "\{0}").format(tempo))
		
#creates a folder if one doesn't previously exist
def main_folder(mp3):
	folder = os.path.dirname(os.path.realpath(mp3))
	if not os.path.exists(folder + "\Playlists"):
		os.mkdir(folder + "\Playlists")
		print "Path Created"
	return (folder + "\Playlists")
	
#Creates sub folder        
def sub_folder(mainF, sub):
	if not os.path.exists("{0}/{1}".format(mainF, sub)):
		os.mkdir("{0}/{1}".format(mainF, sub))
	else:
		return None
			
#Get list of all files ending with a desired file extension
def get_ext(files):
	ext_list = []
	for file in files:
		if file.endswith(".mp3"):
			ext_list.append(file)
	return ext_list
			
#Copies a given file
def copy_file(mp3, tempo):
	destination = create_dest(name, tempo, mp3)
	shutil.copy(mp3, destination)

def wait_for_analysis(id, mp3):

	while True:
		response = en.get('track/profile', id=id, bucket=['audio_summary'])
		if response['track']['status'] <> 'pending':
			break
		time.sleep(1)

	list = []

	#for k,v in response['track']['audio_summary'].items():
		#print "%32.32s %s" % (k, str(v))
	tempo_speed = response['track']['audio_summary']['tempo']
	loudness = response['track']['audio_summary']['loudness']
	#Slow and Soft
	if tempo_speed <= 108 and loudness <= -7:
		Sleep.append(id)
		Sleep.append(tempo_speed)
		Sleep.append(mp3)
		print Sleep
		tempo = "Sleeping"
		copy_file(mp3, tempo)
	
	#Fast and Loud
	elif tempo_speed > 108 and loudness > -7:
		Workout.append(id)
		Workout.append(tempo_speed)
		Workout.append(mp3)
		print Workout
		tempo = "Workout"
		copy_file(mp3, tempo)
	
	#Slow and Loud
	elif tempo_speed <= 108 and loudness > -7:
		Relax.append(id)
		Relax.append(tempo_speed)
		Relax.append(mp3)
		print Relax
		tempo = "Relaxing"
		copy_file(mp3, tempo)
	
	#Fast and Soft
	else:
		Study.append(id)
		Study.append(tempo_speed)
		Study.append(mp3)
		print Study
		tempo = "Studying"  
		copy_file(mp3, tempo)
		
class Application(Tk):
	
	def get_file(self):
		self.filename = askopenfilename()
	
	def get_folder(self):
		self.filelist = get_ext(os.listdir(askdirectory()))
		print self.filelist

	def run_code(self):     

		a = main_folder(self.filename)
		sub_folder(a, "Studying") #Fast+Soft
		sub_folder(a, "Workout") #Fast + Loud
		sub_folder(a, "Sleeping") #Slow + Soft
		sub_folder(a, "Relaxing") #Slow + Loud
		f = open(self.filename, 'rb')
		response = en.post('track/upload', track=f, filetype='mp3')
		trid = response['track']['id']
		print 'track id is', trid
		wait_for_analysis(trid, self.filename)

	def createWidgets(self):
		#button that closes the application
		self.close = ttk.Button(text="close", command=self.quit, style = "C.TButton")
		self.close.pack()
		self.close.place(relx=0.6, rely=0.8)
		
		#button that opens a filename prompt
		self.openfile = ttk.Button(text="select a file", command=self.get_file, style = "C.TButton")
		self.openfile.pack()
		self.openfile.place(relx=0.6, rely=0.2)
		
		#button that opens a file directory prompt
		self.openfile = ttk.Button(text="select a folder", command=self.get_folder, style = "C.TButton")
		self.openfile.pack()
		self.openfile.place(relx=0.6, rely=0.4)

	
		#button that does music analysis with the Echonest API
		self.runcode = ttk.Button(text="start analyzing!", command=self.run_code, style = "C.TButton")
		self.runcode.pack()
		self.runcode.place(relx=0.6, rely=0.6)
	
	
	def __init__(self, master=None):
		Tk.__init__(self)
		self.createWidgets()
		
# start the program
if __name__ == '__main__':
	root = Application()
	root.configure(background='midnight blue')
	style = ttk.Style()
	style.map("C.TButton",
    background=[('pressed', '!disabled', 'royal blue'), ('active', 'deep sky blue')]
    )
	root.mainloop()   
	




