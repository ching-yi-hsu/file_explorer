from os import listdir
import os 
import tkinter as tk
from file_print import file_print

def get_inside_dir_command(file_path):
    return lambda: tk_window(file_path)

def get_inside_file_command(file_name, file_path):
    return lambda: file_print(file_name, file_path)

def show_on_same_window(window, new_file_path):
    window.destroy()
    tk_window(new_file_path)
    

def tk_window(mypath):  
    window = tk.Tk()
    window.title('File Explore')
    window.geometry('600x500')
    file_frames = []
    file_label = []
    file_boutton = []
    files = os.listdir(mypath)

    for f in files:
        file_frame = tk.Frame(window,height=5,bd = 5 ,background = "pink")
        file_frames.append(file_frame)
        
        
        if not os.path.isdir(f):
            command = get_inside_file_command(f, mypath)
            file_boutton = tk.Button(file_frame, text = "Get Inside", command = command  )
            file_boutton.pack(side = "right")
            file_label = tk.Label(file_frame, text = f )
            file_label.pack(side = "left")
        else:
            file_path = f"{mypath}\{f}" 
            command = get_inside_dir_command(file_path)

            file_boutton = tk.Button(file_frame, text = "Get Inside", command = command)
            file_boutton.pack(side = "right")

            command = lambda file_path = file_path : show_on_same_window(window,file_path)
            file_samewidow_boutton = tk.Button(file_frame, text = "show on same window", command = command)
            file_samewidow_boutton.pack(side = "right")
            file_label = tk.Label(file_frame, text = f, background = "green")
            file_label.pack(side = "left")
        file_frame.pack(fill="x", padx=5, pady=5)
    
    window.mainloop()

    if __name__ == "__main__":
        pass