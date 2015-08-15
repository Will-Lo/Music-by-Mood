import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup

import os

Builder.load_string("""
<PopupWindow>:
	size_hint: .5, .5
	auto_dismiss: False
	title: 'Hello world'
	FileChooserListView:
		id: filechooser
		on_selection: my_widget.selected(filechooser.selection)

<MyWidget>:
	id: my_widget
	Button:
		text: "open"
		on_release: my_widget.open(filechooser.path, filechooser.selection)
	Button:
		text: "choose music file to analyse"
		on_release: root.show_popup()
""")

class MyWidget(BoxLayout):
	def open(self, path, filename):
		with open(os.path.join(path, filename[0])) as f:
			print f.read()

	def selected(self, filename):
		print "selected: %s" % filename[0]
	
	def show_popup(self):
		p = PopupWindow()
		p.open()


		
class PopupWindow(Popup):
	pass

class MyApp(App):
	def build(self):
		return MyWidget()

if __name__ == '__main__':
	MyApp().run()