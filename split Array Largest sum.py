def splitArrayLargestSum(nums, k):
    def is_valid(max_sum):
        count = 1
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                count += 1
                current_sum = num
                if count > k:
                    return False
        return True

    left, right = max(nums), sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage:
N = 5
a = [1, 2, 3, 4, 5]
k = 3
result = splitArrayLargestSum(a, k)
print("Result:", result)
