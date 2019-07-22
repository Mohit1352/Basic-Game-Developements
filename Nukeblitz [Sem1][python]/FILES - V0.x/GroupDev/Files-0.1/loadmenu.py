import tkinter as tk
from gamemodes import *
def loadopt():
    choicewid=tk.Tk()
    choicewid.geometry("450x250+400+200")
    choicewid.config(bg="green")
    opt=['New Game','Load Game','Back']
    comm=[ng,lg,choicewid.destroy]
    for i in opt:
        buttons=tk.Button(choicewid,
                          text=i,
                          fg="green",
                          bg="orange",
                          command=comm[opt.index(i)])
        buttons.config(width=20)
        buttons.pack(side=tk.LEFT,padx=20,pady=30,anchor="center")

