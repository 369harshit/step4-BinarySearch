def is_valid_distribution(pages, students, max_pages):
    student_count = 1
    current_pages = 0

    for page in pages:
        if current_pages + page > max_pages:
            student_count += 1
            current_pages = 0

        current_pages += page

    return student_count <= students

def allocatePages(pages, students):
    if students > len(pages):
        return -1  # Invalid input

    low = max(pages)  # Minimum possible maximum page count for a student
    high = sum(pages)  # Maximum possible maximum page count for a student

    while low < high:
        mid = (low + high) // 2

        if is_valid_distribution(pages, students, mid):
            high = mid
        else:
            low = mid + 1

    return low

# Example usage
pages = [12, 34, 67, 90]
students = 2
result = allocatePages(pages, students)
print("Minimum maximum pages for a student:", result)
