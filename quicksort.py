def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high 
    while i < j:
        while (arr[i] <= pivot and i<high): i+=1
        while (arr[j] >= pivot and j > low): j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)

arr = [8, 1, 3,6, 5,4,2]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)