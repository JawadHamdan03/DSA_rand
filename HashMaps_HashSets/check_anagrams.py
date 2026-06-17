# check if two strings are anagrams 


def anagrams(s1:str,s2:str)->bool:
    if not(len(s1)==len(s2)):
        return False;

    dic1 = dict()
    dic2 = dict()

    for c in s1:
        if c not in dic1:
            dic1[c]=1
        else :
            dic1[c]+=1

    for c in s2:
        if c not in dic2:
            dic2[c]=1
        else :
            dic2[c]+=1

    
    for c in dic1:
        if not(dic1[c] == dic2[c]):
            return False
        
    return True;


print(anagrams("ttara","atrta"))
print(anagrams("ttara","atrtaa"))