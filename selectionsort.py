def selection_sort(int_list, n):
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if int_list[min] > int_list[j]:
                min = j
        int_list[i], int_list[min] = int_list[min], int_list[i]
    return int_list

int_list = list(map(int, input().split()))
n = len(int_list)
print(selection_sort(int_list, n))