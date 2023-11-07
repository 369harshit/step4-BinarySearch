def min_eating_speed(piles, h):
    def can_eat_all(speed):
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + speed - 1) // speed
        return hours_needed <= h

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage
piles = [3,6,7,11]
h = 8
result = min_eating_speed(piles, h)
print(f"Koko's maximum bananas eaten within {h} hours: {result}")
