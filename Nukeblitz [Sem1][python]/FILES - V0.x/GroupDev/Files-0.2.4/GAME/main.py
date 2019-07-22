import clearemptysav as ces
import tkinter as tk
import nloadnsave as  nlns
import os
import sys
questnow=0
seqnow=[0]
toStop=0
optval1=0
optval2=0
soundv=True
togs=False
currfile="Unsaved"
temp=None
newsave=False
sys.path.insert(0,str(os.path.realpath("..")+"\\SOUND"))
sys.path.insert(2,str(os.path.realpath("..")+"\\SAV"))

def passas(val):
    global temp
    temp=val

def storeas(func):
    global temp
    temp=func()
    

def hideCons(win):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),6)
    #win.wm_state("iconic")
    #win.wm_state("zoomed")
    win.wm_state("normal")

def reload(window1,window2):
    window1.destroy()
    window2.destroy()

def sound():
    if soundv:
        mus=open(os.path.realpath("..")+"\\SOUND\\theme.wav")
        import winsound as ws
        ws.PlaySound(mus.name,ws.SND_ALIAS|ws.SND_NODEFAULT|ws.SND_ASYNC|ws.SND_LOOP)
        mus.close()
        """
        import soundplay
        soundplay.soundplay()
        """
        """
        import winsound as ws
        ws.PlaySound("theme.wav",ws.SND_ALIAS|ws.SND_NODEFAULT|ws.SND_ASYNC|ws.SND_LOOP)
        """
    else:
        import winsound as ws
        ws.PlaySound(None,ws.SND_ALIAS|ws.SND_NODEFAULT|ws.SND_ASYNC|ws.SND_PURGE)


def soundtog():
    global soundv
    global togs
    if soundv:
        soundv=False
    else:
        soundv=True
    togs=True
    homeopt()
def killlist():
    try:
        files=[i.replace(".nbsf","") for i in os.listdir(os.path.realpath("..")+"\\SAV") if ".nbsf" in i]
        if files==[]:
            raise FileNotFoundError
        else:
            dc=tk.Tk()
            dc.wm_title("Delete Game - NUKEBLITZ - The Game")
            dc.geometry("300x{h}+500+200".format(h=str(45+len(files)*50)))
            dc.config(bg="yellow")
            dc.iconbitmap("icon.ico")
            dlab=tk.Label(dc,text="Choose save file...",height=4,bg="yellow")
            dlab.pack()
            file=""
            for i in files:
                delo=tk.Button(dc,
                                text=i,
                                fg="yellow",
                                bg="blue",
                                command=lambda:killsav(i,dc))
                delo.config(width=50,height=2)
                delo.pack()
    except FileNotFoundError:
        delf=tk.Tk()
        delf.wm_title("No file deleted.!")
        delf.iconbitmap("icon.ico")
        delf.geometry("225x125+513+231")
        delfmes=tk.Message(delf,text="No file loaded.")
        delfmes.config(font=('Arial'))
        delfmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
        ok=tk.Button(delf,
                     text="OKAY",
                     command=delf.destroy)
        ok.config(width=10)
        ok.pack(pady=10,anchor="center")
        
def killsav(file,dc=tk.Tk):
    try:
        dc.destroy()
        os.remove(os.path.realpath("..")+"\\SAV"+"\\{file}.nbsf".format(file=file))
        delf=tk.Tk()
        delf.wm_title("{file} deleted!".format(file=file))
        delf.iconbitmap("icon.ico")
        delf.geometry("225x125+513+231")
        delfmes=tk.Message(delf,text="{file} deleted!".format(file=file))
        delfmes.config(font=('Arial'))
        delfmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
        ok=tk.Button(delf,
                     text="OKAY",
                     command=lambda:destroyer(delf,killlist))
        ok.config(width=10)
        ok.pack(pady=10,anchor="center")
    except FileNotFoundError:
        delf=tk.Tk()
        delf.wm_title("No file deleted.!")
        delf.iconbitmap("icon.ico")
        delf.geometry("225x125+513+231")
        delfmes=tk.Message(delf,text="No files found.")
        delfmes.config(font=('Arial'))
        delfmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
        ok=tk.Button(delf,
                     text="OKAY",
                     command=delf.destroy)
        ok.config(width=10)
        ok.pack(pady=10,anchor="center")

