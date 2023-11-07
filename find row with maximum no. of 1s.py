def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(n):
        cnt_ones = sum(matrix[i])
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    n = 3
    m = 3
    print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))
