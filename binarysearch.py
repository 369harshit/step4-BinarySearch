def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if nums[mid] == target:
            return mid  # Target found, return its index
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half of the array
        else:
            right = mid - 1  # Target is in the left half of the array

    return -1  # Target not found in the array

# Example usage:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = binary_search(nums, target)
print(result)  # Output: -1
