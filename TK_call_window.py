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
    

def create_path_search(window):
    path_text = tk.StringVar()
    command = lambda x = path_text: sucking_time_fucker(x)
    path_text_frame = tk.Frame(window)
    tk.Entry(path_text_frame, textvariable=path_text).pack(side="left")
    tk.Button(path_text_frame, text="open legs", command=command).pack(side="right")
    path_text_frame.pack()
    return path_text


def sucking_time_fucker(path_text):
    print(path_text.get())
    path_text.set("suck my dick")


def tk_window(my_path):
    window = tk.Tk()
    window.title('File Explore')
    window.geometry('600x500')
    file_frames = []
    file_label = []
    file_boutton = []
    files = os.listdir(my_path)
    search_text = create_path_search(window)
    search_text.set(my_path)
    
    
    

    for f in files:
        file_frame = tk.Frame(window,height=5,bd = 5 ,background = "pink")
        file_frames.append(file_frame)
        
        
        if not os.path.isdir(f):
            command = get_inside_file_command(f, my_path)
            file_boutton = tk.Button(file_frame, text = "Get Inside", command = command  )
            file_boutton.pack(side = "right")
            file_label = tk.Label(file_frame, text = f )
            file_label.pack(side = "left")
        else:
            file_path = f"{my_path}\{f}" 
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