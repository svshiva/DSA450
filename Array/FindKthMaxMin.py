# wrong solution
# do not use
def kMaxMin(arr,k):
    n=len(arr)
    if not n:return
    min=max=arr[0]
    
    i=1
    while i<n:
        if arr[i]>max:max=arr[i]
        if arr[i]<min:min=arr[i]
        i+=1
    
    i=0
    _max = min
    _min=max
    while i<k-1:
        j=0
        while j<n:
            if _max<arr[j] and arr[j] < max: _max=arr[j]
            if _min>arr[j] and arr[j] > min: _min=arr[j]
            j+=1
        min, max, _min, _max= _min, _max, max, min
        i+=1
    return (min,max)

a=[1,2,3,4,5,6,7,8,-1,-2,-3,-4]
print(kMaxMin(a,4))