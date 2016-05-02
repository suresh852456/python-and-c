#!/usr/bin/python
"""
This file is used to create the UI for Network creation 
"""
import selfNetwork as sn
import Tkinter
class main_window(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
	def initialize(self):
		self.grid()
		self.entry=Tkinter.Entry(self)
		self.entry.grid(column=0,row=3,sticky='EW')
		button=Tkinter.Button(self,text=u"Submit")
		button.grid(column=0,row=4,sticky='NW')
		label=Tkinter.Label(self,anchor='w',fg='Black',bg='Navyblue')
		label.grid(column=0,row=5,columnspan=2,sticky='EW')
		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,True)
def main():
	main_app=main_window(None)	
	main_app.title("Self Learning Network")	
	main_app.mainloop()
if __name__=="__main__":
	main()

