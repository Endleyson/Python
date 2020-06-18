import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sqlite3
import time

class Gerenciador(ScreenManager):
	pass

class Login(Screen):

	def login_window():
		Config.set('graphics', 'width', '300')
		Config.set('graphics', 'height', '350')
		Config.set('graphics', 'resizable', False)
		Config.set('graphics', 'borderless', '1')

	login_window()

	def analisar_dados(self, name, password):

		if name == "sobrasvr" and password == "Sys11190p":
			self.ids.analisador.text = "...conectado..."

		elif name == "":
			return

		elif password == "":
			return

		else:
			return


class Controle(Screen):

	def ler(self, disp):
		conn = sqlite3.connect('dbanaliser.db')

		cursor = conn.cursor()

		cursor.execute("""
		SELECT * FROM mapas
		WHERE dispositivo = ?
		""", (disp,))
			
		for linha in cursor.fetchall():
			print("Mapa:", linha[1])
			self.ids.imprime.text = linha[1]

class execute(App):
	def build(self):
		Config.set('graphics', 'width', '800')
		Config.set('graphics', 'height', '600')
		Config.set('graphics', 'resizable', False)
		return Gerenciador()

if __name__ == '__main__':
	execute().run()