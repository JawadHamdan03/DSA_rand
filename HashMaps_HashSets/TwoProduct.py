# find the two elements in an array thats their product is equal to target 

def two_product(arr:list , target:int) -> tuple:

    map = dict()

    for i in range(len(arr)):
        if (target//arr[i])in map:
            return (map[target//arr[i]],i)

        if arr[i] not in map:
            map[arr[i]]=i

    return (-1,-1)



print(two_product([1,5,2,4,6,12],12))
