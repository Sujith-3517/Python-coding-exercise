FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    elif temperature >= BOILING_POINT:
        return "Gas"

# Example usage:
temperature_example = 25
result = water_state(temperature_example)
print(f"At {temperature_example} degrees Celsius, the water state is: {result}")
