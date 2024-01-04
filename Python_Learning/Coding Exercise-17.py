def check_string_length(input_string):
    return len(input_string) >= 8

# Example usage:
string_example_1 = "mypass"
result_1 = check_string_length(string_example_1)
print(f"For the string '{string_example_1}', the result is: {result_1}")

string_example_2 = "mylongpassword"
result_2 = check_string_length(string_example_2)
print(f"For the string '{string_example_2}', the result is: {result_2}")
