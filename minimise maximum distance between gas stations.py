def min_max_gas_distance(arr, k):
    n = len(arr)
    low = 0.0  # Minimum possible distance
    high = float(arr[-1])  # Maximum possible distance (at the end of the axis)

    while low < high:
        mid = (low + high) / 2
        count = 0

        for i in range(1, n):
            count += int((arr[i] - arr[i-1]) / mid)  # Count how many stations can be added with mid as the maximum distance

        if count > k:
            low = mid + 0.001  # Increase low to find a smaller maximum distance
        else:
            high = mid - 0.001  # Decrease high to find a larger maximum distance

    return round(low, 6)  # Round to 6 decimal places

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
result = min_max_gas_distance(arr, k)
print("Minimum maximum distance between gas stations:", result)
