def minCostTree(cost):
    n = len(cost)
    cache = [-1] * n 
    
    def solve(index, cost, n):
        if index >= n:
            return 0
        elif cache[index] != -1:
            return cache[index]

        jump1 = solve(index+1, cost, n)
        jump2 = solve(index+2, cost, n)
        cache[index] = min(jump1, jump2) + cost[index]
        return cache[index]
    option1 = solve(0, cost, n)
    option2 = solve(1, cost, n)
    return min(option1, option2)

cost = list(map(int, input().split(",")))
print(minCostTree(cost))