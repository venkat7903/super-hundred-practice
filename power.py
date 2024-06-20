def power(a, b):
    res = 1
    for i in range(b):
        res *= a

    return res 

print(power(2, 10))
print(power(3, 10))