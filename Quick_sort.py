def QuickSort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        QuickSort(arr,left,partition_pos-1)
        QuickSort(arr,partition_pos+1,right)
def partition(arr,left,right):
    i=left
    j=right
    pivot=arr[right]
    while i<j:
        while i<j and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i    
arr=[33,44,22,11,55,66,88]
QuickSort(arr,0,len(arr)-1)
print(arr)
    
            
