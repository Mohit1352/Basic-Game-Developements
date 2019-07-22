import tkinter as tk
questnow=0
seqnow=[0]
toStop=0
optval1=0
optval2=0

def destroyer(window,func):
    window.destroy()
    func()

def ingamemenu(gamewindow):
    igwindow=tk.Tk()
    igwindow.wm_title("In Game Menu")
    igwindow.iconbitmap("icon.ico")
    igwindow.geometry("300x175+500+200")
    igwindow.config(bg="red")
    igwindow.resizable(10,10)
    igmes=tk.Message(igwindow,text="In Game Menu")
    igmes.config(bg="red",font=('Arial'))
    igmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
    savequit=tk.Button(igwindow,
                       text="Save and Menu",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(gamewindow,lambda:destroyer(igwindow,saveandgo)))
    savequit.config(width=30)
    savequit.pack(padx=5,pady=10)
    menu=tk.Button(igwindow,
                       text="Menu",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(gamewindow,lambda:destroyer(igwindow,go)))
    menu.config(width=30)
    menu.pack(padx=5,pady=10)
    

def go():
    global toStop
    toStop=1
    gameset(questnow,seqnow)
    
def reinit():
    global toStop
    toStop=0

def opt1():
    global questnow
    global seqnow
    questnow=optval1
    seqnow.append(optval1)
    gameset(questnow,seqnow)

def opt2():
    global questnow
    global seqnow
    questnow=optval2
    seqnow.append(optval2)
    gameset(questnow,seqnow)

def saveandgo():
    global questnow
    global seqnow
    global toStop
    toStop=1
    file=open("gamesave.txt","w")
    file.write(str(questnow)+"\n")
    file.write(str(seqnow))
    file.close()
    gameset(questnow,seqnow)

def gameplay():
    story=[{"Hi. Do we start?":{"Y":1,"N":2}},
           {"Good choice. Is this a test?":{"Ya":3,"Na":4}},
           {"Why? Not ready yet?":{"Yo":5,"No":6}},
           {"A test for what? NUKE?":{"N":6,"Y":5}},
           {"Ah I got Scared.":{"Why":5,"What":6}},
           {"This was a nuke test.":{"I was right!":6,"Hell yeah!":6}},
           {"Congrats, you beat the game and came to the end. Please save and quit.":{"Please":6,"Save":6}}]
    global questnow
    global seqnow
    global optval1
    global optval2
    gamewindow=tk.Tk()
    gamewindow.wm_title("NUKEBLITZ - Play in progress....")
    gamewindow.iconbitmap("icon.ico")    
    gamewindow.geometry("450x250+400+200")
    gamewindow.config(bg="lightblue")
    gamewindow.resizable(10,10)
    quesdict=story[questnow]
    quescont=[i for i in quesdict][0]
    questext=tk.Message(gamewindow,
                        text=quescont,
                        bg="lightblue")
    questext.config(width=500)
    questext.pack(side=tk.TOP,anchor="center",padx=5,pady=5)
    optdict=quesdict[quescont]
    options=[i for i in optdict]
    optval1=optdict[options[0]]
    optval2=optdict[options[1]]
    button1=tk.Button(gamewindow,
                     text=options[0],
                     fg="blue",
                     bg="lightgreen",
                     command=lambda:destroyer(gamewindow,opt1))
    button1.config(width=30)
    button1.pack(padx=15,pady=15,anchor="center")
    button2=tk.Button(gamewindow,
                     text=options[1],
                     fg="blue",
                     bg="lightgreen",
                     command=lambda:destroyer(gamewindow,opt2))
    button2.config(width=30)
    button2.pack(padx=10,pady=5,anchor="center")
    menubutton=tk.Button(gamewindow,
                         text="MENU",
                         fg="red",
                         bg="yellow",
                         command=lambda:ingamemenu(gamewindow))
    menubutton.config(width=30)
    menubutton.pack(padx=10,pady=30)

def gameset(a,b):
    global questnow
    global seqnow
    questnow=a
    seqnow=b
    if not toStop:
        gameplay()

def newgameopt():
    reinit()
    gameset(0,[0])

def loadgameopt():
    try:
        reinit()
        file=open("gamesave.txt")
        qno=file.readline()
        seq=file.readline()
        seq.replace('[',']')
        seq.replace(']','')
        seqlist=seq.split(',')
        file.close()
        if (qno==None) and (seqlist==[]):
            import os
            os.remove("gamesave.txt")
            loadgameopt()
        gameset(int(qno),seqlist)
    except FileNotFoundError:
        nof=tk.Tk()
        nof.wm_title("Sorry!")
        nof.iconbitmap("icon.ico")
        nof.geometry("225x125+513+231")
        nofmes=tk.Message(nof,text="No save file found.")
        nofmes.config(font=('Arial'))
        nofmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
        ok=tk.Button(nof,
                     text="OKAY",
                     command=nof.destroy)
        ok.config(width=10)
        ok.pack(pady=10,anchor="center")

def exitconf():
    exwindow=tk.Tk()
    exwindow.wm_title("Exit NUKEBLITZ?")
    exwindow.iconbitmap("icon.ico")
    exwindow.geometry("225x125+513+231")
    exwindow.config(bg="yellow")
    exwindow.resizable(10,10)
    exmes=tk.Message(exwindow,text="Are you sure?")
    exmes.config(bg="yellow",font=('Arial'))
    exmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
    yes=tk.Button(exwindow,
                  text="YES",
                  fg="yellow",
                  bg="red",
                  command=quit)
    yes.config(width=10)
    yes.pack(side=tk.LEFT,padx=20,pady=20,anchor="center")
    no=tk.Button(exwindow,
                  text="NO",
                  fg="yellow",
                  bg="green",
                  command=exwindow.destroy)
    no.config(width=10)
    no.pack(side=tk.LEFT,padx=10,pady=20,anchor="center")
    
def loadopt():
    mm.destroy()
    choicewid=tk.Tk()
    choicewid.wm_title("NUKEBLITZ - The Game")
    choicewid.iconbitmap("icon.ico")
    choicewid.geometry("450x250+400+200")
    choicewid.config(bg="green")
    opt=['New Game','Load Game','Back']
    comm=[newgameopt,loadgameopt,choicewid.destroy]
    for i in opt:
        buttons=tk.Button(choicewid,
                          text=i,
                          fg="green",
                          bg="orange",
                          command=comm[opt.index(i)])
        buttons.config(width=20)
        buttons.pack(side=tk.LEFT,padx=20,pady=30,anchor="center")

while True:
    mm = tk.Tk()
    mm.wm_title("NUKEBLITZ - The Game")
    mm.iconbitmap("icon.ico")
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
                       command=loadopt)
    startgame.config(width=20)
    startgame.pack(side=tk.LEFT,padx=50,pady=20,anchor="center")
    endgame = tk.Button(mm, 
                       text="End Game", 
                       fg="red",
                       bg="yellow",
                       command=exitconf)
    endgame.config(width=20)
    endgame.pack(side=tk.LEFT,padx=10,pady=20,anchor="center")
    mm.mainloop()
