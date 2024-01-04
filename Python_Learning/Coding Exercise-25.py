def get_max(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    return f"Max: {max_grade}, Min: {min_grade}"

# Example usage:
grades_list = [8.5, 9.7, 7.8, 9.2, 6.5]
result = get_max(grades_list)
print(result)
