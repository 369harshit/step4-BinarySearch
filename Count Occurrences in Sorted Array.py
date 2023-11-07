def count_occurrences(arr, X):
    count = 0

    for num in arr:
        if num == X:
            count += 1

    return count

# Example usage:
N = 7
X = 3
array = [2, 2, 3, 3, 3, 3, 4]
result = count_occurrences(array, X)
print(result)
