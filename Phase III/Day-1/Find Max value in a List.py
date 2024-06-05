#finding max number in list
#from parent to child
def find_max2(index,nums,n):
    if index == n - 1:
        return nums[index]
    nextGreater=find_max2(index+1,nums,n)
    if nextGreater<nums[index]:
        return nums[index]
    return nextGreater
nums=[21,15,34,7,6]
result=find_max2(0,nums,len(nums))
print("Max ele",result)

#from child to parent
def findmax1(index,nums,n,result):
    if index==n:
        print("Max num is:", result)
        return
    if nums[index]>result:
        result=nums[index]
    findmax1(index+1,nums,n,result)

nums=[12,32,11,10]
result=findmax1(0,nums,len(nums),0)
