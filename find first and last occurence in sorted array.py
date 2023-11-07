def find_first_last_occurrence(nums, target):
    # Initialize variables to store first and last occurrence indices
    first_occurrence = -1
    last_occurrence = -1

    # Find the first occurrence
    for i in range(len(nums)):
        if nums[i] == target:
            first_occurrence = i
            break

    # Find the last occurrence
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            last_occurrence = i
            break

    return [first_occurrence, last_occurrence]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = find_first_last_occurrence(nums, target)
print(result)
