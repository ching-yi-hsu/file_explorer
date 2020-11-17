from os import listdir
import os 
import tkinter as tk
from TK_call_window import tk_window



if __name__ == "__main__":
    mypath = os.getcwd()
    tk_window(mypath)
