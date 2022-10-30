import sys
arg=['-c']
if len(sys.argv)!=3:
	print("Error")
	exit()
try:
	if sys.argv[1]=='-c':
		t=open(f"{sys.argv[2]}",'r')
		m=[]
		for i in t:
			if i != "\n":
				m.append(i)
		t.close()
except FileNotFoundError:
	print(f"[Error] Invalid path , File not found '{sys.argv[2]}' ! ! ")
	exit()	
s=open(f"{sys.argv[2]}",'w')
for u in m:
	s.write(u)
print("PROCESS is DONE SUCCESSFULLY".center(48,"-"))
	