def homeopt():
    global soundv
    col=""
    if soundv:
        col="green"
    else:
        col="red"
    homeop=tk.Tk()
    homeop.wm_title("Game Options")
    homeop.iconbitmap("icon.ico")
    homeop.geometry("300x300+500+200")
    homeop.config(bg="yellow")
    homeop.resizable(10,10)
    lab1=tk.Label(homeop,text="Sound Settings:",bg="yellow")
    lab1.pack()
    togsound=tk.Button(homeop,
                       text=str("Sound="+str(soundv)),
                       bg=col,
                       fg="yellow",
                       command=lambda:destroyer(homeop,soundtog))
    togsound.config(width=30)
    togsound.pack(padx=5,pady=10)
    back=tk.Button(homeop,
                   text="Save Changes",
                   bg="purple",
                   fg="yellow",
                   command=lambda:reload(homeop,mm))
    back.config(width=30)
    back.pack(padx=5,pady=10)
    lab2=tk.Label(homeop,text="",bg="yellow")
    lab2.pack()
    lab3=tk.Label(homeop,text="Misc Settings:",bg="yellow")
    lab3.pack()
    killsave=tk.Button(homeop,
                       text="Delete Save File",
                       bg="red",
                       fg="yellow",
                       command=killlist)
    killsave.config(width=30)
    killsave.pack(padx=5,pady=10)

def destroyer(window,func):
    window.destroy()
    func()

def changename(window):
    global newsave
    if newsave:
        newsave=False
        window.destroy()
        gameplay()
    
def ingamemenu(gamewindow):
    igwindow=tk.Tk()
    igwindow.wm_title("In Game Menu")
    igwindow.iconbitmap("icon.ico")
    igwindow.geometry("300x350+500+200")
    igwindow.config(bg="red")
    igwindow.resizable(10,10)
    igmes=tk.Message(igwindow,text="In Game Menu")
    igmes.config(bg="red",font=('Arial'))
    igmes.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
    saveo=tk.Button(igwindow,
                       text="Save",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(igwindow,save))
    saveo.config(width=30)
    saveo.pack(padx=5,pady=10)
    savequit=tk.Button(igwindow,
                       text="Save and Menu",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(gamewindow,lambda:destroyer(igwindow,saveandgo)))
    savequit.config(width=30)
    savequit.pack(padx=5,pady=10)
    saveaso=tk.Button(igwindow,
                       text="Save As",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(igwindow,saveas))
    saveaso.config(width=30)
    saveaso.pack(padx=5,pady=10)
    saveasquit=tk.Button(igwindow,
                       text="Save As and Menu",
                       bg="yellow",
                       fg="red",
                       command=lambda:destroyer(gamewindow,lambda:destroyer(igwindow,saveasandgo)))
    saveasquit.config(width=30)
    saveasquit.pack(padx=5,pady=10)
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

def saveas():
    global newsave
    newsave=True
    global currfile
    try:
        def filenameinput(window,e,s=""):
            global currfile
            s=e.get()
            currfile=s
            print(currfile,s,e)
            fwithn=[i.replace(".nbsf","") for i in os.listdir(os.path.realpath("..")+"\\SAV") if (currfile in i and ".nbsf" in i)]
            fwnl=len(fwithn)
            print(fwithn,fwnl)
            s1=""
            if s+".nbsf" in os.listdir(os.path.realpath("..")+"\\SAV"):
                s1=s+"_{n}".format(n=fwnl)
                currfile=s1
            global questnow
            global seqnow
            nlns.nsave(str(questnow),str(seqnow),currfile)
            window.destroy()
        sawindow=tk.Tk()
        sawindow.wm_title("Save as:")
        sawindow.iconbitmap("icon.ico")
        sawindow.geometry("300x175+500+200")
        sawindow.config(bg="red")
        sawindow.resizable(10,10)
        sames=tk.Message(sawindow,text="Save file name:")
        sames.config(bg="red",font=('Arial'))
        sames.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=10)
        v = tk.StringVar()
        v.set("Enter file name")
        e = tk.Entry(sawindow, textvariable=v)
        f=lambda:filenameinput(sawindow,e)
        e.bind("<Return>",lambda x:f())
        e.pack()
        okb=tk.Button(sawindow,
                      text="Okay",
                      command=f,
                      width=50)
        okb.pack()
    except Exception:
        pass
        """
        submit=tk.Button(sawindow,
                         text="Save",
                         command=storeas(v.get()))
        """
        """
        if s+".nbsf" in os.listdir():
            namewin=tk.Tk()
            namewin.wm_title("Save already exists! - NUKEBLITZ")
            namewin.iconbitmap("icon.ico")
            namewin.geometry("225x125+513+231")
            exmes=tk.Message(text="Save file of the name \"{s}\" already exists.".format(s=s))
            exist=tk.Button(namewin,
                            text="Okay",
                            command=namewin.destroy)
        else:
            global questnow
            global seqnow
            global currfile
            currfile=s
            nlns.nsave(str(questnow),str(seqnow),currfile)
            sawindow.destroy()
        """

