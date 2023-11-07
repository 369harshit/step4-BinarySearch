def smallest_divisor(nums, threshold):
    def divide_sum(divisor):
        sum_result = 0
        for num in nums:
            ceiling_division = (num + divisor - 1) // divisor
            sum_result += ceiling_division
        return sum_result

    # Initialize the search range for the divisor
    left, right = 1, max(nums)

    while left < right:
        mid = (left + right) // 2
        if divide_sum(mid) > threshold:
            left = mid + 1
        else:
            right = mid

    return left


# Example usage:
nums = [1, 2, 5, 9]
threshold = 6
result = smallest_divisor(nums, threshold)
print("Smallest divisor:", result)
