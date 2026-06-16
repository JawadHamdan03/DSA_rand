## Max Product of subbarays sum of size k
# fixed sliding window
def maxSubArrPrd(arr:list, k:int)->int:
    
    curr_prod=1

    for i in range(k):
        curr_prod*=arr[i]

    max_prod=curr_prod

    for i in range(k,len(arr)):
        curr_prod//=arr[i-k]
        curr_prod*=arr[i]
        max_prod=max(max_prod,curr_prod)
    
    return max_prod


print(maxSubArrPrd([4,2,1,-9,8,4,3],3))


