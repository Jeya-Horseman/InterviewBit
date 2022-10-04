array = [4, 5,6,5,6,7, 8]
def getsubrray(arr, s):
    result=[]
    for x in range(len(arr)):
        result.append(arr[x])
        while(sum(result)>s):
            result.pop(0)
        if(sum(result)==s):
            return result
    return[]
print(getsubrray(array,11))

#https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/1753357/Clear-solution!-Easy-to-understand-with-diagrams%5C