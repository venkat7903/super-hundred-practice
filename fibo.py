# def fibo(n):
#     if (n==0):
#         return 0
#     if (n==1):
#         return 1
#     return fibo(n-1) + fibo(n-2)
def findNthTermUsingCache(n, cache):
    if n == 1:
        return 1 
    if n == 0:
        print(0)
        return 0
    elif cache[n] != -1:
        return cache[n]
 
 
    result1 = findNthTermUsingCache(n - 1, cache)
    result2 = findNthTermUsingCache(n - 2, cache)
    cache[n] = result1 + result2
    return result1 + result2 

n= int(input())
cache = [-1] * (n + 1)
# fibo_list = []
# for i in range(0,n+1):
#     fibo_list.append(findNthTermUsingCache(i, cache))
# print(fibo_list)
print(findNthTermUsingCache(n, cache))