def save():
    global questnow
    global seqnow
    global currfile
    if(currfile!="Unsaved"):
        nlns.nsave(str(questnow),str(seqnow),currfile)
    else:
        saveas()

def saveandgo():
    global questnow
    global seqnow
    global toStop
    toStop=1
    save()
    gameset(questnow,seqnow)

def saveasandgo():    
    global questnow
    global seqnow
    global toStop
    toStop=1
    saveas()
    gameset(questnow,seqnow)

def gameplay():
    try:
        story=[{"Hi. Do we start?":{"Y":1,"N":2}},
               {"Good choice. Is this a test?":{"Ya":3,"Na":4}},
               {"Why? Not ready yet?":{"Yo":5,"No":6}},
               {"A test for what? NUKE?":{"N":6,"Y":5}},
               {"Ah I got Scared.":{"Why":5,"What":6}},
               {"This was a nuke test.":{"I was right!":6,"Hell yeah!":6}},
               {"Congrats, you beat the game and came to the end. Please save and quit.":{".":6,"..":6}}]
        global questnow
        global seqnow
        global optval1
        global optval2
        global currfile
        gamewindow=tk.Tk()
        gamewindow.wm_title("{currfile} - NUKEBLITZ".format(currfile=currfile))
        gamewindow.iconbitmap("icon.ico")    
        gamewindow.geometry("450x250+400+200")
        gamewindow.config(bg="lightblue")
        gamewindow.resizable(10,10)
        changename(gamewindow)
        quesdict=story[questnow]
        quescont=[i for i in quesdict][0]
        questext=tk.Message(gamewindow,
                            text=quescont,
                            bg="lightblue")
        questext.config(width=500)
        questext.pack(side=tk.TOP,anchor="center",padx=5,pady=5)
        optdict=quesdict[quescont]
        options=[i for i in optdict]
        print(options)
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
    except Exception:
        pass

def gameset(a,b):
    global questnow
    global seqnow
    questnow=a
    seqnow=b
    if not toStop:
        gameplay()

def newgameopt():
    reinit()
    global currfile
    currfile="Unsaved"
    gameset(0,[0])

def l(file,window):
    qno,seq=nlns.nload(file)
    global currfile    
    if currfile=="Unsaved":
        currfile=file
    seq.replace('[',']')
    seq.replace(']','')
    seqlist=seq.split(',')
    window.destroy()
    if (qno==None) and (seqlist==[]):
        os.remove("{file}.nbsf".format(file=file))
        loadgameopt()
    gameset(int(qno),seqlist)

def loadgameopt():
    
    ces.findclear()
    try:
        files=[i.replace(".nbsf","") for i in os.listdir(os.path.realpath("..")+"\\SAV") if ".nbsf" in i]
        print(files)
        if files==[]:
            raise FileNotFoundError
        else:
            loadc=tk.Tk()
            loadc.wm_title("Load Game - NUKEBLITZ - The Game")
            loadc.geometry("300x{h}+500+200".format(h=str(45+len(files)*50)))
            loadc.config(bg="yellow")
            loadc.iconbitmap("icon.ico")
            loadlab=tk.Label(loadc,text="Choose save file...",height=4,bg="yellow")
            loadlab.pack()
            file=""
            for i in files:
                loado=tk.Button(loadc,
                                text=i,
                                fg="yellow",
                                bg="blue",
                                command=lambda:l(i,loadc))
                loado.config(width=50,height=2)
                loado.pack()
            reinit()
            
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
    import ctypes
    sound()
    mm = tk.Tk()
    mm.wm_title("NUKEBLITZ - The Game")
    mm.iconbitmap("icon.ico")
    mm.geometry("450x250+400+200")
    mm.config(bg="red")
    mm.resizable(10,10)
    name1 = "NUKE"
    name2="BLITZ"
    name3=""
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
    startgame.pack(pady=5,anchor="center")#side=tk.LEFT,padx=30,pady=20,
    options= tk.Button(mm, 
                       text="Options", 
                       fg="purple",
                       bg="yellow",
                       command=homeopt)
    options.config(width=20)
    options.pack(pady=5,anchor="center")#side=tk.LEFT,padx=10,pady=20,
    endgame = tk.Button(mm, 
                       text="End Game", 
                       fg="red",
                       bg="yellow",
                       command=exitconf)
    endgame.config(width=20)
    endgame.pack(pady=5,anchor="center")#side=tk.LEFT,padx=10,pady=20,
    hideCons(mm)
    mm.mainloop()
