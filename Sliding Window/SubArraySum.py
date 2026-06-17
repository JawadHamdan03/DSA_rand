# find the start, end indices of a subarray that sums to target 
# Dynamic Sliding Window

def find_subarray_sum_target(arr:list,target:int)->tuple:
    
    l=0
    sum=arr[l]
    for r in range(1,len(arr)):
        sum+=arr[r]
        while sum>target:
            sum-=arr[l]
            l+=1
        if sum==target :
            return (l,r)

    return (-1,-1)


print(find_subarray_sum_target([3,5,4,8,6,2],18))