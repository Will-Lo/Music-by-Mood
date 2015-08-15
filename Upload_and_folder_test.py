import os 
import sys
import shutil
import pyen
import time

#New folder to be created in python file directory
newpath = r'Playlists'

#To be changed in Kivy
#tempo = "Placeholder"
name = os.listdir(r"C:\Users")[1]

#destination = r"C:\Users\{0}\Documents\GitHub\Tech-Retreat-Demo\Playlists\{1}".format(name, tempo)

def create_dest(name, tempo):
    return r"C:\Users\{0}\Documents\GitHub\Tech-Retreat-Demo\Playlists\{1}".format(name, tempo)
    

#API Information
en = pyen.Pyen("PM7SRY6GGZNM4QNTG")
en.trace = False

high = []
low = []

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
def copy_file(src, tempo):
    destination = create_dest(name, tempo)
    shutil.copy(src, destination)

def wait_for_analysis(id):
    while True:
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] <> 'pending':
            break
        time.sleep(1)

    list = []

    #for k,v in response['track']['audio_summary'].items():
        #print "%32.32s %s" % (k, str(v))
    tempo_speed = response['track']['audio_summary']['tempo']

    if tempo_speed <= 108:
        low.append(id)
        low.append(tempo_speed)
        low.append(mp3)
        print low
        tempo = "Slow"
        copy_file(mp3, tempo)
    else:
        high.append(id)
        high.append(tempo_speed)
        high.append(mp3)
        print high
        tempo = "Fast"
        
        copy_file(mp3, tempo)
  
    
mp3 = r"C:\Users\{0}\Music\13 Nutritious - Dash Cancel [Ultra Street Fighter IV].mp3".format(name)
#mp3 = r"C:\Python work\tech retreat\Darude - Sandstorm.mp3"
#type = "mp3"



def main():     
    
    mainFolder(newpath)
    sub_folder(newpath, "Fast")
    sub_folder(newpath, "Slow")
    
    f = open(mp3, 'rb')
    response = en.post('track/upload', track=f, filetype='mp3')
    trid = response['track']['id']
    print 'track id is', trid
    wait_for_analysis(trid)

    
    #Loop though song list, copy all
    #copy_file("C:\Users\{0}\Music\CopyFile.txt".format(name))
    #copy_file("C:\Users\{0}\Music\TestMP3.mp3".format(name))
    #copy_file("C:\Users\{0}\Music\Blazo - Cult Classic Records Present- Friends and Family - 03 Busy Dreaming.mp3".format(name))
    #copy_file(r"C:\Users\{0}\Music\13 Nutritious - Dash Cancel [Ultra Street Fighter IV].mp3".format(name))

main()