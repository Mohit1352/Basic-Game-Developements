import tkinter as tk
root=tk.Tk()
frame1=tk.Frame(root,
                bg="white")
frame2=tk.Frame(root,
                bg="black")
frame1.pack()
frame2.pack()
frame1.pack()
frame2.pack()
for i in range(0,100):
    if i%5==0:
        if frame1.bg=="white":
            frame1.config(bg="black")
        else:
            frame1.config(bg="white")
        if frame2.bg=="white":
            frame2.config(bgc="black")
        else:
            frame1.config(bg="white")
print("Done")
