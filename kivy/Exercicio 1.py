from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Exerciocio1App(App):
	def build(self):
		box = FloatLayout()
		button = Button(text= "Adicionar", size_hint= (.15, .06), pos_hint={"x":.1, "y":.4}, on_release= self.mudar)
		label = Label(text= "LISTA", font_size= 40, size_hint= (.15, .06), pos_hint={"x":.1,"y":.7})
		self.textinput = TextInput(hint_text= "Insira um Texto", font_size= 20, size_hint= (.25, .06), pos_hint={"x":.05,"y":.55})
		self.texto = Label(text= "", font_size= 15, size_hint= (.15, .06), pos_hint={"x":.6,"y":.7})
		box.add_widget(button)
		box.add_widget(label)
		box.add_widget(self.textinput)
		box.add_widget(self.texto)
		return box

	def mudar(self, texto):
		self.texto.text = self.textinput.text
		self.textinput.text = ""


Exerciocio1App().run()