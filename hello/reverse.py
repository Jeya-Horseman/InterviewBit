"""def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"

print("The reversed string(using loops) is : ")
print(reverse(s)) """

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]
s = "Geeksforgeeks"
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

