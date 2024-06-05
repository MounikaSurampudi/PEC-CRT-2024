def printAllSubsets(nums, index, result, value):
    if index == len(nums):
        print(result)
        value[0] += 1
        return

    # Include
    result.append(nums[index])
    printAllSubsets(nums, index + 1, result, value)
    result.pop()

    # Exclude
    printAllSubsets(nums, index + 1, result, value)


nums = [10, 20, 30, 40, 50, 60, 65]

value = [0]

printAllSubsets(nums, 0, [], value)
print(value[0])
