def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right)// 2

        # Check if the middle element is greater than its neighbors
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

# Example usage:
nums = [1,2,3,1]
result = findPeakElement(nums)
print(result)  # Output will be 2
