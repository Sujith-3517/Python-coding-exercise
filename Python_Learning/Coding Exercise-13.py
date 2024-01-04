from datetime import date

def get_age(year_of_birth, current_year=date.today().year):
    age = current_year - year_of_birth
    return age

# Example usage:
year_of_birth_example = 1990
current_year_example = 2022

result = get_age(year_of_birth_example, current_year_example)
print(f"If born in {year_of_birth_example} and it's {current_year_example}, the age is: {result}")

# Using default current_year (current year)
result_default_year = get_age(year_of_birth_example)
print(f"If born in {year_of_birth_example} and it's the current year, the age is: {result_default_year}")
