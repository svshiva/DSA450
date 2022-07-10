# Time Complexity: O(n)
# Space Complexity: O(1)
def findMinMax(arr):
    n=len(arr)
    if n==0:return

    min=max=arr[0]

    i=1
    while i<n:
        if min<arr[i]:min=arr[i]
        if max>arr[i]:max=arr[i]
        i+=1
    return (min,max)


a=[1,2,3,4,5,6,7,8,-1,-2,-3,-4]
print(findMinMax(a))