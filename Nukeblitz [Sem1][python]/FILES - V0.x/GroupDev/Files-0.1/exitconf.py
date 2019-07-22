import tkinter as tk
def exitconf():
    exitwid=tk.Tk()
    exitwid.config(bg="yellow")
    exitwid.geometry("450x250+400+200")
    confmsg="Do you want to exit?\nAll unsaved progress may be lost."
    conf=tk.Message(exitwid,text=confmsg)
    conf.config(bg="yellow",fg="darkblue",font=("Arial",10),width=100,pady=10)
    conf.pack(side=tk.TOP,anchor="center")
    qb=tk.Button(exitwid,
                 text="YES",
                 fg="yellow",
                 bg="red",
                 command=quit)
    qb.config(width=20)
    qb.pack(side=tk.LEFT,padx=50,pady=20,anchor="center")
    cancel=tk.Button(exitwid,
                 text="NO",
                 fg="yellow",
                 bg="green",
                 command=exitwid.destroy)
    cancel.config(width=20)
    cancel.pack(side=tk.LEFT,padx=20,pady=20,anchor="center")
    
