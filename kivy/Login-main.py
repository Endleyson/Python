import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Gerenciador(ScreenManager):
	pass
	
class Logar(Screen):
    pass

class Create_Account(Screen): 
    pass

class Login(App):
	def build(self):
		return Gerenciador()

Login().run()


