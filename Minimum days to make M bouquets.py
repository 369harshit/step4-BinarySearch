def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    left, right = min(bloomDay), max(bloomDay)
    
    while left < right:
        mid = (left + right) // 2
        bouquets, flowers = 0, 0

        for day in bloomDay:
            if day <= mid:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        if bouquets < m:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3

result = minDays(bloomDay, m, k)
print(result)
