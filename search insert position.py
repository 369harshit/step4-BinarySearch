def searchInsert(nums, target):
    # Initialize low and high pointers for binary search
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid  # Element found at index 'mid'
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low  # Element not found, return the insert position

# Example usage:
nums = [1, 3, 5, 6]
target = 2
result = searchInsert(nums, target)
print(result)
