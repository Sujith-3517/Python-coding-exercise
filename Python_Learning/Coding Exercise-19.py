def strength(password):
    # Check the conditions for a strong password
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong Password"
    else:
        return "Weak Password"
