import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty


import os

Builder.load_string("""
<PopupWindow>:
	size_hint: .5, .5
	auto_dismiss: False
	title: 'Hello world'
	FileChooserListView:
		on_selection: root.selected(self.selection)
		

<MyWidget>:
	id: my_widget
	Label:
		text: "Sort your music based on their mood"
		font_size: 25
		pos_hint: {'center_x': 0.5, 'center_y': 0.85}
		size_hint: 0.6,0.4
	
	
	Button:
		text: "choose music file to analyse"
		on_release: root.show_popup()
		pos_hint: {'center_x': 0.5, 'center_y': 0.35}
		size_hint: 0.6,0.2

<HomeScreen>:
	BoxLayout:
		MyWidget
""")
#global variables containing where the file location is
file_location = "" 



class MyWidget(FloatLayout):
	
	def show_popup(self):
		p = PopupWindow()
		p.open()

class HomeScreen(Screen):
	pass
box = FloatLayout()
	
class PopupWindow(Popup):
	
	def selected(self, filename):
		print "selected: %s" % filename[0]
		global file_location 
		file_location = filename[0]
		self.dismiss(force = True)
		

class MyApp(App):
	def build(self):
		return HomeScreen()

		
if __name__ == '__main__':
	MyApp().run()