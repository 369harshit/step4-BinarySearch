def upper_bound(arr, x):
    low, high = 0, len(arr) - 1
    result = -1  # Initialize result to an invalid value

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            result = mid  # Update the result and continue searching for a smaller index
            high = mid - 1
        else:
            low = mid + 1

    return result

# Example usage:
N = 4
arr = [1, 2, 2, 3]
x = 2
result = upper_bound(arr, x)
print("Result:", result)
