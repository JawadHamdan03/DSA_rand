## Count number of subarrays with K window that sums to target 
# fixed window

def countSubArraysSumsToTarget(arr:list,k:int, target:int)->int:
    count = 0
    curr_sum=0
    for i in range(k):
        curr_sum+=arr[i]
    
    if curr_sum==target:
            count+=1

    for i in range(k,len(arr)):
        
        curr_sum-=arr[i-k]
        curr_sum+=arr[i]
        if curr_sum==target:
            count+=1
        

    return count


print(countSubArraysSumsToTarget([2,3,2,2,3,1,3,8,5,0,2,4],3,7))