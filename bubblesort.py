def bubble_sort(int_list, n):
    for i in range(n-1, 1, -1):
        for j in range(0, i):
            if int_list[j] > int_list[j+1]:
                int_list[j], int_list[j+1] = int_list[j+1], int_list[j]
    return int_list

int_list = list(map(int, input().split()))
n = len(int_list)
print(bubble_sort(int_list, n))