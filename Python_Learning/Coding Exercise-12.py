def temperature_feelings(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    elif temperature < 15:
        return "Cold"

# Example usage:
temperature_example_1 = 10
result_1 = temperature_feelings(temperature_example_1)
print(f"At {temperature_example_1} degrees Celsius, it feels: {result_1}")

temperature_example_2 = 16
result_2 = temperature_feelings(temperature_example_2)
print(f"At {temperature_example_2} degrees Celsius, it feels: {result_2}")

temperature_example_3 = 26
result_3 = temperature_feelings(temperature_example_3)
print(f"At {temperature_example_3} degrees Celsius, it feels: {result_3}")
