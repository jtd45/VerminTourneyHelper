import tkinter as tk
from tkinter import *
import sys
import ctypes  # An included library with Python install.   

class enterTourneySize(object):
	rounds=0
	partis=0
	team=0
	def __init__(self,master):
		top=self.top=Toplevel(master)
		self.top.attributes('-topmost',1)
		rLabel=self.rL=Label(top,text="Enter # rounds")
		pLabel=self.pL=Label(top,text="Enter # teams per round (i.e. 2= x vs x, 3= x vs x vs x, etc.)")
		tLabel=self.tL=Label(top,text="Enter # vermin per team")
		rEntry=self.rEntry=Entry(top)
		pEntry=self.pEntry=Entry(top)
		tEntry=self.tEntry=Entry(top)
		rLabel.grid(row=0,column=0)
		pLabel.grid(row=1,column=0)
		tLabel.grid(row=2,column=0)
		rEntry.grid(row=0,column=1)
		pEntry.grid(row=1,column=1)
		tEntry.grid(row=2,column=1)
		rEntry.bind("<Return>",func= lambda event, a=0: self.enter(event,a))
		pEntry.bind("<Return>",func= lambda event, a=1: self.enter(event,a))
		tEntry.bind("<Return>",func= lambda event, a=2: self.enter(event,a))
		tEntry.bind("<Return>",func= lambda event, a=2: self.enter(event,a))
		rEntry.focus_force()
	
	def enter(self,event,entryID):
		try:
			self.rounds=int(self.rEntry.get())
			self.partis=int(self.pEntry.get())
			self.team=int(self.tEntry.get())
			if self.team>0 and self.partis>0 and self.rounds>0:
				self.top.destroy()
				return
			ctypes.windll.user32.MessageBoxW(0, "Missing Value", "Alert", 1)
			return
		except ValueError:
			ctypes.windll.user32.MessageBoxW(0, "Error: Not a Number", "Alert", 1)
			return

class enterStatsNamesWindow(object):
	csvString=""
	def enter(self,event):
		if(self.nameEntry.get()==""):
			self.csvString=""
			ctypes.windll.user32.MessageBoxW(0, "Missing Name", "Alert", 1)
			return
		self.csvString+=self.nameEntry.get()
		for i in range(0,5):
			self.csvString+=","+self.statEntry[i].get()
			if(self.statEntry[i].get()==""):
				self.csvString=""
				ctypes.windll.user32.MessageBoxW(0, "Missing "+self.labelStr[i], "Alert", 1)
				return
			try:
				float(self.statEntry[i].get())
				pass
			except ValueError:
				self.csvString=""
				ctypes.windll.user32.MessageBoxW(0, "Missing "+self.labelStr[i], "Alert", 1)
				return
		self.csvString+=","
		self.top.destroy()
	
	def __init__(self,master):
		top=self.top=Toplevel(master)
		self.top.attributes('-topmost',1)
		self.top.focus_force()
		self.nameLabel=Label(top,text="Name: ")
		self.nameLabel.grid(row=0,column=0)
		self.nameEntry=Entry(top)
		self.nameEntry.focus_force()
		self.nameEntry.config(takefocus="0")
		self.nameEntry.bind("<Return>",self.enter)
		self.nameEntry.grid(row=0,column=1)
		self.labelStr=["Life: ","Musl: ","Blst: ","Gurd: ","Fast: "]
		self.statLabels=dict()
		self.statEntry=dict()
		for i in range(0,5):
			self.statLabels[i]=Label(top,text=self.labelStr[i])
			self.statLabels[i].grid(row=1,column=i*2)
			self.statEntry[i]=Entry(top)
			self.statEntry[i].bind("<Return>",self.enter)
			self.statEntry[i].grid(row=1,column=i*2+1)
	