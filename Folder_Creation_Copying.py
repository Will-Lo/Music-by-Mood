import os 
import sys
import shutil

#New folder to be created in python file directory
newpath = r'Test'

#To be changed in Kivy
name = os.listdir(r"C:\Users")[1]
destination = "C:\Users\{0}\Documents\GitHub\Tech-Retreat-Demo\Test".format(name)

#Creates new folder if not already existing
def mainFolder(new):
    if not os.path.exists(new):
        os.mkdir(new)
        print "Path Created"

#Creates sub folder        
def sub_folder(mainF, sub):
    if not os.path.exists("{0}/{1}".format(mainF, sub)):
        os.mkdir("{0}/{1}".format(mainF, sub))
        
#Copies a given file
def copy_file(src):
    shutil.copy(src, destination)

def main():     
    
    mainFolder(newpath)
    sub_folder(newpath, "Playlist")
    copy_file("C:\Users\{0}\Music\CopyFile.txt".format(name))
    copy_file("C:\Users\{0}\Music\TestMP3.mp3".format(name))
    copy_file("C:\Users\{0}\Music\Blazo - Cult Classic Records Present- Friends and Family - 03 Busy Dreaming.mp3".format(name))
    copy_file(r"C:\Users\{0}\Music\13 Nutritious - Dash Cancel [Ultra Street Fighter IV].mp3".format(name))

main()