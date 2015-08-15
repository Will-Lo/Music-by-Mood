import os 
import sys
import shutil

#New folder to be created in python file directory
newpath = r'Test'

destination = "C:\Users\Colin\Documents\GitHub\Tech-Retreat-Demo\Test"

#Creates new folder if not already existing
if not os.path.exists(newpath):
	os.mkdir(newpath)
	print "Path Created"

#Copies a given file
def copy_file(src):
	shutil.copy(src, destination)

copy_file("C:\Users\Colin\Music\CopyFile.txt")
copy_file("C:\Users\Colin\Music\TestMP3.mp3")
