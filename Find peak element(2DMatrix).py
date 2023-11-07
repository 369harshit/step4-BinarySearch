def find_peak_element(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            is_peak = True

            # Check if the current element is greater than its neighbors
            if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                is_peak = False
            if i < rows - 1 and matrix[i][j] < matrix[i + 1][j]:
                is_peak = False
            if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                is_peak = False
            if j < cols - 1 and matrix[i][j] < matrix[i][j + 1]:
                is_peak = False

            # If the current element is a peak, return its position
            if is_peak:
                return i, j

# Example usage
matrix = [[1,4],[3,2]]

peak_row, peak_col = find_peak_element(matrix)
print(f"Peak Element: {matrix[peak_row][peak_col]} at position ({peak_row}, {peak_col})")
