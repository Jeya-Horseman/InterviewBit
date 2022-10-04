def isSubstring(s1, s2):
    M = len(s1)
    N = len(s2)
    s=N-M+1
    for i in range(s):
        for j in range(M):
            if (s2[i + j] != s1[j]):
                break
        if j + 1 == M:
            return i

    return -1
if __name__ == "__main__":
    s1 = "for"
    s2 = "geeksforgeeks"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))
