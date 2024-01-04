def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    elif temperature >= 100:
        return "Gas"

temperature_example = 25
result = water_state(temperature_example)
print(f"At {temperature_example} degrees Celsius, the water state is: {result}")
