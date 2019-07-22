import tkinter as tk
gameqsops=[{"Hi. Do we start?":{"Y":1,"N":2}},
           {"Good choice. Is this a test?":{"Ya":3,"Na":4}},
           {"Why? Not ready yet?":{"Yo":5,"No":6}},
           {"A test for what? NUKE?":{"N":6,"Y":5}},
           {"Ah I got Scared.":{"Why":5,"What":6}},
           {"This was a nuke test.":{"I was right!":6,"Hell yeah!":6}},
           {"Congrats, you beat the game and came to the end. Please save and quit.":{"Please":6,"Save":6}}]
#gameqsops=[{"":{"":n1,"":n2}}..........]
cq=
s=
v1=-1
v2=-1
    
def game(currq,seq):
    global cq
    global s
    cq=currq
    s=seq

def gameactual():
    global v1
    global v2
    qwindow=tk.Tk()
    qwindow.config(bg="blue")
    qwindow.geometry("500x300+375+175")
    q=gameqsops[cq]
    tex=[p for p in q][0]
    opts=q[tex]
    options=[p for p in opts]
    choiceq=[opts[p] for p in opts]
    v1=choiceq[0]
    v2=choiceq[1]
    que=tk.Message(qwindow,text=tex)
    que.config(bg="blue",fg="black",font=("Arial",10),width=480)
    que.pack(side=tk.TOP,padx=10,pady=10,anchor="center")
    button1=tk.Button(qwindow,text=options[0],command=app1)
    button1.config(width=10)
    button1.pack(side=tk.LEFT,padx=20,pady=10,anchor="center")
    button2=tk.Button(qwindow,text=options[1],command=app2)
    button2.config(width=10)
    button2.pack(side=tk.LEFT,padx=20,pady=10,anchor="center")
    saq=tk.Button(qwindow,text="Save and Quit to Menu",command=saqmenu)
    saq.pack(side=tk.BOTTOM)


def app1():
    s.append(v1)
    cq=v1
    gameactual()

def app2():
    s.append(v2)
    cq=v2
    gameactual()

def saqmenu():
    f1=open("lastplayedq.txt",mode="w")
    f1.write(str(cq))
    f1.close()
    f1=open("lastplayedseq.txt",mode="w")
    f1.write(str(s))
    f1.close()
