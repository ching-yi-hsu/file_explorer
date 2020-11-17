from os import listdir
import os 
import tkinter as tk
import TK_call_window
def file_print(f,mypath):
    file_path = mypath + '\\' + f  
    with open(file_path,"r") as file :
        app = tk.Tk()
        label_text = tk.Label(app,text = file.read() )
        label_text.pack()
if __name__ == "__main__":
    pass