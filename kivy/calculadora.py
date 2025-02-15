import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout) :

	#Function called when the equals is pressed
	def calculate(self,calculation) :
		if calculation:
			try:
				# Solve formula and display it in entry
				# which is pointed at by display
				self.display.text = str(eval(calculation))
			except Exception:
				self.display.text = "Error"

class CalculatorApp(App) :
	def build(self) :
		return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()
