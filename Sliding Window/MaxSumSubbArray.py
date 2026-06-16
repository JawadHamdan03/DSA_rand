## max subarray sum of  of size k

## Fixed Sliding Window
def maxSubArraySum(arr:list , k:int) -> int:
    max_sum=-10000000
    curr_sum=0
    for i in range(k):
        curr_sum+=arr[i]
    
    max_sum=curr_sum

    for i in range(k,len(arr)):
        curr_sum+=arr[i]
        curr_sum-=arr[i-k]
        max_sum=max(max_sum,curr_sum)
    
    return max_sum


print(maxSubArraySum([4,2,1,-9,8,4,3],3))