names = ["John", "Smith", "Sen", "Plakay", "Dora", "Ngacely"]

for name in names:
    match name:
        case "John":
            print("Hello " + name)
        case "Smith":
            print("Hello " + name)
        case "Sen":
            print("Namaste " + name)
        case "Plakay":
            print("Namaste " + name)
        case "Dora":
            print("Hallo " + name)
        case "Ngacely":
            print("Hallo " + name)
        case _:
            print("Greeting not specified for " + name)
