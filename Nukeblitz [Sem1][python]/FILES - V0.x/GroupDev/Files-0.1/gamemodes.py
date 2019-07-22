import gameplay
def ng():
    gameplay.game(0,[])
    gameplay.gameactual()
def lg():
    f1=open("lastplayedq.txt")
    currq=int(f1.read())
    f1.close()
    f1=open("lastplayedseq.txt")
    seq=(f1.read()).split(',')
    f1.close()
    gameplay.game(currq,seq)
    gameplay.gameactual()
