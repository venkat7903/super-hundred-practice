def move_zeroes_to_end(nums,n):
    i=0
    j=n-1
    while(i<=j):
        while(nums[i] != 0):
            i+=1
        while(nums[j] == 0): 
            j-=1
        if (i<=j):
            nums[i], nums[j] = nums[j], nums[i]


def main():
    nums = [5, 0, 1, 3, 4, 0, 5, 6] #list(map(int, input().split()))
    n = len(nums)
    move_zeroes_to_end(nums, n)
    print(nums)
main()