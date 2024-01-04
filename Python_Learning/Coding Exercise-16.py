def temperature_feelings(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# Example usage:
temperature_example_1 = 10
result_1 = temperature_feelings(temperature_example_1)
print(f"At {temperature_example_1} degrees Celsius, it feels: {result_1}")

temperature_example_2 = 7
result_2 = temperature_feelings(temperature_example_2)
print(f"At {temperature_example_2} degrees Celsius, it feels: {result_2}")

temperature_example_3 = 5
result_3 = temperature_feelings(temperature_example_3)
print(f"At {temperature_example_3} degrees Celsius, it feels: {result_3}")
