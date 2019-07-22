def encnsave(s1,s2,filename):
	s=s1+"-"+s2
	sdash=""
	for i in s:
		sdash+=chr(ord(i)-5)
	fn="{filename}.nbsf".format(filename=filename)
	file=open(fn,"w")
	file.write(sdash)
	file.close()
	

def decode(file):
	encoded=file.read()
	file.close()
	decoded=open("dsf.txt","w+")
	s=""
	for i in encoded:
		s+=chr(ord(i)+5)
	decoded.write(s)
	n=decoded.name
	decoded.close()
	return n

def load(filename):
        import os
        fn="{filename}.nbsf".format(filename=filename)
        src=open(fn)
        dcd=decode(src)
        f=open(dcd)
        savdetails=str.split(f.read(),"-")
        fnd=f.name
        f.close()
        os.remove(fnd)
        s1=savdetails[0]
        s2=savdetails[1]
        return (s1,s2)

encnsave("qwerty","qwerty","sav1")
load("sav1")
