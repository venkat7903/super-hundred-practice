def cal_sum(n):
    if (n == 0):
        return 0
    rem = n % 10
    n = n // 10
    return rem + cal_sum(n)

n = int(input())
print(cal_sum(n))