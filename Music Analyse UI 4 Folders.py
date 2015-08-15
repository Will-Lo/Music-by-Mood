import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen

import os 
import sys
import shutil
import pyen
import time

#New folder to be created in python file directory
#newpath = r'Playlists'
#global variables containing where the file location is
mp3 = "" 

#To be changed in Kivy
#tempo = "Placeholder"
name = os.listdir(r"C:\Users")[1]

#destination = r"C:\Users\{0}\Documents\GitHub\Tech-Retreat-Demo\Playlists\{1}".format(name, tempo)

def create_dest(name, tempo):
    return ((mainFolder(mp3) + "\{0}").format(tempo))
    

#API Information
en = pyen.Pyen("PM7SRY6GGZNM4QNTG")
en.trace = False

Study = []
Workout = []
Sleep = []
Relax = []

#Creates new folder if not already existing
def mainFolder(mp3):
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
        
#Copies a given file
def copy_file(src, tempo):
    destination = create_dest(name, tempo)
    shutil.copy(src, destination)

def wait_for_analysis(id):

    while True:
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] <> 'pending':
            break
        time.sleep(0)

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
        tempo = "Studying"
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
  
    
#mp3 = r"C:\Users\{0}\Music\13 Nutritious - Dash Cancel [Ultra Street Fighter IV].mp3".format(name)
#mp3 = r"C:\Python work\tech retreat\Darude - Sandstorm.mp3"
#type = "mp3"



def run_code():     
    
    a = mainFolder(mp3)
    sub_folder(a, "Studying") #Fast+Soft
    sub_folder(a, "Workout") #Fast + Loud
    sub_folder(a, "Sleeping") #Slow + Soft
    sub_folder(a, "Relaxing") #Slow + Loud
    
    f = open(mp3, 'rb')
    response = en.post('track/upload', track=f, filetype='mp3')
    trid = response['track']['id']
    print 'track id is', trid
    wait_for_analysis(trid)

Builder.load_string("""
<PopupWindow>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Hello world'
    FileChooserListView:
        on_selection: root.selected(self.selection)
        

<HomeScreen>:
    id: my_widget
    FloatLayout:
        Label:
            text: "Sort your music based on their mood"
            font_size: 25
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}
            size_hint: 0.6,0.4
        
        Button:
            text: "Choose music file to analyse"
            on_release: root.show_popup()
            pos_hint: {'center_x': 0.5, 'center_y': 0.75}
            size_hint: 0.6,0.2
        
        Button:
            text: "Start analysing!"
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            size_hint: 0.6,0.2
            on_release: 
				root.analyse_music()
				root.manager.transition.direction = 'left'
				root.manager.current = 'results'
						

<MainWidget>:
    screen_manager: screen_manager
    ScreenManager:
        id:screen_manager
        HomeScreen:
            id:home_screen
            name: 'home'
            manager: screen_manager

<ResultsScreen>:
	FloatLayout:
		Label:
			text: "Here are your playlists"
			font_size: 25
			pos_hint: {'center_x': 0.5, 'center_y': 0.20}
			size_hint: 0.6,0.4
		
		Button:
			text: "Go Back"
			pos_hint: {'center_x': 0.2, 'center_y': 0.10}
			size_hint: 0.3,0.1
			on_release:
				root.manager.transition.direction = 'right'
				root.manager.current = 'home'
		
		Button:
			text: "Exercise Playlist"
			pos_hint: {'center_x': 0.2, 'center_y': 0.70}
			size_hint: 0.2,0.3
		
		Button:
			text: "Studying Playlist"
			pos_hint: {'center_x': 0.4, 'center_y': 0.70}
			size_hint: 0.2,0.3
		
		Button:
			text: "Sleep Playlist"
			pos_hint: {'center_x': 0.6, 'center_y': 0.70}
			size_hint: 0.2,0.3
		
		Button:
			text: "Relaxing Playlist"
			pos_hint: {'center_x': 0.8, 'center_y': 0.70}
			size_hint: 0.2,0.3
			
<MainWidget>:
	screen_manager: screen_manager
	ScreenManager:
		id:screen_manager
		HomeScreen:
			id:home_screen
			name: 'home'
			manager: screen_manager
		ResultsScreen:
			id:results_screen
			name: 'results'
			manager: screen_manager


""")

class HomeScreen(Screen):
    def show_popup(self):
        p = PopupWindow()
        p.open()
    
    def analyse_music(self):
        run_code()

        box = FloatLayout()
    
class PopupWindow(Popup):
    
    def selected(self, filename):
        print "selected: %s" % filename[0]
        global mp3
        mp3 = filename[0]
        self.dismiss(force = True)

class ResultsScreen(Screen):
	pass

class MainWidget(FloatLayout):
    manager = ObjectProperty(None)
        
class MyApp(App):
    def build(self):
        return MainWidget()

        
if __name__ == '__main__':
    MyApp().run()