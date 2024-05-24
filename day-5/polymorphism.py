a=["i1","charan3","am2"]
dic={}
for i in a:
    dic[i[-1]]=i[:-1]
print(dic)
def neword(strin):
    res=""
    for i in strin:
        if i not in res:
            res+=i
    return res
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowLen=len(allowed)
        for i in words:
            newWord=neword(i)
            print(newWord,allowed)
            if len(newWord)>allowLen:
                continue
            elif len(newWord)==allowLen:
                if newWord==allowed:
                    count+=1
                else:
                    continue
            else:
                for k in newWord:
                    if k in  
        return count