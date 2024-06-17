def merge(arr,left, mid, right):
    n = right - left + 1
    new_arr = [0] * n
    i = left 
    j = mid+1
    k = 0
    while i<=mid and j <= right:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            i+=1
        else:
            new_arr[k] = arr[j]
            j+= 1
        k+=1
    while i <= mid:
        new_arr[k] = arr[i]
        i+=1
        k+=1
    while j <= right:
        new_arr[k] = arr[j]
        j+=1
        k+=1
    for c in range(0, n):
        arr[left+c] = new_arr[c]
    return arr

def merge_sort(arr, left, right):
    if left == right:
        return 
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    return merge(arr, left, mid, right)

arr = [8, 1, 3,6, 5,4,2]
n = len(arr)
print(merge_sort(arr, 0, n-1))