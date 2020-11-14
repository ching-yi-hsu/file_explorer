from os import listdir
import os
import tkinter as tk
import file_print

def tk_window():
    window = tk.Tk()
    window.title('File Explore')
    window.geometry('600x500')
    mypath = os.getcwd()
    files = listdir(mypath)
    file_fram = []
    file_label = []
    file_boutton = []

    for f in files:
        file_fram= tk.Frame(window,height=5,bd = 5 ,background = "pink")
        f_sp = f.split(".")
        if len(f_sp) == 2 :
            file_boutton = tk.Button(file_fram, text = "entery", command = lambda f = f, f_sp = f_sp:file_print.file_print(f,f_sp) )
            file_boutton.pack(side = "right")
            file_label = tk.Label(file_fram, text = f )
            file_label.pack(side = "left")
        else:
            file_boutton = tk.Button(file_fram, text = "entery", command = lambda f = f, f_sp = f_sp:file_print.file_print(f,f_sp) )
            file_boutton.pack(side = "right")
            file_label = tk.Label(file_fram, text = f, background = "green")
            file_label.pack(side = "left")
        file_fram.pack(fill="x", padx=5, pady=5)
    window.mainloop()
    
if __name__ == "__main__":
    tk_window()
