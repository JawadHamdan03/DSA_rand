# find the most Frequent element in a string
# counting 

def mostFrequent(s:str):
    dic = dict()
    for c in s :
        if c not in dic:
            dic[c]=1
        else :
            dic[c]+=1
    
    maxElem='*'
    maxCount=0
    for c,v in dic.items() :
        if v >= maxCount:
            maxElem=c
            maxCount=v
    
    return maxElem


print(mostFrequent("jawaddd"))