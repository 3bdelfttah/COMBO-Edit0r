import sys
import re
msg=''''
░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║░░██║
██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░

███████╗██████╗░██╗████████╗░█████╗░██████╗░
██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██║░░██║██║░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║░░██║██║░░░██║░░░██║░░██║██╔══██╗
███████╗██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║
╚══════╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                COMBO-Edit0r v0.1 by 3bdelfttah

'''
print(msg)

helpmsg='''
                       [Help menu]
_________________________________________
-h | --help -----> open help menu

-w  ----->  -w <path to list>                     #Always required as first arg

-d -----> removes duplicates from list


-f -----> -f <emailservice name>  
filters list by emailservice name
             

-u -----> converts email:password list to user:password list

-o -----> -o <path to save into or set txt file name that will be saved in the current dir>
          #Always required as last arg 
_________________________________________
'''
#Handling sys.argv input errors 
if len(sys.argv)==1:
	print("[Error] No arguments were given ")
	print("[-] try argu -h or --help for help menu")
	exit()
if sys.argv[1]=='-h' or sys.argv[1]=='--help':
	print(helpmsg)
	exit()
argvs=['-h','--help','-w']
if sys.argv[1] not in argvs:
	print("[!] [Error] Wrong argument ! !")
	print("[-] try argu -h or --help for help menu")
	exit()
if len(sys.argv)==3 :
	print("[Error] No process argu were given ")
	print("[-] try argu -h or --help for help menu")
	exit()
argvs_3=['-f','-u','-d']
if sys.argv[3] not in argvs_3 :
	print("[!] [Error] Wrong argument ! !")
	print("[-] try argu -h or --help for help menu")
	exit()
if sys.argv[-2] !='-o' :
	print("[!] [Error] argument missing or may be wrong ! !")
	print("[-] try -o as last argu before path ")
	print("[-] try argu -h or --help for help menu")
	exit()
#Handling errors with sys.argv[1],[2] input and opening file 	
try:
		if sys.argv[1]=='-w' :
			f=open(f"{sys.argv[2]}",'r')
  #defining dic a to use in removing duplicates 
			a={}
 #defining list y , c to use in removing /n from all file  f content to append in list b
			y=[]
			c=[]
		for ia in f :
 #appending file content in dic a & list c
			a.update({ia[:ia.index(':')]:ia[ia.index(':')+1:]})
			c.append(ia[:ia.index(':')])
			c.append(ia[ia.index(':')+1:])
		for x in c:
			y.append(x.replace("\n", ""))
		b=list(y)
except NameError:
	pass
except IndexError:
	print("[Error] Invalid input ! ! ")
	print("[-] try argu -h or --help for help menu")
	exit()		        	
except FileNotFoundError:
	print(f"[Error] Invalid path , File not found '{sys.argv[2]}' ! ! ")
	exit()
except ValueError:
	print("[Error] Combolist not valid ! !")
	print(f"[-] try 'python COMBO-C0rrect0r.py -c {sys.argv[2]} ' ")
	exit()	
	
#_______________________________________
#defining function to filter combolist emails by email service name
def filterbymail_serv(ar,loc):
	z=[]
	servname=[]
#appending all emails (that in main list b that contains all file content in form email in first index and password in next index) in list z
	for em_index in range(0,len(b),2):
		z.append(b[em_index])
# detecting email service name from email and appending it in list servname	
	for n in z:
		servname.append(n[n.index('@')+1:n.index('.')])
#checking if given service name by user is not in servname list before opening file to save filtered emails into or it will be useless
	if ar not in servname :
		print(" No emails found with this service name !! ".center(10,"#"))
		exit()
	fbym=open(f"{loc}.txt",'a')
	for email_index in range(0,len(b)-1,2):
#validating emails with given service name with regex
		email=re.findall(rf"\w+.?\w+.?_?\w?d?_?[@]{ar}\....",b[email_index])
#printing filtered-emails:pass into file 
		for e in email:
			print(f"{e}:{b[b.index(e)+1]}",file=fbym)
	fbym.close()
	print(" PROCESS is DONE SUCCESSFULLY ! ! ".center(48,'-'))
#_______________________________________
def remove_dup(loc):
	rdf=open(f"{loc}.txt","a")
#defining list co_list and appending dic a keys (non duplicated emails ) in it as we do in the next for loop 
	co_list=[]
	final=[]
	for em in a:
		rdf.write(f"{em}:{a[em]}")
		co_list.append(em)
		co_list.append(a[em])
	reps=[]
	for xx in co_list:
		reps.append(xx.replace("\n", ""))
#replacing co_list with comp_list (no /n in it)	
	comp_list=list(reps)
# looping on main list (b) to check duplicated emails in it with emails in comp_list but with different password than one that in comp_list
	for ind in range(0,len(b),2):
	 for iii in range(0,len(co_list),2):
	 		 if b[ind]== comp_list[iii]:
	 		 	if b[ind+1] != comp_list[iii+1]:
#after collecting non duplicated emails and duplicated but with differrent passwords , appending it with its passwords in list final in usual combolist form email:password 
	 		 		final.append(f"{b[ind]}:{b[ind+1]}")
	 		 else:
	 		 	continue

	for li in final:
#printing final list content in file 
	 		 print(li,end="\n",file=rdf)
	rdf.close()
	print(" PROCESS is DONE SUCCESSFULLY ! ! ".center(48,'-'))		 
#_______________________________________
def user_pw_convert(dirc):
	upwf=open(f'{dirc}.txt','a')
#defining list user_pw to contain our function`s result 
	user_pw=[]
	for user_ind in range(0,len(b),2):
		user=b[user_ind]
		pw=b[user_ind+1]
#extracting username by slicing email and take the slice before (@) and appending it with its password in user_pw list
		user_pw.append(f"{user[:user.index('@')]}:{pw}")
	for up in user_pw:
		print(up,file=upwf)
	upwf.close()
	print(" PROCESS is DONE SUCCESSFULLY ! ! ".center(48,'-'))
#_______________________________________
# The next 3 functions are for handling more errors and to print an announcement just before the function starts working 

def dupremover_start():
	if sys.argv[3]=='-d' and sys.argv[4]=='-o' and sys.argv[1]=='-w':
		print("[INF] Working on Removing duplicates ... ")
		remove_dup(sys.argv[5])
		
#_______________________________________
def filter_start():
	
	if sys.argv[3]=='-f' and sys.argv[1]=='-w' :
		if sys.argv[4]=='-o':
			print("[Error] Email service name missing ! ! ")
			print("[-] Provide email service name after -f to filter ")
			exit()
		if sys.argv[5]=='-o':
				print(f"[INF] Working on Filtering {sys.argv[4]} Emails ... ")
				filterbymail_serv(sys.argv[4],sys.argv[6])
		
#_______________________________________
def convert_start():
	if sys.argv[3]=='-u' and sys.argv[4]=='-o' and sys.argv[1]=='-w':
		print("[INF] Working on Converting to user:pass ... ")
		user_pw_convert(sys.argv[5])				#_______________________________________
try:
	dupremover_start()
	filter_start()
	convert_start()
except IndexError:
	print("[Error] Invalid input ! ! ")
	print("[-] try argu -h or --help for help menu")
except FileNotFoundError:
	print(f"[Error] Invalid path or file name '{sys.argv[-1]}' ")
	exit()
f.close()	

	
	
	
