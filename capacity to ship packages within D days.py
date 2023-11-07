def shipWithinDays(weights, D):
    def count_days(capacity):
        days = 1
        current_capacity = 0
        for weight in weights:
            if current_capacity + weight > capacity:
                days += 1
                current_capacity = 0
            current_capacity += weight
        return days

    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        required_days = count_days(mid)

        if required_days > D:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
result = shipWithinDays(weights, D)
print("Minimum capacity required:", result)
