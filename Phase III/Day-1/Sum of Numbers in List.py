# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]

nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)
