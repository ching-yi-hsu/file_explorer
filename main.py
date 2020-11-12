from os import listdir
import os
import tkinter as tk



window = tk.Tk()
window.title('File Explore')
window.geometry('500x300')
mypath = os.getcwd()
files = listdir(mypath)
file_fram = []
file_label = []
file_boutton = []
n  = 0


for f in files:
    
    file_fram= tk.Frame(window,height=5,bd = 5 ,background = "pink")
    file_label = tk.Label(file_fram, text = f)
    
    file_boutton = tk.Button(file_fram, text = "entery", command = lambda name = f:print(name) )
    file_boutton.pack(side = "right")
    file_label.pack(side = "left")
    file_fram.pack(fill="x", padx=5, pady=5)
  
    
    #file_labels.appen(file_label)
    
window.mainloop()

