import os
savpath=os.path.realpath("..")+"\SAV"
def findclear():
        for i in [z for z in os.listdir("{savpath}".format(savpath=savpath)) if ".nbsf" in z]:
                if i==".nbsf":
                        os.remove("{savpath}\\".format(savpath=savpath)+i)
