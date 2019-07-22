import tkinter as tk
import loadmenu
import exitconf
def main():
    mm = tk.Tk()
    mm.geometry("450x250+400+200")
    mm.config(bg="red")
    mm.resizable(10,10)
    name1 = "NUKE"
    name2="-"
    name3="BLITZ"
    n1 = tk.Message(mm, text = name1)
    n1.config(bg='red', font=('Arial', 20, 'bold'))
    n1.pack(side=tk.TOP,fill=tk.BOTH,pady=10)
    n2 = tk.Message(mm, text = name2)
    n2.config(bg='red', font=('Arial', 20, 'bold'))
    n2.pack(side=tk.TOP,fill=tk.BOTH)
    n3 = tk.Message(mm, text = name3)
    n3.config(bg='red', font=('Arial', 20, 'bold'))
    n3.pack(side=tk.TOP,fill=tk.BOTH)
    startgame = tk.Button(mm, 
                       text="Start Game", 
                       fg="green",
                       bg="yellow",
                       command=loadmenu.loadopt)
    startgame.config(width=20)
    startgame.pack(side=tk.LEFT,padx=50,pady=20,anchor="center")
    endgame = tk.Button(mm, 
                       text="End Game", 
                       fg="red",
                       bg="yellow",
                       command=exitconf.exitconf)
    endgame.config(width=20)
    endgame.pack(side=tk.LEFT,padx=10,pady=20,anchor="center")
    tk.mainloop()
main()
