import os 
import sys
import shutil

#New folder to be created in python file directory
newpath = r'Test'

#To be changed in Kivy
name = os.listdir(r"C:\Users")[1]
destination = "C:\Users\{0}\Documents\GitHub\Tech-Retreat-Demo\Test".format(name)

#Creates new folder if not already existing
if not os.path.exists(newpath):
	os.mkdir(newpath)
	print "Path Created"

#Copies a given file
def copy_file(src):
	shutil.copy(src, destination)

copy_file("C:\Users\{0}\Music\CopyFile.txt").format(name)
copy_file("C:\Users\{0}\Music\TestMP3.mp3").format(name)
copy_file("C:\Users\{0}\Music\Blazo - Cult Classic Records Present- Friends and Family - 03 Busy Dreaming.mp3").format(name)
copy_file(r"C:\Users\{0}\Music\13 Nutritious - Dash Cancel [Ultra Street Fighter IV].mp3").format(name)

