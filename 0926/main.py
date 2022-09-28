def quicksort(arr,l,r):
    if l < r:
        s = partition(arr,l,r)
        quicksort(arr,l,-1)
        quicksort(arr,s+1,r)


def partition(arr,l,r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j





arr = [4,5,6,1,2,7,10]
quicksort(arr,0,6)

print(arr)

