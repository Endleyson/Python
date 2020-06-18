import kivy
from kivy.app import App
from kivy.lang import Builder

code = """
FloatLayout:
	Button: 
		text: "<<<"
		size_hint: .2, .1
	    pos_hint: {"x": .2, "y": .7}
	    on_release: label.text = str(int(label.text)-1)

	Button: 
		text: ">>>"
		size_hint: .2, .1
	    pos_hint: {"x": .6, "y": .7}
	    on_release: label.text = str(int(label.text)+1)

	Label:
		id: label
		text: "0"
		font_size: 200
		size_hint: .2, .1
	    pos_hint: {"x": .4, "y": .32}
"""

class Exerciocio3App(App):
	def build(self):
		return Builder.load_string(code)

Exerciocio3App().run()