def strin(s1,s2):
    if s1 in s2:
        return s2.index(s1)
    return -1
s1='for'
s2='geeksforgeeks'
s=strin(s1,s2)
print(s)
