n=input()
num=""
char=""
for i in n:
	if i in "0123456789":
		num+=i
	else:
		if(num!="" and char!=""):
			print(char*int(num),end="")
		num=''
		char=i
if(num != "" and char != ""):
	print(char * int(num), end="")