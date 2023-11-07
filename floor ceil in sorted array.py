def find_floor_ceiling(arr, n, x):
    floor = None
    ceiling = None

    for num in arr:
        if num == x:
            floor = ceiling = num
            break
        elif num < x:
            floor = num
        elif num > x:
            ceiling = num
            break

    return floor, ceiling

# Example usage:
n = 6
arr = [3, 4, 4, 7, 8, 10]
x = 5

floor, ceiling = find_floor_ceiling(arr, n, x)
print("Result:",floor, ceiling)
