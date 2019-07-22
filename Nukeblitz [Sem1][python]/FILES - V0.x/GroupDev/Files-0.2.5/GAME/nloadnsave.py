import os
savpath=os.path.realpath("..")+"\\SAV"
def nsave(s1,s2,filename):
	s=s1+"-"+s2
	sdash=""
	for i in s:
		sdash+=chr(ord(i)-5)
	fn="{savpath}\{filename}.nbsf".format(filename=filename,savpath=savpath)
	file=open(fn,"w")
	file.write(sdash)
	print("Saved file",filename)
	file.close()

def decode(file):
	encoded=file.read()
	file.close()
	decoded=open("{savpath}\dsf.txt".format(savpath=savpath),"w+")
	s=""
	for i in encoded:
		s+=chr(ord(i)+5)
	decoded.write(s)
	n=decoded.name
	decoded.close()
	return n

def nload(filename):
        import os
        fn="{savpath}\{filename}.nbsf".format(filename=filename,savpath=savpath)
        try:
                src=open(fn)
                dcd=decode(src)
                f=open(dcd)
                savdetails=str.split(f.read(),"-")
                fnd=f.name
                f.close()
                os.remove(fnd)
                s1=savdetails[0]
                s2=savdetails[1]
                print("Loaded",filename)
                return (s1,s2)
        except FileNotFoundError:
                return("E","E")
