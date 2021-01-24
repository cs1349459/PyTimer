try:
    from tkinter import *
    import tkinter.font as font
except:
    from Tkinter import *
    import tkFont as font
import threading
import math
from time import time, sleep
from sys import exit

def startimer():
    global timer;global start;global spinner;global label;global tk
    timer = 0
    delay = int(spinner.get())
    startime = time()
    start.pack_forget()
    spinner.pack_forget()
    label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    while True:
        try:
            timer = (time()-startime) - delay
            sleep(0.015)
            if timer >= 0:
                strtime = str(math.floor(timer/3600)) + " : " + str(math.floor(timer/60)%60).zfill(2) + " : " + str(round(timer)%60).zfill(2) + "." + (str(round(timer%1, 2)).split(".")[1])
            else:
                strtime = "- " + str(math.floor(-timer/3600)) + " : " + str(math.floor(-timer/60)%60).zfill(2) + " : " + str(round(-timer)%60).zfill(2) + "." + (str(round(-timer%1, 2)).split(".")[1])
            label.config(text = strtime)
            tk.update()
        except Exception as e:
            print(e)
            try:
                tk.destroy()
                exit()
            except:
                exit()
        

timer = None
tk = Tk()
tk.title("PyTimer")
tk.geometry("200x50")
tk.resizable(0, 0)
tk.wm_attributes
start = Button(tk, text = "Start timer in x seconds", command = startimer)
start.place(relx = 0, rely = 0, relwidth = 0.8, relheight = 1)
spinner = Spinbox(tk, from_ = 1, to_ = 60)
spinner.place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 1)
label = Label(tk, bg = "#fff", fg = "#000", font = font.Font(family = "Helvetica", size = 20), anchor = "w")

