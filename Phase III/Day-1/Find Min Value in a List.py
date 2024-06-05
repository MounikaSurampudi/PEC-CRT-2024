#finding minimum in a list
def find_min2(index,nums,n):
    if index == n - 1:
        return nums[index]
    nextsmaller=find_min2(index+1,nums,n)
    if nextsmaller>nums[index]:
        return nums[index]
    return nextsmaller
nums=[21,15,34,7,9]
result=find_min2(0,nums,len(nums))
print("Min ele",result)
