# find the intersection of two arrays

def intersection(arr1:list,arr2:list)->list:
    st = set()
    res :list=[]
    for i in arr1:
        st.add(i)
    
    for i in arr2:
        if i in arr1:
            res.append(i)
        
    return res



print(intersection([4,2,1,6],[3,6,9,2,10]))