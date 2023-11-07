def is_possible(time, boards, painters, k):
    painters_required = 1
    current_time = 0

    for board in boards:
        if current_time + board > time:
            painters_required += 1
            current_time = 0

        current_time += board

    return painters_required <= k

def min_time_to_paint_boards(boards, k):
    low = max(boards)  # Minimum possible time
    high = sum(boards)  # Maximum possible time

    while low < high:
        mid = (low + high) // 2

        if is_possible(mid, boards, k, k):
            high = mid
        else:
            low = mid + 1

    return low

# Example usage
boards = [10, 20, 30, 40]
k = 2
result = min_time_to_paint_boards(boards, k)
print("Minimum time required:", result)
