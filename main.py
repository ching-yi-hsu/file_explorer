from os import listdir
import os 
import tkinter as tk
from TK_call_window import tk_window


if __name__ == "__main__":
    my_path = os.getcwd()
    tk_window(my_path)
