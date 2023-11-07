def findKthMissing(nums, k):
    num = 1  # Start from the first positive integer
    count = 0  # Counter for missing numbers

    while True:
        if num not in nums:
            count += 1
            if count == k:
                return num
        num += 1

# Example usage:
nums = [2,3,4,7,11]
k = 5
result = findKthMissing(nums, k)
print(result)
