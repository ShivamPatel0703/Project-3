from time import *
from tkinter import *
root = Tk() #Creating Root Widget here
root.title("Digital Clock") #Name of the Clock GUI
def clockTime(): # time function that includes GUI String for the Clock to be diplayed
    clockString = strftime("%H:%M:%S:%p")
    clockLabel.config(text = clockString)
    clockLabel.after(100,clockTime) #Calls back functiomn, uses ms (100 in this case till it calls function)
clockLabel = Label(root, font = ("Terminal", 100), background = "white", foreground = "blue") #Features of the clock
clockLabel.pack(anchor = "center")
clockTime()
mainloop()

