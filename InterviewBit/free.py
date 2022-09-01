l=[x for x in range(201) if sum(int(c) for c in str(x))==9 and str(x)=="".join(sorted(str(x)))]
print(l)