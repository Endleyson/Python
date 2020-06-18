from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Main(App):
    def build(self):
        return Incrementador()
Main().run()