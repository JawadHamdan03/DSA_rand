## longest subarray that sums to target
# dynamic sliding window

# return the length of the longest  subarray
def longest_subarray(arr:list, target:int)->int:
    sum=0
    l=0
    maxLength=0
    for r in range(len(arr)):
        sum+=arr[r]
        while sum>target:
            sum-=arr[l]
            l+=1
        
        maxLength=max(maxLength,r-l+1)


    return maxLength


print(longest_subarray([4,3,3,2,1,5,2,3,5,10,1],10))