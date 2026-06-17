# Two Sum : find two elements of an array that sums to target, and return their indices


def two_sum(arr:list, target:int) -> tuple:

    map = dict()

    for i in range(len(arr)):
        if (target-arr[i]) in map:
            return (map[target-arr[i]],i)
        if arr[i] not in map:
            map[arr[i]]=i
        
    return (-1,-1)



print(two_sum([1,5,2,4,6,12],17))