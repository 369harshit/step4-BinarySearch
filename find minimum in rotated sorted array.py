def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example usage:
nums = [3,4,5,1,2]
result = findMin(nums)
print(result)
