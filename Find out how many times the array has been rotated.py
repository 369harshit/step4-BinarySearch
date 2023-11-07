def findRotationCount(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
nums = [3,4,5,1,2]
rotation_count = findRotationCount(nums)
print(rotation_count)
