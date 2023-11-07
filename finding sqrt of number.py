import math

def find_square_root_floor(n):
    result = math.floor(math.sqrt(n))
    return result

# Example usage
number = 28
result = find_square_root_floor(number)
print(f"The square root of {number} is: {result}")
