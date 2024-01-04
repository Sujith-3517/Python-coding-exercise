def calculate_average(my_list):
    if not my_list:
        return None  # Return None for an empty list to avoid division by zero

    # Calculate the average
    average = sum(my_list) / len(my_list)
    return average

# Example usage:
example_list = [10, 20, 30, 40]
result = calculate_average(example_list)
print(f"The average of the list {example_list} is: {result}")
