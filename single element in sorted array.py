def singleNonDuplicate(nums):
    for i in range(len(nums)):
        if i == 0 and nums[i] != nums[i + 1]:
            return nums[i]
        elif i == len(nums) - 1 and nums[i] != nums[i - 1]:
            return nums[i]
        elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]

# Example usage:
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
result = singleNonDuplicate(nums)
print(result)  # Output will be 5
